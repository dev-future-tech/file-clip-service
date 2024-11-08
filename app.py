from flask import Flask, request, make_response
import logging
from typing import List
from file_service import FileCollSchema
import file_service
import json

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/api/file", methods=["POST"])
def save_file():
    schema = FileCollSchema()

    file_metadata = schema.load(request.get_json())

    logging.info(file_metadata['files'])

    file_service.saveFiles(file_metadata=file_metadata)

    response = make_response()

    return response

