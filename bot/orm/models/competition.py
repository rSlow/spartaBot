from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum

from ..base import Base


class CompetitionType(int, Enum):
    TEAM = 1
    TEAM_AGAINST = 2
    PERSONAL = 3
    PERSON_AGAINST = 4


class Competition(Base):
    __tablename__ = "competitions"

    name: Mapped[str]
    type = mapped_column(
        SQLEnum(CompetitionType),
        nullable=False,
        default=CompetitionType.TEAM.value
    )
