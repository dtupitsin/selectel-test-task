import logging
import os

from dotenv import load_dotenv, find_dotenv

from app.utils import request_id, client_ip

load_dotenv(find_dotenv())

logger = {
    'version': 1,
    'formatters': {'default': {
        'class': 'app.config.CustomFormatter',
        'format': '[%(asctime)s] %(levelname)s in [%(module)s:%(funcName)s]: %(client_ip)s %(request_id)s - %(message)s',
    }},
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'appLogger': {
            'handlers': ['console'],
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    }
}


bucket = os.getenv('BUCKET', None)


class CustomFormatter(logging.Formatter):
    def format(self, record):
        record.request_id = request_id()
        record.client_ip = client_ip()
        s = super(CustomFormatter, self).format(record)
        return s
