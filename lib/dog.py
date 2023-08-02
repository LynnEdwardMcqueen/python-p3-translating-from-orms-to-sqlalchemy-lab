from models import Dog
import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Base, Dog
from testing.conftest import db_dir, SQLITE_URL



def create_table(base, engine):
    base.metadata.create_all(engine)
    pass

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    dogs = session.query(Dog)
    return dogs


def find_by_name(session, name):
    named_dogs = session.query(Dog).filter(Dog.name == name).all()
    # We get a list of tuples.  Send back the 0th element.
    return named_dogs[0]

def find_by_id(session, id):
    id_dog = session.query(Dog).filter(Dog.id == id).all()
    return id_dog[0]

def find_by_name_and_breed(session, name, breed):
    desired_dog = session.query(Dog).filter(Dog.name == name, Dog.breed == breed)
    return desired_dog[0]

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()


