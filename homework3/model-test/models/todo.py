from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .base import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="todos")
    title = Column(Text)
    completed = Column(Boolean, nullable=False, default=False, server_default="0")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)
