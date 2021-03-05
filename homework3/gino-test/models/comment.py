
from .base import db


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), nullable=False)
    body = db.Column(db.Text)

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
            self.post_id = int(data["postId"])
        except Exception:
            pass
        self.name = data["name"]
        self.email = data["email"]
        self.body = data["body"]
