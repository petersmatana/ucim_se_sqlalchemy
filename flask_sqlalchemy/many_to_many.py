# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


'''
tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
)


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('pages', lazy='dynamic'))


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
'''


user_group = db.Table('user_group',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('usergroup_id', db.Integer, db.ForeignKey('usergroup.id'))
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    skupiny = db.relationship('Usergroup', secondary=user_group,
                              backref='user')


class Usergroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


def db_populate():
    u1 = User(name='smonty')
    u2 = User(name='filip')

    ug1 = Usergroup(name='admin')
    ug2 = Usergroup(name='obyc-user')
    ug3 = Usergroup(name='root')

    u1.skupiny.append(ug1)
    u2.skupiny.append(ug2)

    db.session.add(u1)
    db.session.add(u2)
    db.session.add(ug1)
    db.session.add(ug2)
    db.session.add(ug3)

    db.session.commit()

db.create_all()
db_populate()
