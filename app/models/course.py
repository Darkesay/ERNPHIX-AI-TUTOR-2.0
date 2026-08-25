from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(200),
        nullable=False,
        index=True
    )

    description = Column(
        Text,
        nullable=True
    )

    level = Column(
        String(50),
        nullable=False,
        default="Beginner"
    )

    duration = Column(
        String(100),
        nullable=True
    )

    category_id = Column(
        Integer,
        ForeignKey("skill_categories.id"),
        nullable=False
    )

    skill_id = Column(
        Integer,
        ForeignKey("skills.id"),
        nullable=False
    )

    category = relationship(
        "SkillCategory",
        back_populates="courses"
    )

    skill = relationship(
        "Skill",
        back_populates="courses"
    )