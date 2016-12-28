# -*- coding: utf-8 -*-

# http://alextechrants.blogspot.cz/2013/11/10-common-stumbling-blocks-for.html

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


class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=True)


class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True)
    item_name = Column(String(50), nullable=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    restaurant = relationship(Restaurant)

Base.metadata.create_all(engine)
# příprava továrny
session_factory = sessionmaker(bind=engine)
# vytvoření nové session
session = session_factory()
# scoped session!
session = scoped_session(session_factory)


def insert_data():
    restaurace1 = Restaurant(name='viva')
    session.add(restaurace1)

    jidlo1 = MenuItem(item_name='pizza', restaurant=restaurace1)
    session.add(jidlo1)
    jidlo2 = MenuItem(item_name='hambac', restaurant=restaurace1)
    session.add(jidlo2)

    restaurace2 = Restaurant(name='sono')
    session.add(restaurace2)

    jidlo3 = MenuItem(item_name='mick jagger na houbach',
                      restaurant=restaurace2)
    session.add(jidlo3)
    jidlo4 = MenuItem(item_name='nevim', restaurant=restaurace2)
    session.add(jidlo4)

    session.commit()


def fetch_data_restaurace():
    for x in session.query(Restaurant).all():
        print 'id = {0}, name = {1}'.format(x.id, x.name)


def fetch_data_menu_items():
    for x in session.query(MenuItem).all():
        print 'id = {0}, name = {1}'.format(x.id, x.item_name)
        if x.restaurant:
            print 'restaurace, name = {0}'.format(x.restaurant.name)


def update_restaurant():
    r2 = session.query(Restaurant).all()
    for x in r2:
        print x.name

    r1 = session.query(Restaurant).filter_by(name='viva').one()
    r1.name = 'Viva'
    r2 = session.query(Restaurant).filter_by(name='sono').one()
    r2.name = 'Sono'

    session.add(r1)
    session.add(r2)
    session.commit()

    r2 = session.query(Restaurant).all()
    for x in r2:
        print x.name


def delete_restaurant():
    query = session.query(Restaurant).filter_by(name='viva').all()
    for x in query:
        print 'co najdu mazu = ', x.name
        session.delete(x)

    query = session.query(Restaurant).all()
    for x in query:
        print 'co jsem nasel po mazani = ', x.name

insert_data()
# fetch_data_restaurace()
# fetch_data_menu_items()

# update_restaurant()
delete_restaurant()