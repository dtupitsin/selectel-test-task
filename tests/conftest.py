from uuid import uuid4

import pytest

from app import app
from app.utils import AUTH_TOKEN


@pytest.fixture(scope="session")
def user_id():
    return uuid4()


@pytest.fixture(scope="session")
def filename():
    return "test_file"


@pytest.fixture(scope="session")
def upload_file_data():
    return "just some data"


@pytest.fixture(scope="session")
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="session")
def auth_header(user_id):
    return {AUTH_TOKEN: user_id}
