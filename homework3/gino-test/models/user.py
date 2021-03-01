from datetime import datetime
# from sqlalchemy import (
#     Column,
#     Integer,
#     String,
#     Boolean,
#     DateTime,
# )
# from sqlalchemy.orm import relationship

# from .base import Base

from .base import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    is_staff = db.Column(db.Boolean, nullable=False, default=False, server_default="0")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_class = db.Column(db.String(64), default="~", server_default="~")

    # posts = db.relationship("Post", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, cnt={self.user_class})"

    def __repr__(self):
        return str(self)
