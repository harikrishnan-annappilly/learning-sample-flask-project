import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
app.secret_key = 'key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.user.view import user_blueprint

@app.before_first_request
def create_all():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(user_blueprint, url_prefix='/user')
