from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime

from app.utils import get_db, host
from app.services.nguoi_dung import NguoiDungService, Token
from app.crud.lich_su_tai_khoan import create_lich_su_tai_khoan
from app.schemas.lich_su_tai_khoan import LichSuTaiKhoanCreate

import requests


router = APIRouter(
    prefix="/api",
    tags=["default"],
    responses={404: {"description": "Not found"}}
)


@router.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)) -> Token:
    user = NguoiDungService().authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    create_lich_su_tai_khoan(db, LichSuTaiKhoanCreate(email=user.email, ma_hanh_dong=1))
    requests.post(f"{host}/api/lich-su-tai-khoan", json={"email": user.email, "ma_hanh_dong": 1})
    return {"access_token": NguoiDungService().create_access_token(data={"sub": user.email}), "token_type": "bearer"}
