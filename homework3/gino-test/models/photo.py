
from .base import db


class Photo(db.Model):
    __tablename__ = "photos"

    id = db.Column(db.Integer, primary_key=True)
    albumid = db.Column(db.Integer, db.ForeignKey("albums.id"))
    # album = db.relationship("Album", back_populates="photos")
    title = db.Column(db.String(128))
    url = db.Column(db.String(256))
    thumbnailUrl = db.Column(db.String(256))

    # posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)
