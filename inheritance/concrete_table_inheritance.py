# -*- coding: utf-8 -*-

'''

    tady je problem, ze kdyz pridam manazera tak se nic nesvazuje
    s predkem - tabulkou employee

'''


from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker


Base = declarative_base()
engine = create_engine('sqlite:///databaze.db')


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


class Manager(Employee):
    __tablename__ = 'manager'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    manager_data = Column(String(50))

    __mapper_args__ = {
        'concrete': True
    }


class Engineer(Employee):
    __tablename__ = 'engineer'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    engineer_info = Column(String(50))

    __mapper_args__ = {
        'concrete': True
    }

Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)
session = session_factory()
session = scoped_session(session_factory)


e = Employee(name='employee name')

m = Manager(name='manazer', manager_data='data manazera')

session.add(e)
session.add(m)

session.commit()
