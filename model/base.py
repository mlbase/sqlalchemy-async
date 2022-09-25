import re
from typing import Any
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    @declared_attr
    def __tablename__(self) -> str:
         return re.sub(r'(?<!^)(?=[A-Z])', '_', self.__name__).lower()