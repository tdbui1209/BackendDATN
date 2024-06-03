from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.utils import get_db, host
from app.crud import nguoi_dung as crud_nguoi_dung
from app.schemas import nguoi_dung as schema_nguoi_dung, vai_tro as schema_vai_tro
from app.services.nguoi_dung import NguoiDungService
import requests


router = APIRouter(
    prefix="/api",
    tags=["Người dùng"],
    responses={404: {"description": "Not found"}},
    # dependencies=[Depends(NguoiDungService().get_current_user)]
)


@router.post("/nguoi-dung", response_model=schema_nguoi_dung.NguoiDung, status_code=status.HTTP_201_CREATED)
def create_user(nguoi_dung: schema_nguoi_dung.NguoiDungCreate, db: Session = Depends(get_db)):
    data = crud_nguoi_dung.create_nguoi_dung(db, nguoi_dung)
    if not data:
        raise HTTPException(status_code=400, detail="Email đã tồn tại")
    requests.post(f"{host}/api/lich-su-tai-khoan", json={"email": nguoi_dung.email, "ma_hanh_dong": 6})
    return data


@router.get("/nguoi-dung", response_model=list[schema_nguoi_dung.NguoiDung], status_code=status.HTTP_200_OK)
def read_user(skip: int = 0, limit: int = 100, search_string: str = None, dang_hoat_dong: bool = None, ma_vai_tro: str = None, db: Session = Depends(get_db)):
    data = crud_nguoi_dung.get_nguoi_dung(db, skip=skip, limit=limit, search_string=search_string, dang_hoat_dong=dang_hoat_dong, ma_vai_tro=ma_vai_tro)
    if not data:
        raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")
    return data


@router.get("/nguoi-dung/{email}", response_model=schema_nguoi_dung.NguoiDung, status_code=status.HTTP_200_OK)
def read_user_by_email(email: str, db: Session = Depends(get_db)):
    data = crud_nguoi_dung.get_nguoi_dung_by_email(db, email)
    if data is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")
    return data


@router.get("/nguoi-dung/{email}/vai-tro", response_model=schema_vai_tro.VaiTro, status_code=status.HTTP_200_OK)
def read_user_role(email: str, db: Session = Depends(get_db)):
    data = crud_nguoi_dung.get_ma_vai_tro_nguoi_dung(db, email)
    if data is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")
    return data


@router.put("/nguoi-dung/{email}", response_model=schema_nguoi_dung.NguoiDungBase, status_code=status.HTTP_200_OK)
def update_user(email: str, user: schema_nguoi_dung.NguoiDungBase, db: Session = Depends(get_db)):
    data = crud_nguoi_dung.update_nguoi_dung(db, email, user)
    if data is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")
    return data


@router.patch("/nguoi-dung/{email}")
def update_status_user(email: str, status: bool, db: Session = Depends(get_db)):
    data = crud_nguoi_dung.update_status_nguoi_dung(db, email, status)
    if data is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")
    return data


@router.delete("/nguoi-dung/{email}")
def delete_user(email: str, db: Session = Depends(get_db)):
    data = crud_nguoi_dung.delete_nguoi_dung(db, email)
    if data is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")
    return data


@router.patch("/nguoi-dung/{email}/khoi-phuc-mat-khau")
def change_password(email: str, db: Session = Depends(get_db)):
    data = crud_nguoi_dung.reset_password(db, email)
    if data is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")
    requests.post(f"{host}/api/lich-su-tai-khoan", json={"email": email, "ma_hanh_dong": 7})
    return data


@router.patch("/nguoi-dung/{email}/doi-mat-khau")
def change_password(email: str, old_password: str, new_password: str, db: Session = Depends(get_db)):
    data = crud_nguoi_dung.change_password(db, email, old_password, new_password)
    if data is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")
    if data is False:
        raise HTTPException(status_code=400, detail="Mật khẩu không khớp")
    requests.post(f"{host}/api/lich-su-tai-khoan", json={"email": email, "ma_hanh_dong": 3})
    return data


@router.patch("/nguoi-dung/{email}/khoa-tai-khoan")
def lock_user(email: str, db: Session = Depends(get_db)):
    data = crud_nguoi_dung.lock_user(email, db)
    if data is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")
    requests.post(f"{host}/api/lich-su-tai-khoan", json={"email": email, "ma_hanh_dong": 4})
    return data


@router.patch("/nguoi-dung/{email}/mo-khoa-tai-khoan")
def unlock_user(email: str, db: Session = Depends(get_db)):
    data = crud_nguoi_dung.unlock_user(email, db)
    if data is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy người dùng")
    requests.post(f"{host}/api/lich-su-tai-khoan", json={"email": email, "ma_hanh_dong": 5})
    return data
