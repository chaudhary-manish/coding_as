from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

def test_app():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome To FastAPI World"}


class TestUserLogin:
    """TestUserLogin tests /users/auth"""

    def test_get_request_returns_405(self):
        """login endpoint does only expect a post request"""
        response = client.get("/users/auth")
        assert response.status_code == 405

    def test_post_request_without_body_returns_422(self):
        """body should have username, password and email"""
        response = client.post("/users/auth")
        assert response.status_code == 422

    def test_post_request_with_improper_body_returns_422(self):
        """both email and password is required"""
        response = client.post(
            "/users/auth",
            json={"username": "chaudhary94rc@gmail.com"}
        )
        assert response.status_code == 422

    def test_post_request_with_proper_body_returns_200_with_jwt_token(self):
        response = client.post(
            "/users/auth",
            json={"username": "chaudhary94rc@gmail.com", "password": "12345"}
        )
        assert response.status_code == 200
        assert len(response.json()) == 2

class TestUserLogin:
    """TestUserLogin tests /users/auth"""

    def test_read_item_bad_token(self):
        response = client.get("/posts", headers={"token": "bearer hailhydra"})
        assert response.status_code == 401
        assert response.json() == {"detail": "Could not validate credentials"}
    
    def test_post_request_with_proper_body_returns_200_with_jwt_token(self):
        response = client.post(
            "/users/auth",
            json={"username": "chaudhary94rc@gmail.com", "password": "12345"}
        )
        if response:
            response = client.get(
            "/posts", headers={"token": response.json()["token_type"] +  " " + response.json()["access_token"]}
            )
            assert response.status_code == 200
            assert response.json()["count"] == 2
       