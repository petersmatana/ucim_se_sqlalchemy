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
# delete_database()

Base = declarative_base()
engine = create_engine('sqlite:///databaze.db')


class JednaTabulka(Base):
    __tablename__ = 'jedna_tabulka'
    id = Column(Integer, primary_key=True)
    label = Column(String(50))
    child_id = Column(Integer, ForeignKey('druha_tabulka.id'))
    child = relationship("DruhaTabulka", back_populates="parent")


class DruhaTabulka(Base):
    __tablename__ = 'druha_tabulka'
    id = Column(Integer, primary_key=True)
    label = Column(String(50))
    # http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-one
    parent = relationship("JednaTabulka", back_populates="child", uselist=False)

Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)
session = session_factory()
session = scoped_session(session_factory)


def insert_data():
    dt = DruhaTabulka(label='druha tabulka 1')
    dt2 = DruhaTabulka(label='druha tabulka 2')

    jt = JednaTabulka(label='houby', child=dt)
    jt2 = JednaTabulka(label='houby 2', child=dt2)

    session.add(dt)
    session.add(dt2)

    session.add(jt)
    session.add(jt2)

    session.commit()


def get_data():
    # data = JednaTabulka.query.filter_by(label='houby').first()
    data = session.query(JednaTabulka).filter_by(label='houby').first()
    print data.label
    print data.child.label


# insert_data()
get_data()
