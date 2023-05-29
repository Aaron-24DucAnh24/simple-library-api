from flask import Blueprint
from db import get_db
from flask_jwt_extended import jwt_required, get_jwt_identity

borrows = Blueprint('borrows', __name__, url_prefix="/api/v1/borrows")

@borrows.get('/reader/<book_id>')
@jwt_required()
def get_readers_of_book(book_id):
    cur = get_db().cursor()

    cur.execute(f'select * from books where bookid = {book_id};')
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
@jwt_required()
def get_books_if_me():
    cur = get_db().cursor()

    cur.execute(f'\
        select userid from users\
        where email = "{get_jwt_identity()}";\
    ')
    ret = cur.fetchone()
    user_id = ret['userid']

    cur.execute(f'\
        select bookid, author, year\
        from borrows natural join books\
        where userid = {user_id}; \
    ')

    ret = cur.fetchall()
    cur.close()

    return {'data': ret}

@borrows.get('/book/<user_id>')
@jwt_required()
def get_books_of_reader(user_id):
    cur = get_db().cursor()

    cur.execute(f'select * from users where userid = {user_id};')
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
@jwt_required()
def get_borrow(book_id):
    cur = get_db().cursor()
    cur.execute(f'\
        select userid from users\
        where email = "{get_jwt_identity()}";\
    ')
    user_id = cur.fetchone()['userid']

    cur.execute(f'\
        select bookid, bookname, author, year from books\
        where bookid = "{book_id}";\
    ')
    ret = cur.fetchone()

    if not ret:
        return {'error': 'Book not found'}

    cur.execute(f'\
        insert into borrows \
        values("{book_id}", "{user_id}");\
    ')
    
    get_db().commit()
    cur.close()

    return {'data': ret}

@borrows.get('/give-back/<book_id>')
@jwt_required()
def give_back(book_id):    
    cur = get_db().cursor()

    cur.execute(f'\
        select userid from users\
        where email = "{get_jwt_identity()}";\
    ')
    user_id = cur.fetchone()['userid']

    cur.execute(f'\
        delete from borrows where \
        bookid = {book_id} and userid = {user_id}; \
    ')
    get_db().commit()
    cur.close()

    return {'data': {'bookid': book_id}}

@borrows.get('/give-back-all')
@jwt_required()
def give_back_all():
    cur = get_db().cursor()

    cur.execute(f'\
        select userid from users\
        where email = "{get_jwt_identity()}";\
    ')
    user_id = cur.fetchone()['userid']

    cur.execute(f'\
        delete from borrows where \
        userid = {user_id}; \
    ')
    get_db().commit()
    cur.close()

    return {'msg': 'Give back all successfully'}
