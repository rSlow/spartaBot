from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from orm.base import Base
from orm.models.groups import Group


class Timetable(Base):
    __tablename__ = "timetables"

    datetime: Mapped[datetime]
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    group: Mapped[Group] = relationship()
