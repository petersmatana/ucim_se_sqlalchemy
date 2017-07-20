# -*- coding: utf-8 -*-

# http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html

import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.schema import Table


def delete_database():
    try:
        os.remove('/home/smonty/Documents/ucim_se_sqlalchemy/databaze.db')
    except Exception as ex:
        print 'neco se podelalo, chyba = ', ex
delete_database()

Base = declarative_base()
engine = create_engine('sqlite:///databaze.db')

association_table = Table('association', Base.metadata,
    Column('child_id', Integer, ForeignKey('child.id')),
    Column('parent_id', Integer, ForeignKey('parent.id'))
)


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    child = relationship('Child',
                        secondary=association_table,
                        back_populates='parent')


class Child(Base):
    __tablename__ = 'child'
    name = Column(String(80))
    id = Column(Integer, primary_key=True)
    parent = relationship('Parent',
                          secondary=association_table,
                          back_populates='child')

Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)
session = session_factory()
session = scoped_session(session_factory)


def insert_data():
    p1 = Parent(name='p1')
    ch1 = Child(name='ch1')

    p1.child.append(ch1)

    session.add(p1)
    session.add(ch1)

    session.commit()


def insert_data2():
    p2 = Parent(name='p2')
    ch2 = Child(name='ch2')

    ch2.parent.append(p2)

    session.add(p2)
    session.add(ch2)

    session.commit()


def get_data():
    data = session.query(Parent).filter_by(name='p1').all()
    for x in data:
        print x.name

insert_data()
insert_data2()
get_data()
