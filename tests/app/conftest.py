import pytest


@pytest.fixture(scope="module")
def filename():
    return "app-testfile.txt"
