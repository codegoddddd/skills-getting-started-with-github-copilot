import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def activities_snapshot():
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(copy.deepcopy(original))
