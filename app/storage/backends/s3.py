import re
from logging import info, debug

import boto3

from app import config
from app.storage.backends import Storage


class S3Storage(Storage):
    def __init__(self):
        super().__init__()
        self.s3 = boto3.resource('s3')
        self.client = boto3.client('s3')

    def upload(self, user_id: str, filename: str, data: str) -> (bool, int):
        info(f"User({user_id}) upload file {filename}, len: {len(data)}")
        result = self.client.put_object(
            Bucket=config.bucket,
            Body=data,
            Key=f"{user_id}/{filename}",
        )
        ret_code = int(result["ResponseMetadata"]["HTTPStatusCode"])
        debug(f"ret_code: {ret_code} ")
        return ret_code == 200, ret_code

    def list(self, user_id: str) -> list:
        prefix = f"{user_id}/"
        user_bucket = self.s3.Bucket(config.bucket)
        objects = user_bucket.objects.filter(Prefix=prefix)

        result = []

        for obj in objects:
            file = re.sub(f'^{prefix}', '', obj.key)
            if len(file) > 0:
                result.append(file)

        return result

    def delete(self, user_id, filename) -> (bool, int):
        info(f"User({user_id}) delete file {filename}")
        result = self.client.delete_object(
            Bucket=config.bucket,
            Key=f"{user_id}/{filename}",
        )
        ret_code = int(result["ResponseMetadata"]["HTTPStatusCode"])
        return ret_code == 204, ret_code
