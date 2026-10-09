from app.auth import create_access_token


def test_root_returns_service_info(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["docs"] == "/docs"


def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_read_current_user(client, auth_headers):
    response = client.get("/users/me", headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["email"] == "user@example.com"


def test_current_user_requires_token(client):
    assert client.get("/users/me").status_code == 401


def test_current_user_rejects_malformed_token(client):
    response = client.get("/users/me", headers={"Authorization": "Bearer invalid"})

    assert response.status_code == 401


def test_current_user_rejects_token_without_subject(client):
    token = create_access_token({})

    response = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 401


def test_current_user_rejects_token_for_unknown_user(client):
    token = create_access_token({"sub": "ghost@example.com"})

    response = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 401
