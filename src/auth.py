from flask import (
    Blueprint, 
    request, 
    json
)
from werkzeug.security import (
    check_password_hash, 
    generate_password_hash
)
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)
from db import get_db, create_id
from blocklist import blocklist
import validators

auth = Blueprint("auth", __name__, url_prefix = "/api/v1/auth")

@auth.post('/register')
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    cur = get_db().cursor()
    cur.execute(f'select * from users where email = "{email}"')
    ret = cur.fetchone()
     
    if ret:
        return {'error': 'Duplicated email'}

    if not validators.email(email):
        return {'error': 'Email is not valid'}

    hashed_password = generate_password_hash(password)
    user_id = create_id('users')

    cur.execute(f'\
        insert into users values ( \
            {user_id},\
            "{username}",\
            "{email}", \
            "{hashed_password}", \
            "reader" \
    )')
    cur.close()
    get_db().commit()

    refresh_token = create_access_token(identity=email)
    access_token  = create_access_token(identity=email)

    return {'data': {
            'username': username,
            'email': email,
            'role': 'reader',
            'refresh': refresh_token,
            'access': access_token
    }}

@auth.post('/login')
def login():
    email = request.json['email']
    password = request.json['password']

    cur = get_db().cursor()
    cur.execute(f'select password, username, role \
        from users where email = "{email}"'
    )
    ret = cur.fetchone()
    cur.close()

    if not ret:
        return {'error': 'Incorrect email'}
    
    if not check_password_hash(ret['password'], password):
        return {'error': 'Incorrect password'}

    access_token = create_access_token(identity=email)
    refresh_token  = create_refresh_token(identity=email)

    return {'data': {
            'username': ret['username'],
            'email': email,
            'role': ret['role'],
            'access': access_token,
            'refresh': refresh_token
    }}

@auth.get('/logout')
@jwt_required(refresh=True)
def logout():
    refresh_jti = get_jwt()['jti']
    blocklist.add(refresh_jti, 'refresh')
    return {'msg': 'Clear refresh token successfully'}

@auth.get('/logout2')
@jwt_required()
def logout2():
    refresh_jti = get_jwt()['jti']
    blocklist.add(refresh_jti, 'refresh')
    return {'msg': 'Clear access token successfully'}

@auth.get('/refresh')
@jwt_required(refresh=True)
def refresh():
    new_access_token = create_access_token(get_jwt_identity())
    return {'access': new_access_token}
