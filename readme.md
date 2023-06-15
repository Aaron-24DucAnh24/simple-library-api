# Simple Flask API for library management

### Using my docker image
```bash
docker-compose up
```

### Setup using Virtualenv

1. Make sure you got
- Python3
- Pip3

2. Install and setup virtualenv
```bash
sudo pip3 install virtualenv
python3 -m venv venv
```
3. Activate virtual env
```bash
source venv/bin/activate
```

4. Install dependencies
```bash
python3 -m pip install -r requirements.txt
```

### Run
```bash
flask --app src/app run
```
> now, the server is running on *http://127.0.0.1:5000*
> whenever you want to exit env mode
```bash
deactivate
```

### API
1. Login
```python
method = 'POST'

url_postfix = "/api/v1/auth/login"

request = {
    'email': str,
    'password': str
}

response = {
    'data': {
            'username': str,
            'email': str,
            'role': str,
            'access': str,
            'refresh': str,
    }
}
```

2. Register
```python
method = 'POST'

url_postfix = "/api/v1/auth/register"

request = {
    'email': str,
    'password': str,
    'username': str
}

response = {
    'data': {
            'username': str,
            'email': str,
            'role': str,
            'access': str,
            'refresh': str,
    }
}
```

3. Refresh access token
```python
method = 'GET'

url_postfix = "/api/v1/auth/refresh"

response = {
    'access': str
}
```

4. Clear access token

```python
method = 'GET'

url_postfix = "/api/v1/auth/logout2"

response = {
    'msg': 'Clear access token successfully'
}
```

5. Clear refresh token

```python
method = 'GET'

url_postfix = "/api/v1/auth/logout"

response = {
    'msg': 'Clear refresh token successfully'
}
```

6. Get all books
```python
method = 'GET'

url_postfix = "/api/v1/books/"

response = {
    'data': [
        ...
        {
            'bookid': int,
            'bookname': str,
            'author': str,
            'year': int,
            'total_number': int,
            'available_number': int
        }
    ]
} 
```

7. Get available books
```python
method = 'GET'

url_postfix = "/api/v1/books/available"

response = {
    'data': [
        ...
        {
            'bookid': int,
            'bookname': str,
            'author': str,
            'year': int,
            'total_number': int,
            'available_number': int
        }
    ]
} 
```

8. Get borrowed books
```python
method = 'GET'

url_postfix = "/api/v1/books/borrowed"

response = {
    'data': [
        ...
        {
            'bookid': int,
            'bookname': str,
            'author': str,
            'year': int,
            'total_number': int,
            'available_number': int
        }
    ]
} 
```

9. Add a book
```python
method = 'POST'

url_postfix = "/api/v1/books/"

request_body = {
    'name': str,
    'author': str,
    'year': int,
    'number': int
}

response = {
    'data': {
        'bookid': int,
        'bookname': str,
        'author': str,
        'year': int,
        'borrowed_number': int
    }
}
```

10. Delete a book
```python
method = 'DELETE'

url_postfix = "/api/v1/books/<book_id>"

response = {
    'data': {
        'bookname': str,
        'author': str,
        'year': int,
    }
}
```

11. Get readers of a book
```python
method = 'GET'

url_postfix = "/api/v1/borrows/reader/<book_id>"

response = {
    'data': [
        ...
        {
            'userid': int,
            'username': str,
            'email': str,
            'role': str
        }
    ]
}
```

12. Get books of a reader
```python
method = 'GET'

url_postfix = "/api/v1/borrows/book/<user_id>"

response = {
    'data': [
        ...
        {
            'bookid': int,
            'author': str,
            'year': int
        }
    ]
}
```

13. Get my books
```python
method = 'GET'

url_postfix = "/api/v1/borrows/book/me"

response = {
    'data': [
        ...
        {
            'bookid': int,
            'author': str,
            'year': int
        }
    ]
}
```

14. Borrow a book
```python
method = 'GET'

url_postfix = "/api/v1/borrows/borrow/<book_id>"

response = {
    'data': {
        'bookid': int,
        'author': str,
        'year': int
    }
}
```

15. Give back a book
```python
method = 'GET'

url_postfix = "/api/v1/borrows/give-back/<book_id>"

response = {
    'data': {
        'bookid': int
    }
}
```

16. Give back all book
```python
method = 'GET'

url_postfix = "/api/v1/borrows/give-back-all

response = {
    'msg': 'Give back all successfully'
}
```
