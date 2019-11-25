
from flask import Blueprint, request

from app import storage
from app.utils import auth_required, get_auth_token, response_message

api = Blueprint("api", __name__)


@api.route("/files", methods=["GET"])
@auth_required
def get_objects():
    result = storage.list(get_auth_token())
    return response_message(result)


@api.route("/files/<string:filename>", methods=["PUT"])
@auth_required
def upload_object(filename):
    token = get_auth_token()
    users_data = request.data

    (success, code) = storage.upload(token, filename, users_data)
    if success:
        return response_message([], status=204)

    return response_message(
        {"message": "An error occurred while uploading the file."},
        status=code
    )


@api.route("/files/<string:filename>", methods=["DELETE"])
@auth_required
def delete_object(filename):
    token = get_auth_token()
    (success, code) = storage.delete(token, filename)
    if success:
        return response_message([], status=204)

    return response_message(
        {"message": "An error occurred while deleting the file."},
        status=code
    )
