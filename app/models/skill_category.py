from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class SkillCategory(Base):
    __tablename__ = "skill_categories"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        unique=True,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    skills = relationship(
        "Skill",
        back_populates="category",
        cascade="all, delete-orphan"
    )

    courses = relationship(
        "Course",
        back_populates="category",
        cascade="all, delete-orphan"
    )