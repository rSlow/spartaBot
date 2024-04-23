from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship

from orm.base import Base
from orm.models.groups import Group


class Person(Base):
    __tablename__ = 'persons'

    fio: Mapped[str]
    group_id: Mapped[int] = ForeignKey('groups.id')
    group: Mapped[Group] = relationship()
