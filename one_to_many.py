# -*- coding: utf-8 -*-

# http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html

import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker


def delete_database():
    try:
        os.remove('/home/smonty/Documents/ucim_se_sqlalchemy/databaze.db')
    except Exception as ex:
        print 'neco se podelalo, chyba = ', ex
delete_database()

Base = declarative_base()
engine = create_engine('sqlite:///databaze.db')


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="children")


Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)
session = session_factory()
session = scoped_session(session_factory)


def insert_data():
    p1 = Parent(name='rodic 1')
    ch1 = Child(name='potomek 1, rodic 1', parent=p1)
    ch2 = Child(name='potomek 2, rodic 1', parent=p1)
    ch3 = Child(name='potomek 3, rodic 1', parent=p1)

    p2 = Parent(name='rodic 2')
    ch4 = Child(name='potomek 4, rodic 2', parent=p2)
    ch5 = Child(name='potomek 5, rodic 2', parent=p2)
    ch6 = Child(name='potomek 6, rodic 2', parent=p2)

    session.add(p1)
    session.add(p2)

    session.add(ch1)
    session.add(ch2)
    session.add(ch3)
    session.add(ch4)
    session.add(ch5)
    session.add(ch6)

    session.commit()


def rodic_co_ma_potomky():
    query = session.query(Parent).filter_by(name='rodic 2')
    for x in query:
        print x.name
        for y in x.children:
            print y.name


def potomek_ma_rodice():
    query = session.query(Child).filter_by(name='potomek 2, rodic 1')
    for x in query:
        print x.name
        print x.parent.name


insert_data()
# rodic_co_ma_potomky()
potomek_ma_rodice()
