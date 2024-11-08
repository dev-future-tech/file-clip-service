import psycopg
import logging
from typing import List
from marshmallow import Schema, fields

logger = logging.getLogger(__name__)

class FileMeta:
    def __init__(self, file_id, file_name, content):
        self.file_id = file_id
        self.file_name = file_name
        self.content = content

class FileColl:
    def __init__(self, files):
        self.files = files


class FileMetaSchema(Schema):
    name= fields.String()
    content= fields.String()

class FileCollSchema(Schema):
    files= fields.List(
        fields.Nested(FileMetaSchema),
        required=False,
    )

def saveFiles(file_metadata: FileColl):
    items = []
    for rec in file_metadata["files"]:
        logger.info(f'${rec["name"]}, ${rec["content"]}')
        item = FileMeta(file_id=1,file_name=rec["name"], content=rec["content"])
        items.append(item)
    saved = FileColl(files=items)
    return saved

