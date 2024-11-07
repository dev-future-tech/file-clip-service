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
    file_id= fields.Str(dump_only=True)
    file_name= fields.Str(dump_only=True)
    content= fields.Str(dump_only=True)

class FileCollSchema(Schema):
    files= fields.List(
        fields.Nested(FileMetaSchema),
        required=False,
    )



def saveFiles(file_metadata: FileColl):
    for rec in file_metadata.files:
        logger.info(rec.file_name)
    return
