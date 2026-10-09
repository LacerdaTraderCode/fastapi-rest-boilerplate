def create_item(client, headers, title="Item", description=None):
    return client.post(
        "/items/",
        json={"title": title, "description": description},
        headers=headers,
    )


def test_items_require_authentication(client):
    assert client.get("/items/").status_code == 401
    assert client.post("/items/", json={"title": "x"}).status_code == 401


def test_create_item(client, auth_headers):
    response = create_item(client, auth_headers, "Book", "Hardcover")

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == "Book"
    assert body["description"] == "Hardcover"
    assert body["owner_id"] == 1


def test_create_item_requires_title(client, auth_headers):
    response = client.post("/items/", json={"description": "no title"}, headers=auth_headers)

    assert response.status_code == 422


def test_list_items_supports_pagination(client, auth_headers):
    for index in range(3):
        create_item(client, auth_headers, f"Item {index}")

    response = client.get("/items/", params={"skip": 1, "limit": 1}, headers=auth_headers)

    assert response.status_code == 200
    assert [item["title"] for item in response.json()] == ["Item 1"]


def test_list_items_only_returns_own_items(client, make_auth_headers):
    first = make_auth_headers("first@example.com")
    second = make_auth_headers("second@example.com")
    create_item(client, first, "Private")

    response = client.get("/items/", headers=second)

    assert response.json() == []


def test_get_item(client, auth_headers):
    item_id = create_item(client, auth_headers, "Lookup").json()["id"]

    response = client.get(f"/items/{item_id}", headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["title"] == "Lookup"


def test_get_missing_item_returns_404(client, auth_headers):
    response = client.get("/items/999", headers=auth_headers)

    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_cannot_access_item_owned_by_another_user(client, make_auth_headers):
    owner = make_auth_headers("owner@example.com")
    intruder = make_auth_headers("intruder@example.com")
    item_id = create_item(client, owner).json()["id"]

    assert client.get(f"/items/{item_id}", headers=intruder).status_code == 404
    assert client.delete(f"/items/{item_id}", headers=intruder).status_code == 404


def test_update_item(client, auth_headers):
    item_id = create_item(client, auth_headers, "Old").json()["id"]

    response = client.put(
        f"/items/{item_id}",
        json={"title": "New", "description": "Updated"},
        headers=auth_headers,
    )

    assert response.status_code == 200
    assert response.json()["title"] == "New"
    assert response.json()["description"] == "Updated"


def test_update_missing_item_returns_404(client, auth_headers):
    response = client.put("/items/999", json={"title": "New"}, headers=auth_headers)

    assert response.status_code == 404


def test_delete_item(client, auth_headers):
    item_id = create_item(client, auth_headers).json()["id"]

    response = client.delete(f"/items/{item_id}", headers=auth_headers)

    assert response.status_code == 204
    assert client.get(f"/items/{item_id}", headers=auth_headers).status_code == 404
