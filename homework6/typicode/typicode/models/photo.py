from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .database import db



class Photo(db.Model):
    __tablename__ = "photos"

    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.id"))
    title = db.Column(db.String(128))
    url = db.Column(db.String(256))
    thumbnailUrl = db.Column(db.String(256))

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
            self.album_id = int(data["albumId"])
        except Exception:
            pass
        self.title = data["title"]
        self.url = data["url"]
        self.thumbnailUrl = data["thumbnailUrl"]
