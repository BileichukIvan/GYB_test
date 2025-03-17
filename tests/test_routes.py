import json
import uuid


def test_create_user(client, app):
    with app.app_context():
        unique_email = f"{uuid.uuid4()}@example.com"
        response = client.post(
            "/users", json={"name": "John Doe", "email": unique_email}
        )
        data = json.loads(response.data)

        assert response.status_code == 201
        assert data["name"] == "John Doe"
        assert data["email"] == unique_email
        assert "id" in data


def test_create_user_missing_fields(client, app):
    with app.app_context():
        response = client.post("/users", json={"name": "John Doe"})
        data = json.loads(response.data)

        assert response.status_code == 400
        assert data["error"] == "Name and email are required"


def test_get_users(client, app):
    with app.app_context():
        unique_email = f"{uuid.uuid4()}@example.com"
        client.post("/users", json={"name": "John Doe", "email": unique_email})

        response = client.get("/users")
        data = json.loads(response.data)

        assert response.status_code == 200
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["name"] == "John Doe"
        assert data[0]["email"] == unique_email


def test_get_user(client, app):
    with app.app_context():
        unique_email = f"{uuid.uuid4()}@example.com"
        response = client.post(
            "/users", json={"name": "John Doe", "email": unique_email}
        )
        user_id = json.loads(response.data)["id"]

        response = client.get(f"/users/{user_id}")
        data = json.loads(response.data)

        assert response.status_code == 200
        assert data["name"] == "John Doe"
        assert data["email"] == unique_email


def test_get_user_not_found(client, app):
    with app.app_context():
        response = client.get("/users/999")
        assert response.status_code == 404


def test_update_user(client, app):
    with app.app_context():
        unique_email = f"{uuid.uuid4()}@example.com"
        response = client.post(
            "/users", json={"name": "John Doe", "email": unique_email}
        )
        user_id = json.loads(response.data)["id"]

        response = client.put(
            f"/users/{user_id}",
            json={"name": "Jane Doe", "email": f"{uuid.uuid4()}@example.com"},
        )
        data = json.loads(response.data)

        assert response.status_code == 200
        assert data["name"] == "Jane Doe"


def test_update_user_not_found(client, app):
    with app.app_context():
        response = client.put(
            "/users/999", json={"name": "Jane Doe", "email": "jane@example.com"}
        )
        assert response.status_code == 404


def test_delete_user(client, app):
    with app.app_context():
        unique_email = f"{uuid.uuid4()}@example.com"
        response = client.post(
            "/users", json={"name": "John Doe", "email": unique_email}
        )
        user_id = json.loads(response.data)["id"]

        response = client.delete(f"/users/{user_id}")
        data = json.loads(response.data)

        assert response.status_code == 200
        assert data["message"] == "User deleted successfully"

        response = client.get(f"/users/{user_id}")
        assert response.status_code == 404


def test_delete_user_not_found(client, app):
    with app.app_context():
        response = client.delete("/users/999")
        assert response.status_code == 404
