import pytest
import os
from app import create_app
from app.extensions import db


@pytest.fixture
def app():
    """
    Create and configure a new app instance for each test.
    """

    os.environ["DATABASE_URL"] = "sqlite:///:memory:"
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
    )

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """
    A test client for the app.
    """
    return app.test_client()


@pytest.fixture
def runner(app):
    """
    A test runner for the app.
    """
    return app.test_cli_runner()
