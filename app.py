import logging
from flask import Flask, request, make_response
from opentelemetry.instrumentation.flask import FlaskInstrumentor
import logging
from typing import List
from file_service import FileCollSchema
import file_service

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)


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

