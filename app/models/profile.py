from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    education_level = Column(
        String,
        nullable=True
    )

    current_level = Column(
        String,
        nullable=True
    )

    learning_goal = Column(
        String,
        nullable=True
    )

    preferred_learning_style = Column(
        String,
        nullable=True
    )

    interests = Column(
        String,
        nullable=True
    )

    user = relationship(
        "User",
        back_populates="profile"
    )