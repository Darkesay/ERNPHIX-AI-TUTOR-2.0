from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user import User


router = APIRouter(
    prefix="/api/employees",
    tags=["Employees"]
)


@router.get("/")
def get_employees(
    db: Session = Depends(get_db)
):
    employees = db.query(User).all()

    return {
        "total": len(employees),
        "employees": [
            {
                "id": employee.id,
                "name": employee.name,
                "email": employee.email,
            }
            for employee in employees
        ]
    }