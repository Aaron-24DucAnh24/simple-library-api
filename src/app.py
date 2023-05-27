from flask import Flask, g
from auth import auth
from book import books
from borrows import borrows

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

app.register_blueprint(auth)
app.register_blueprint(books)
app.register_blueprint(borrows)

if __name__== '__main__':
    app.run()
