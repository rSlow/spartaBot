from abc import ABC

from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr
from sqlalchemy import ForeignKey

from .competition import Competition
from .groups import Group
from .persons import Person
from ..base import Base


class CompetitionResult:
    competition_id: Mapped[int] = ForeignKey("competitions.id")

    @declared_attr
    def competition(self) -> Mapped[Competition]:
        return relationship()

    result: Mapped[float] = mapped_column(default=0)


class CompetitionGroupResult(CompetitionResult, Base):
    __tablename__ = "group_results"

    group_id: Mapped[int] = ForeignKey("groups.id")
    group: Mapped[Group] = relationship()


class CompetitionPersonalResult(CompetitionResult, Base):
    __tablename__ = "personal_results"

    person_id: Mapped[int] = ForeignKey("groups.id")
    person: Mapped[Person] = relationship()
