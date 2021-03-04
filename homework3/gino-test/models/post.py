
from .base import db


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # user = db.relationship("User", back_populates="posts")
    title = db.Column(db.String(256), nullable=False)
    body = db.Column(db.Text)

    # comments = db.relationship("Comment", back_populates="post")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title})"

    def __repr__(self):
        return str(self)
