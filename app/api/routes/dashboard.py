from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user import User


router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def get_dashboard(
    db: Session = Depends(get_db)
):
    total_users = db.query(User).count()

    return {
        "total_users": total_users,
        "total_employees": total_users,
        "total_candidates": 0,
        "active_learners": total_users,
        "total_courses": 0,
        "completion_rate": 0
    }
