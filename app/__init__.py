from logging.config import dictConfig

from flask import Flask

from app.storage import new_storage
from app.config import logger

dictConfig(logger)

app = Flask(__name__)
storage = new_storage("s3")


from app import views    # noQa
from app.api import api  # noQA

app.register_blueprint(api, url_prefix="/api")
