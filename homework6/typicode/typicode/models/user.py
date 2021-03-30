from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(32))
    username = db.Column(db.String(32), unique=True)
    phone = db.Column(db.String(32))
    email = db.Column(db.String(32))
    website = db.Column(db.String(128))

    street = db.Column(db.String(32))
    suite = db.Column(db.String(32))
    city = db.Column(db.String(32))
    zipcode = db.Column(db.String(32))
    geo_lat = db.Column(db.String(32))
    geo_lng = db.Column(db.String(32))

    company_name = db.Column(db.String(32))
    company_catchPhrase = db.Column(db.String(128))
    company_bs = db.Column(db.String(128))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)

    def update_jsonplaceholder(self, data: dict):
        try:
            self.id = int(data["id"])
        except Exception:
            pass
        self.fullname = data["name"]
        self.username = data["username"]
        self.email = data["email"]
        self.street = data["address"]["street"]
        self.suite = data["address"]["suite"]
        self.city = data["address"]["city"]
        self.zipcode = data["address"]["zipcode"]
        self.geo_lat = data["address"]["geo"]["lat"]
        self.geo_lng = data["address"]["geo"]["lng"]
        self.phone = data["phone"]
        self.website = data["website"]
        self.company_name = data["company"]["name"]
        self.company_catchPhrase = data["company"]["catchPhrase"]
        self.company_bs = data["company"]["bs"]



