from logging import error

from app.storage.backends import s3

_storage_backends = {
    "s3": s3.S3Storage,
    "null": None
}


def new_storage(backend):
    if backend in _storage_backends.keys():
        storage = _storage_backends[backend]
        return storage()

    error(f"Wrong storage backend: {backend}")
    return None
