from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .base import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    postId = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="comments")
    name = Column(String(32), nullable=False)
    email = Column(String(32), nullable=False)
    body = Column(Text)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)
