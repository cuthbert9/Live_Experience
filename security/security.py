from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext


SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def create_token(data):
    to_encode=data.copy()
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)


def hash_password(password:str):
    return pwd_context.hash(password)


def verify_password(plain_password:str ,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)