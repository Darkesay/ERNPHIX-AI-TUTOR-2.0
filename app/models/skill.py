from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    level = Column(
        String,
        nullable=True
    )

    category_id = Column(
        Integer,
        ForeignKey("skill_categories.id"),
        nullable=False
    )

    category = relationship(
        "SkillCategory",
        back_populates="skills"
    )

    courses = relationship(
        "Course",
        back_populates="skill",
        cascade="all, delete-orphan"
    )