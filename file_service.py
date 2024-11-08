import psycopg
import logging
from typing import List
from marshmallow import Schema, fields

logger = logging.getLogger(__name__)

class FileMeta:
    file_id: str
    file_name: str
    content: str

class FileColl:
    files: List[FileMeta]

class FileMetaSchema(Schema):
    name= fields.String()
    content= fields.String()

class FileCollSchema(Schema):
    files= fields.List(
        fields.Nested(FileMetaSchema),
        required=False,
    )

def saveFiles(file_metadata: FileColl):
    for rec in file_metadata["files"]:
        logger.info(f'${rec["name"]}, ${rec["content"]}')
    return
