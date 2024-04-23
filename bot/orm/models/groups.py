from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped

from orm.base import Base


class Group(Base):
    __tablename__ = "groups"

    name: Mapped[int]  # AA-11

    @hybrid_property
    def course(self):
        return int(self.name.split("-")[1][1])
