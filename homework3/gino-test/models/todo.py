
from .base import db


class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # user = db.relationship("User", back_populates="todos")
    title = db.Column(db.Text)
    completed = db.Column(db.Boolean, nullable=False, default=False, server_default="0")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)
