# -*- coding: utf-8 -*-

'''

nevim ale docela easy?

'''

import os
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker


def delete_database():
    try:
        os.remove('/home/smonty/Documents/ucim_se_sqlalchemy/transakce/databaze.db')
    except Exception as ex:
        print('neco se podelalo, chyba = ', ex)
# delete_database()


Base = declarative_base()
engine = create_engine('sqlite:///databaze.db')
#engine = create_engine('postgresql+psycopg2://postgres:root@localhost/smonty')


class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=True)
    dalsi_sloupec = Column(String(80), nullable=True, unique=True)


class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True)
    item_name = Column(String(50), nullable=True, unique=True)


Base.metadata.create_all(engine)
# příprava továrny
session_factory = sessionmaker(bind=engine)
# vytvoření nové session
session = session_factory()
# scoped session!
session = scoped_session(session_factory)


# kdyz jeden unique neprojde, cely to jde (logicky) dohaje...
try:
    r = Restaurant(name='asd', dalsi_sloupec='unique 2')

    mi = MenuItem(item_name='unique item 2')

    session.add(r)
    session.add(mi)

    session.commit()
    print('transakce ok')
except Exception as ex:
    session.rollback()
    print('roll back')
finally:
    session.close()

