from flask import Flask, request, make_response
import logging
from typing import List
from file_service import FileCollSchema
import file_service
import json

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/borrow", methods=["GET", "POST"])
def borrow_book():
    bookId = request.args.get('book_id', default=None, type=str)
    userId = request.args.get('user_id', default=None, type=str)

    logger.info(f"User {userId}, wants to borrow book {bookId}")

    response = make_response()
    response.status_code = 200

    return response

@app.route("/api/file", methods=["POST"])
def save_file():
    schema = FileCollSchema()
    file_json = schema.load(request.get_json())

    print(file_json)

    file_metadata: FileColl = json.loads(request.get_json())

    logging.info(file_metadata)

    file_service.saveFiles(file_metadata=file_metadata)

    response = make_response()

    return response

