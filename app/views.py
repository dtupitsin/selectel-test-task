from logging import info, error

from flask import request
from werkzeug.exceptions import HTTPException
from werkzeug.http import HTTP_STATUS_CODES

from app import app
from app.utils import error_message


@app.after_request
def after_request(response):
    info(f"{request.method} {request.path} {response.status}")
    return response


@app.errorhandler(403)
@app.errorhandler(405)
@app.errorhandler(500)
@app.errorhandler(Exception)
def error_handler(e):
    error(e)
    if isinstance(e, HTTPException):
        return error_message(e.code, HTTP_STATUS_CODES[e.code])

    return error_message(500, HTTP_STATUS_CODES[500])
