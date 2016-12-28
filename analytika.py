# -*- coding: utf-8 -*-

import os
from sqlalchemy import Column, Integer, String, Float, func
from sqlalchemy.ext.declarative import declarative_base
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


class Analysis(Base):
    __tablename__ = 'analysis'
    id = Column(Integer, primary_key=True)
    kategorie = Column(String(80), nullable=True)
    cena = Column(Float, nullable=True)


def insert_data():
    session.add(Analysis(kategorie='heft', cena='13.10'))
    session.add(Analysis(kategorie='heft', cena='7.10'))
    session.add(Analysis(kategorie='blbost', cena='15.50'))
    session.add(Analysis(kategorie='to_chces', cena='1.11'))
    session.add(Analysis(kategorie='blbost', cena='8.16'))
    session.add(Analysis(kategorie='to_chces', cena='3.90'))
    session.add(Analysis(kategorie='to_chces', cena='4.20'))
    session.add(Analysis(kategorie='blbost', cena='8.89'))
    session.commit()


def agregace():
    agg = session.query(Analysis, func.avg(Analysis.cena)).\
                        group_by(Analysis.kategorie).all()
    for x in agg:
        print '{0} = {1} kc'.format(x[0].kategorie, x[1])


def agregace_having():
    agg = session.query(Analysis, func.avg(Analysis.cena)).\
                        group_by(Analysis.kategorie).\
                        having(func.count(Analysis.cena) >= 3)
    for x in agg:
        print '{0} = {1} kc'.format(x[0].kategorie, x[1])


def agregace3():
    agg = session.query(func.avg(Analysis.cena)).\
        group_by(Analysis.kategorie).\
        having
    for x in agg:
        print '{0} = {1} kc'.format(x[0].kategorie, x[1])


Base.metadata.create_all(engine)
# příprava továrny
session_factory = sessionmaker(bind=engine)
# vytvoření nové session
session = session_factory()
# scoped session!
session = scoped_session(session_factory)

insert_data()
agregace3()
