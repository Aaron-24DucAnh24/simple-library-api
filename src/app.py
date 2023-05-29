from flask import Flask, g
from auth import auth
from book import books
from borrows import borrows
from flask_jwt_extended import JWTManager
from datetime import timedelta
from blocklist import blocklist
import os

app = Flask(__name__)

app.config.from_mapping(
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY'),
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=1),
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
)

jwt = JWTManager(app)
block_list = set()

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return blocklist.check(jwt_payload['jti'])

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

app.register_blueprint(auth)
app.register_blueprint(books)
app.register_blueprint(borrows)
    