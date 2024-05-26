from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils import get_db
from app.crud import lich_su_tai_khoan as lich_su_tai_khoan_crud
from app.schemas import lich_su_tai_khoan as lich_su_tai_khoan_schema


router = APIRouter(
    prefix="/api",
    tags=["Lịch sử tài khoản"],
    dependencies=[Depends(get_db)]
)


@router.post("/lich-su-tai-khoan", response_model=lich_su_tai_khoan_schema.LichSuTaiKhoan)
def create_lich_su_tai_khoan(lich_su_tai_khoan: lich_su_tai_khoan_schema.LichSuTaiKhoanCreate, db: Session = Depends(get_db)):
    return lich_su_tai_khoan_crud.create_lich_su_tai_khoan(db=db, lich_su_tai_khoan=lich_su_tai_khoan)


@router.get("/lich-su-tai-khoan", response_model=list[lich_su_tai_khoan_schema.LichSuTaiKhoan])
def read_lich_su_tai_khoan(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    lich_su_tai_khoan = lich_su_tai_khoan_crud.get_lich_su_tai_khoan(db, skip=skip, limit=limit)
    return lich_su_tai_khoan
