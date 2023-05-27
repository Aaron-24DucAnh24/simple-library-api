from flask import Blueprint, request, json
from db import get_db, create_id

books = Blueprint(
    "books", 
    __name__, 
    url_prefix = "/api/v1/books"
)

@books.get('/')
def get_all():
    cur = get_db().cursor()
    cur.execute('select * from books;')
    ret = cur.fetchall()
    cur.close()
    return {'data': ret}

@books.get('/available')
def get_available():
    cur = get_db().cursor()
    cur.execute('select * from books where available_number > 0;')
    ret = cur.fetchall()
    cur.close()
    return {'data': ret}

@books.get('/borrowed')
def get_borrowed():
    cur = get_db().cursor()
    cur.execute('\
        select bookid, bookname, author, year,\
        (total_number-available_number) as borrowed_number\
        from books where available_number < total_number;\
    ')
    ret = cur.fetchall()
    cur.close()
    return {'data': ret}

@books.post('/')
def add():
    name = request.json['name']
    author = request.json['author']
    year = request.json['year']
    number = request.json['number']
    
    cur = get_db().cursor()
    cur.execute(f'select * from books where bookname = "{name}";')
    ret = cur.fetchall()
    cur.close()
    if len(ret):
        return {'error': 'Duplicated book name'}

    if number < 0:
        return {'error': 'Negative number'}

    book_id = create_id('books')
    cur = get_db().cursor()
    cur.execute(f'insert into books values ( \
        {book_id}, "{name}", "{author}", {year}, {number}, {number} \
    );')
    cur.close()
    get_db().commit()

    ret = request.json
    ret['id'] = book_id
    return {'data': ret}

@books.delete('/<book_id>')
def delete(book_id):
    cur = get_db().cursor()
    cur.execute(
        f'select bookname, author, year \
        from books where bookid = {book_id};' 
    )
    ret = cur.fetchone()
    cur.execute(f'delete from books where bookid = {book_id};')
    cur.close()
    get_db().commit()

    return {'data': ret} if ret else {'error': 'Book not found'}
