import psycopg
import logging

CONNECT_URL = "dbname=library_db user=librarian"

def get_borrowed_book(book_id):
    with psycopg.connect(CONNECT_URL) as conn:
        with conn.cursor() as cur:
            cur.execute('select user_id from borrowed_books where book_id=%s', (book_id))
            record = cur.fetchone()
            return record[0]



def borrow_book(user_id,book_id):
    found_user = get_borrowed_book(book_id)

    if found_user is not None:
        logging.info("Book %s is on loan", book_id)
        raise Exception("Book is already on loan")

    with psycopg.connect(CONNECT_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("insert into borrowed_books(user_id, book_id) values (%s,%s)", (user_id, book_id))
