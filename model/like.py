from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from .base import Base


class Like(Base):
    id = Column(Integer, primary_key=True, index=True)
    is_liked = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey=True, index=True)
    owner = relationship("User", back_populates="likes")
    video_id = Column(Integer, ForeignKey=True, index=True)
    video = relationship("Video", back_populates="likes")