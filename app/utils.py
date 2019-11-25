import json
from logging import info, warning
from functools import wraps
from uuid import UUID, uuid4

from flask import request, Response, g
from werkzeug.exceptions import Forbidden


AUTH_TOKEN = "X-Auth-Token"


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        headers = request.headers
        if AUTH_TOKEN in headers.keys() and validate_uuid(headers[AUTH_TOKEN]):
            info(f"Auth OK with token: {headers[AUTH_TOKEN]}")
            return func(*args, **kwargs)
        warning(f"No or wrong token")
        raise Forbidden
    return wrapper


def get_auth_token() -> str:
    return request.headers[AUTH_TOKEN].lower()


def validate_uuid(uuid: str) -> bool:
    try:
        uuid_obj = UUID(uuid)
    except ValueError:
        return False
    return str(uuid_obj) == uuid.lower()


def error_message(status: int, message: str):
    return Response(json.dumps({
        "status": status,
        "result": message
    }), status=status,
        content_type="application/json")


def response_message(message, status=200):
    return Response(
        json.dumps(message),
        status=status,
        content_type="application/json",
    )


def request_id():
    if getattr(g, 'request_id', None):
        return g.request_id

    g.request_id = uuid4()
    return g.request_id


def client_ip():
    return request.remote_addr
