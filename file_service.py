import psycopg
import logging
from typing import List
from marshmallow import Schema, fields
import os

logger = logging.getLogger(__name__)

# CONNECT_URL = "psycopgdbname=library_db user=librarian passwd=letmein"
CONNECT_URL = os.environ.get("DATABASE_URL", "postgresql://librarian:letmein@localhost:5432/library_db")


class FileMeta:
    def __init__(self, file_id, file_name, content):
        self.file_id = file_id
        self.file_name = file_name
        self.content = content

    def file_id( self ):
        return self.file_id

class FileColl:

    def __init__(self, files):
        self._files = files
    
    @property
    def files( self ):
        return self._files
    
    @files.setter
    def files(self, new_files):
        self._files = new_files


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

    with connectDB() as conn:
        with conn.cursor() as cur:
            for rec in file_metadata["files"]:
                logger.info(f'${rec["name"]}, ${rec["content"]}')
                cur.execute('insert into files (file_name,content) values (%s, %s) returning file_id', (rec["name"], rec["content"]))
                new_id = cur.fetchone()[0]
                print(f'New id is {new_id}')
                item = FileMeta(file_id=new_id,file_name=rec["name"], content=rec["content"])

                items.append(item)
        saved = FileColl(files=items)

    return saved

def connectDB():
    return psycopg.connect(CONNECT_URL)