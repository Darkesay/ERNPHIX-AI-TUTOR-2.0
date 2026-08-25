from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database.database import get_db
from app.models.course import Course
from app.models.skill import Skill
from app.models.skill_category import SkillCategory


router = APIRouter(
    prefix="/api",
    tags=["Courses"]
)


# =========================================================
# REQUEST SCHEMAS
# =========================================================

class CourseCreate(BaseModel):
    title: str
    description: str | None = None
    level: str = "Beginner"
    duration: str | None = None
    category_id: int
    skill_id: int


# =========================================================
# GET ALL COURSES
# =========================================================

@router.get("/courses/")
def get_courses(
    db: Session = Depends(get_db)
):
    courses = db.query(Course).all()

    return {
        "total": len(courses),
        "courses": [
            {
                "id": course.id,
                "title": course.title,
                "description": course.description,
                "level": course.level,
                "duration": course.duration,
                "category_id": course.category_id,
                "category": (
                    course.category.name
                    if course.category
                    else None
                ),
                "skill_id": course.skill_id,
                "skill": (
                    course.skill.name
                    if course.skill
                    else None
                ),
            }
            for course in courses
        ],
    }


# =========================================================
# GET ONE COURSE
# =========================================================

@router.get("/courses/{course_id}")
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    course = (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return {
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "level": course.level,
        "duration": course.duration,
        "category_id": course.category_id,
        "category": (
            course.category.name
            if course.category
            else None
        ),
        "skill_id": course.skill_id,
        "skill": (
            course.skill.name
            if course.skill
            else None
        ),
    }


# =========================================================
# CREATE COURSE
# =========================================================

@router.post("/courses/")
def create_course(
    course_data: CourseCreate,
    db: Session = Depends(get_db)
):
    # Check category
    category = (
        db.query(SkillCategory)
        .filter(
            SkillCategory.id == course_data.category_id
        )
        .first()
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Skill category not found"
        )

    # Check skill
    skill = (
        db.query(Skill)
        .filter(
            Skill.id == course_data.skill_id
        )
        .first()
    )

    if not skill:
        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    # Make sure skill belongs to category
    if skill.category_id != category.id:
        raise HTTPException(
            status_code=400,
            detail="Skill does not belong to the selected category"
        )

    # Prevent duplicate course title
    existing = (
        db.query(Course)
        .filter(
            Course.title == course_data.title
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Course already exists"
        )

    course = Course(
        title=course_data.title,
        description=course_data.description,
        level=course_data.level,
        duration=course_data.duration,
        category_id=course_data.category_id,
        skill_id=course_data.skill_id,
    )

    db.add(course)
    db.commit()
    db.refresh(course)

    return {
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "level": course.level,
        "duration": course.duration,
        "category_id": course.category_id,
        "category": category.name,
        "skill_id": course.skill_id,
        "skill": skill.name,
    }