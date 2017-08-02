# -*- coding: utf-8 -*-

'''

    tady to hezky funguje, kdyz pridam engineera, svaze se tento zaznam
    i s tabulkou employee

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


# neco z tohoto: http://docs.sqlalchemy.org/en/latest/orm/mapper_config.html
# fuuuuu!!.... :(

# http://docs.sqlalchemy.org/en/latest/orm/inheritance.html

class Manager(Employee):
    __tablename__ = 'manager'
    id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    manager_name = Column(String(30))

    # newtable_id = relationship("NewTable", back_populates="parent")

    __mapper_args__ = {
        'polymorphic_identity': 'manager',
    }


'''
class NewTable(Base):
    __tablename__ = 'new_table'
    label = Column(String(50))

    parent_id = Column(Integer, ForeignKey('manager.id'))
    parent = relationship("Manager", back_populates="child")
'''


Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)
session = session_factory()
session = scoped_session(session_factory)


def insert_data():
    e = Engineer(name='smonty', engineer_name='eng name')
    m = Manager(name='adam', manager_name='man name')

    session.add(e)
    session.add(m)

    session.commit()

insert_data()


def select_data():
    data = session.query(Engineer).filter_by(engineer_name='eng name').first()
    print 'jmeno inzenyra = ', data.engineer_name


select_data()


def delete_data():
    data = session.query(Engineer).filter_by(engineer_name='eng name').first()

    session.delete(data)

    session.commit()

delete_data()
