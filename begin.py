# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker

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

restaurace1 = Restaurant(name='viva')
session.add(restaurace1)
restaurace2 = Restaurant(name='sono')
session.add(restaurace2)
session.commit()
