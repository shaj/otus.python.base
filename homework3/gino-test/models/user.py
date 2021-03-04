from datetime import datetime

from .base import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(32))
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(32))
    website = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # address = db.relationship("Address", back_populates="user")
    # albums = db.relationship("Album", back_populates="user")
    # posts = db.relationship("Post", back_populates="user")
    # todos = db.relationship("Todo", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)

    @classmethod
    def parse_jsonplaceholder(cls, data: dict):
        return User(), Address(), Company()


class Address(db.Model):
    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # user = db.relationship("User", back_populates="address")
    street = db.Column(db.String(32))
    suite = db.Column(db.String(32))
    city = db.Column(db.String(32))
    zipcode = db.Column(db.String(32))
    geo_lat = db.Column(db.String(32))
    geo_lng = db.Column(db.String(32))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, {self.city}, {self.street}, {self.suite})"

    def __repr__(self):
        return str(self)


class Company(db.Model):
    __tablename__ = "company"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    catchPhrase = db.Column(db.String(128))
    bs = db.Column(db.String(128))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name: {self.name})"

    def __repr__(self):
        return str(self)

