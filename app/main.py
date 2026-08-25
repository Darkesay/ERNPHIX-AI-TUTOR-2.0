from fastapi import FastAPI

from app.database.database import Base, engine

# =========================================================
# DATABASE MODELS
# =========================================================

from app.models.user import User
from app.models.profile import StudentProfile
from app.models.skill_category import SkillCategory
from app.models.skill import Skill
from app.models.course import Course

# =========================================================
# API ROUTERS
# =========================================================

from app.api.routes.auth import router as auth_router
from app.api.routes.users import router as users_router
from app.api.routes.dashboard import router as dashboard_router
from app.api.routes.employees import router as employees_router
from app.api.routes.skills import router as skills_router
from app.api.routes.courses import router as courses_router

# =========================================================
# CREATE DATABASE TABLES
# =========================================================

Base.metadata.create_all(bind=engine)

# =========================================================
# CREATE FASTAPI APPLICATION
# =========================================================

app = FastAPI(
    title="EarnFix API",
    version="1.0.0",
    description="EarnFix AI-powered employee onboarding, skills and learning platform API"
)

# =========================================================
# REGISTER API ROUTES
# =========================================================

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(dashboard_router)
app.include_router(employees_router)
app.include_router(skills_router)
app.include_router(courses_router)

# =========================================================
# HEALTH / HOME
# =========================================================

@app.get("/")
def home():
    return {
        "message": "Welcome to EarnFix API",
        "status": "online",
        "version": "1.0.0"
    }