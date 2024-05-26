from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import JWTError, jwt
from pydantic import BaseModel
from app.models import NguoiDung
from typing import Annotated
from app.utils import get_db


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class NguoiDungService:
    def __init__(self): 
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.access_token_expire_minutes = 30
        self.secret_key="f6926e5c72a6ab9ff52eb16876bb8c9b0f45d2c1a16e27ac28c92f100536f9f6"
        self.algorithm="HS256"
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, plain_password):
        return self.pwd_context.hash(plain_password)
    
    def get_user(self, email: str, db: Session):
        return db.query(NguoiDung).filter(NguoiDung.email == email).first()
    
    def authenticate_user(self, email: str, password: str, db: Session):
        user = self.get_user(email, db)
        if not user:
            return False
        if not self.verify_password(password, user.mat_khau):
            return False
        return user

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=self.access_token_expire_minutes)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt
    
    async def get_current_user(self, token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="login"))],
                               db: Session = Depends(get_db)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except JWTError:
            raise credentials_exception
        user = self.get_user(email=token_data.username, db=db)
        if user is None:
            raise credentials_exception
        return user
    
    async def get_current_active_user(
        current_user: Annotated[NguoiDung, Depends(get_current_user)],
    ):
        if not current_user.is_active:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
