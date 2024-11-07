from flask import Flask, request, make_response
import logging

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

