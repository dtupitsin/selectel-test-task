import pytest

from app.utils import validate_uuid


@pytest.mark.parametrize("test_uuid", [
    "36af623c-0c5a-4c85-ae58-d3d89bb2b795",
    "36af623c-0c5a-4c85-ae58-d3d89bb2b79b",
    "11111111-1111-1111-1111-111111111111",
    '38033FA1-FC3B-44D7-888C-FC95CB990C62',
])
def test_validate_uuid(test_uuid):
    assert validate_uuid(test_uuid)


@pytest.mark.parametrize("test_uuid", [
    "36af623c-0c5a-4c85-ae58",
    "X-Auth-Token",
    "36af623c-0qwe-4c85-ae58-d3d89bb2b79b",
])
def test_wrong_validate_uuid(test_uuid):
    assert not validate_uuid(test_uuid)

