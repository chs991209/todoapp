import os

from flask import Flask
from flask import render_template, redirect

from api_v1 import api as api_v1
from models import db

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix='/api/v1')


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def regist():
    return render_template('register.html')


basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dalskdfjlskfjlskjflaksjflk'

db.init_app(app)
db.app = app
db.create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)