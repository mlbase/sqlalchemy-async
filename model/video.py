from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class Video(Base):
    __tablename__ = "api_video"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey=True, index=True)
    title = Column(String, index=True)
    is_deleted = Column(Boolean, default=False)
    is_blinded = Column(Boolean, default=False)
    watch_count = Column(Integer)
    report_count = Column(Integer)
    like_count = Column(Integer)
    owner = relationship("User", back_populates="videos")