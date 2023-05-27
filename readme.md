# Simple Flask API for library management

### Setup

1. Make sure you got
- Python3
- Pip3

2. Run env mode
```bash
sudo pip3 install virtualenv
python3 virtual venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip3 install requirements
```

### Run
```bash
flask run
```
> now, the server is running on *http://127.0.0.1:5000*
> whenever you want to exit env mode
```bash
deactivate
```

### API
1. Get all books
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

2. Get available books
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

3. Get borrowed books
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

4. Add a book
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

5. Delete a book
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