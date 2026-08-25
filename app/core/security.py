from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone


# Password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# JWT settings
SECRET_KEY = "AI_TUTOR_2_0_SECRET_KEY_CHANGE_THIS_LATER"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def verify_access_token(token: str) -> dict:
    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )