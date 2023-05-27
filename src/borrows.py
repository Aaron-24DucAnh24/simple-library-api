from flask import Blueprint
from db import get_db

borrows = Blueprint('borrows', __name__, url_prefix="/api/v1/borrows")

@borrows.get('/reader/<book_id>')
def get_readers_of_book(book_id):
    cur = get_db().cursor()

    cur.execute(f'select * from books where bookid = {book_id}')
    ret = cur.fetchone()
    if not ret: 
        return {'error': 'Not found book'}

    cur.execute(
        f'select userid, username, email, role\
        from borrows natural join users \
        where bookid = {book_id};'
    )

    ret = cur.fetchall()
    cur.close()

    return {'data': ret}

@borrows.get('/book/me')
def get_books_if_me():
    # todo
    return '1'

@borrows.get('/book/<user_id>')
def get_books_of_reader(user_id):
    cur = get_db().cursor()

    cur.execute(f'select * from users where userid = {user_id}')
    ret = cur.fetchone()
    if not ret: 
        return {'error': 'Not found user'}

    cur.execute(
        f'select bookid, author, year\
        from borrows natural join books \
        where userid = {user_id};'
    )

    ret = cur.fetchall()
    cur.close()
    
    return {'data': ret}

@borrows.get('/borrow/<book_id>')
def get_borrow(book_id):
    # todo
    return 1 

@borrows.get('/give-back/<book_id>')
def give_back(book_id):
    # todo
    return 1 

@borrows.get('/give-back-all')
def give_back_all():
    # todo
    return 1 
