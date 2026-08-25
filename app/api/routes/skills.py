from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database.database import get_db
from app.models.skill import Skill
from app.models.skill_category import SkillCategory


router = APIRouter(
    prefix="/api",
    tags=["Skills"]
)


# =========================================================
# REQUEST SCHEMAS
# =========================================================

class SkillCategoryCreate(BaseModel):
    name: str
    description: str | None = None


class SkillCreate(BaseModel):
    name: str
    description: str | None = None
    level: str | None = None
    category_id: int


# =========================================================
# SKILL CATEGORIES
# =========================================================

@router.get("/skill-categories/")
def get_skill_categories(db: Session = Depends(get_db)):
    categories = db.query(SkillCategory).all()

    return {
        "total": len(categories),
        "categories": [
            {
                "id": category.id,
                "name": category.name,
                "description": category.description,
            }
            for category in categories
        ],
    }


@router.post("/skill-categories/")
def create_skill_category(
    category_data: SkillCategoryCreate,
    db: Session = Depends(get_db),
):
    existing = (
        db.query(SkillCategory)
        .filter(SkillCategory.name == category_data.name)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Skill category already exists",
        )

    category = SkillCategory(
        name=category_data.name,
        description=category_data.description,
    )

    db.add(category)
    db.commit()
    db.refresh(category)

    return {
        "id": category.id,
        "name": category.name,
        "description": category.description,
    }


# =========================================================
# SKILLS
# =========================================================

@router.get("/skills/")
def get_skills(db: Session = Depends(get_db)):
    skills = db.query(Skill).all()

    return {
        "total": len(skills),
        "skills": [
            {
                "id": skill.id,
                "name": skill.name,
                "description": skill.description,
                "level": skill.level,
                "category_id": skill.category_id,
                "category": (
                    skill.category.name
                    if skill.category
                    else None
                ),
            }
            for skill in skills
        ],
    }


@router.post("/skills/")
def create_skill(
    skill_data: SkillCreate,
    db: Session = Depends(get_db),
):
    category = (
        db.query(SkillCategory)
        .filter(SkillCategory.id == skill_data.category_id)
        .first()
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Skill category not found",
        )

    skill = Skill(
        name=skill_data.name,
        description=skill_data.description,
        level=skill_data.level,
        category_id=skill_data.category_id,
    )

    db.add(skill)
    db.commit()
    db.refresh(skill)

    return {
        "id": skill.id,
        "name": skill.name,
        "description": skill.description,
        "level": skill.level,
        "category_id": skill.category_id,
        "category": category.name,
    }