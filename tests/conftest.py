import pytest
from fastapi.testclient import TestClient

from financial_mng.app import app


@pytest.fixture
def client():
    return TestClient(app)
