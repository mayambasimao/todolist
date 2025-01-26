import pytest
from fastapi.testclient import TestClient

from todolist.main import app


@pytest.fixture
def client():
    return TestClient(app)
