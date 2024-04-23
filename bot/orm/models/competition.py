from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum

from ..base import Base


class CompetitionType(str, Enum):
    TEAM = "TEAM"
    TEAM_AGAINST = "TEAM_AGAINST"
    PERSONAL = "PERSONAL"
    PERSON_AGAINST = "PERSON_AGAINST"


class Competition(Base):
    __tablename__ = "competitions"

    name: Mapped[str]
    type: Mapped[CompetitionType] = mapped_column(
        nullable=False,
        default=CompetitionType.TEAM.name,
    )
