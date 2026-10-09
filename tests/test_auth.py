from datetime import timedelta

from jose import jwt

from app.auth import ALGORITHM, SECRET_KEY, create_access_token, get_password_hash, verify_password


def test_password_hash_roundtrip():
    hashed = get_password_hash("secret")

    assert hashed != "secret"
    assert verify_password("secret", hashed)
    assert not verify_password("wrong", hashed)


def test_access_token_contains_subject_and_expiry():
    token = create_access_token({"sub": "user@example.com"}, timedelta(minutes=5))

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    assert payload["sub"] == "user@example.com"
    assert "exp" in payload


def test_register_creates_user(client, credentials):
    response = client.post("/auth/register", json=credentials)

    assert response.status_code == 201
    body = response.json()
    assert body["email"] == credentials["email"]
    assert body["is_active"] is True
    assert "password" not in body
    assert "hashed_password" not in body


def test_register_rejects_duplicate_email(client, credentials):
    client.post("/auth/register", json=credentials)

    response = client.post("/auth/register", json=credentials)

    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_register_rejects_invalid_email(client):
    response = client.post("/auth/register", json={"email": "not-an-email", "password": "x"})

    assert response.status_code == 422


def test_login_returns_bearer_token(client, credentials):
    client.post("/auth/register", json=credentials)

    response = client.post(
        "/auth/login",
        data={"username": credentials["email"], "password": credentials["password"]},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["token_type"] == "bearer"
    assert body["access_token"]


def test_login_rejects_wrong_password(client, credentials):
    client.post("/auth/register", json=credentials)

    response = client.post(
        "/auth/login",
        data={"username": credentials["email"], "password": "wrong-pass"},
    )

    assert response.status_code == 401


def test_login_rejects_unknown_user(client):
    response = client.post(
        "/auth/login",
        data={"username": "ghost@example.com", "password": "whatever"},
    )

    assert response.status_code == 401
