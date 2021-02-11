from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    fullname = Column(String(32))
    username = Column(String(32), unique=True)
    email = Column(String(32))
    website = Column(String(128))
    created_at = Column(DateTime, default=datetime.utcnow)

    address = relationship("Address", back_populates="user")
    albums = relationship("Album", back_populates="user")
    posts = relationship("Post", back_populates="user")
    todos = relationship("Todo", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)

    @classmethod
    def parse_jsonplaceholder(cls, data: dict):
        return User(), Address(), Company()


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="address")
    street = Column(String(32))
    suite = Column(String(32))
    city = Column(String(32))
    zipcode = Column(String(32))
    geo_lat = Column(String(32))
    geo_lng = Column(String(32))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, {self.city}, {self.street}, {self.suite})"

    def __repr__(self):
        return str(self)


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    catchPhrase = Column(String(128))
    bs = Column(String(128))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name: {self.name})"

    def __repr__(self):
        return str(self)

