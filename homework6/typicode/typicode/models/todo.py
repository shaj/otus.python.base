from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .database import db



class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.Text)
    completed = db.Column(db.Boolean, nullable=False, default=False, server_default="0")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)

    def update_jsonplaceholder(self, data: dict):
        try:
            self.id = int(data["id"])
        except Exception:
            pass
        try:
            self.user_id = int(data["userId"])
        except Exception:
            pass
        self.title = data["title"]
        self.completed = data["completed"]
