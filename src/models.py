import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_from_id = Column(String(250), nullable=False)
    user_to_id = Column(String(250), nullable=False)
    favorites = relationship("Favorites", back_populates="user")

class Character (Base):
    __tablename__ = 'Character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250), nullable=False)
   
class Spaceship (Base):
    __tablename__ = 'Spaceship'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    make = Column(String(250))
    model = Column(String(250))

class Favorites (Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    list_of_favorites = Column(String(250))
    user = relationship("User", back_populates="favorites")
    character = relationship("Character")
    starship = relationship("Spaceship")
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    starship_id = Column(Integer, ForeignKey('starship.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
