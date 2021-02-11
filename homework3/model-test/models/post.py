from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .base import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")
    title = Column(String(256), nullable=False)
    body = Column(Text)

    comments = relationship("Comment", back_populates="post")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title})"

    def __repr__(self):
        return str(self)
