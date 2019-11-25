import pytest
from flask import Response


def test_get_object(client, auth_header):
    print(auth_header)
    response = client.get("/api/files",
                          headers=auth_header)

    assert isinstance(response, Response)
    assert response.status_code == 200
    result = response.json

    assert isinstance(result, list)


@pytest.mark.parametrize("wrong_auth_headers", [
    {"X-Auth-Token": "qwerr-auth-param"},
    {"Auth-Token": "ba474819-9df4-4127-a852-11039297b051"},
    {},
])
def test_get_object_forbidden(client, wrong_auth_headers):
    response: Response = client.get("/api/files",
                                    headers=wrong_auth_headers)

    assert isinstance(response, Response)
    assert response.status_code == 403


def test_upload_object(client, auth_header, filename, upload_file_data):
    response: Response = client.put(f"/api/files/{filename}",
                                    headers=auth_header,
                                    data=upload_file_data)

    assert isinstance(response, Response)
    print(response.status)
    assert 200 <= response.status_code < 300

    response = client.get("/api/files",
                          headers=auth_header)
    files = response.json
    assert filename in files


def test_delete_object(client, auth_header, filename):
    response = client.get("/api/files",
                          headers=auth_header)
    files = response.json
    assert filename in files

    response = client.delete(f"/api/files/{filename}",
                             headers=auth_header)

    assert isinstance(response, Response)
    assert 200 <= response.status_code < 300

    response = client.get("/api/files",
                          headers=auth_header)
    files = response.json
    assert filename not in files
