from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .base import Base


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True)
    albumid = Column(Integer, ForeignKey("albums.id"))
    album = relationship("Album", back_populates="photos")
    title = Column(String(128))
    url = Column(String(256))
    thumbnailUrl = Column(String(256))

    # posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)
