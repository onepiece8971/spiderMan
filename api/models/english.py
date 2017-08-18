from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import fields
import time

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
    sentence = db.Column(db.Text)
    create_time = db.Column(db.Integer, default=int(time.time()))
    update_time = db.Column(db.Integer, default=int(time.time()))
    delete = db.Column(db.SMALLINT, default=0)

    fields = {
        'id': fields.Integer,
        'name': fields.String,
        'voice': fields.String,
        'images': fields.String,
        'meaning': fields.String,
        'sentence': fields.String,
    }

    def __init__(self, name, phsymbol, voice, images, meaning, sentence):
        self.name = name
        self.phsymbol = phsymbol
        self.voice = voice
        self.images = images
        self.meaning = meaning
        self.sentence = sentence

    @classmethod
    def insert_english(cls, item):
        english = cls(item['name'], item['phsymbol'], item['voice'], item['images'], item['meaning'], item['sentence'])
        one = english.query.filter_by(name=item['name']).first()
        if one:
            one.phsymbol = english.phsymbol
            one.voice = english.voice
            one.images = english.images
            one.meaning = english.meaning
            one.sentence = english.sentence
            one.update_time = int(time.time())
        else:
            db.session.add(english)
        db.session.commit()

    def __repr__(self):
        return '<English %r>' % self.name
