from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    hashed_password = Column(String)

    post_entries = relationship("Post", back_populates="owner")
    comments = relationship("Comments", back_populates="owner")
