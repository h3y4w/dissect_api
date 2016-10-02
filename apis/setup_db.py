from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://localhost/dissect'
db=SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    stage = db.Column(db.Integer)
    def __init__(self):
        self.start = datetime.utcnow()
        self.stage = 0

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(120))
    role = db.Column(db.String(10))
    def __init__(self, user_info):
        self.first_name = user_info['first_name']
        self.last_name = user_info['last_name']
        self.email = user_info['email']
        self.password = user_info['password'] #hash password here or b4
        self.role='regular'

db.create_all()
db.session.commit()