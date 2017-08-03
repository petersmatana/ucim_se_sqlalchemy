# -*- coding: utf-8 -*-

'''

    tady to hezky funguje, kdyz pridam engineera, svaze se tento zaznam
    i s tabulkou employee

    !!! http://docs.sqlalchemy.org/en/latest/orm/mapper_config.html



               poly join
    employee ------------- enginees
             ------------- manager  ---- N:1 ---- company

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
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'employee',
        'polymorphic_on': type
    }


class Engineer(Employee):
    __tablename__ = 'engineer'
    id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    engineer_name = Column(String(30))

    __mapper_args__ = {
        'polymorphic_identity': 'engineer',
    }


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    managers = relationship("Manager", back_populates="company")


class Manager(Employee):
    __tablename__ = 'manager'
    id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    manager_name = Column(String(30))

    company_id = Column(ForeignKey('company.id'))
    company = relationship("Company", back_populates="managers")

    __mapper_args__ = {
        'polymorphic_identity': 'manager',
    }


Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)
session = session_factory()
session = scoped_session(session_factory)


def insert_data():
    c = Company(name='fuuu')
    c2 = Company(name='fiii')

    m = Manager(manager_name='asd', company=c)
    m2 = Manager(manager_name='jojo', company=c2)
    m3 = Manager(manager_name='llll', company=c2)

    session.add(c)
    session.add(c2)

    session.add(m)
    session.add(m2)
    session.add(m3)

    session.commit()

insert_data()
