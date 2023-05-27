from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix = "/api/v1/auth")

@auth.post('/login')
def login():
    # todo
    return 1

@auth.post('/register')
def register():
    # todo
    return 1

@auth.get('/logout')
def logout():
    # todo
    return 1
