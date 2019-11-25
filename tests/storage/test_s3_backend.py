import pytest

from app.storage import new_storage
from app.storage.backends import Storage


@pytest.fixture(scope="module")
def storage():
    return new_storage("s3")


def test_create_new_storage(storage):
    assert storage is not None
    assert isinstance(storage, Storage)


def test_upload(storage, user_id, filename, upload_file_data):
    result, code = storage.upload(user_id, filename, upload_file_data)
    assert result


def test_list(storage, user_id):
    result = storage.list(user_id)
    assert isinstance(result, list)
    assert len(result) > 0


def test_delete(storage, user_id, filename):
    files_cnt = len(storage.list(user_id))

    result, code = storage.delete(user_id, filename)
    assert result
    files_current = storage.list(user_id)
    assert isinstance(files_current, list)
    assert files_cnt - len(files_current) == 1

