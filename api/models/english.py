from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://zcl:123456@192.168.31.39/spider'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class English(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    phsymbol = db.Column(db.String(64))
    voice = db.Column(db.String(256))
    images = db.Column(db.String(256))
    meaning = db.Column(db.String(512))
    sentence = db.Column(db.Text())

    fields = {
        'id': fields.Integer,
        'name': fields.String,
        'voice': fields.String,
        'images': fields.String,
        'meaning': fields.String,
        'sentence': fields.String,
    }

    def __repr__(self):
        return '<English %r>' % self.name
