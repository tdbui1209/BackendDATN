from sqlalchemy.orm import Session
from app.models import LichSuTaiKhoan
from app.schemas.lich_su_tai_khoan import LichSuTaiKhoanCreate
from datetime import datetime


def create_lich_su_tai_khoan(db: Session, lich_su_tai_khoan: LichSuTaiKhoanCreate):
    db_lich_su_tai_khoan = LichSuTaiKhoan(
        email=lich_su_tai_khoan.email,
        ma_hanh_dong=lich_su_tai_khoan.ma_hanh_dong,
        thoi_gian=datetime.now()
    )
    db.add(db_lich_su_tai_khoan)
    db.commit()
    db.refresh(db_lich_su_tai_khoan)
    return db_lich_su_tai_khoan


def get_lich_su_tai_khoan(db: Session, skip: int = 0, limit: int = 100):
    return db.query(LichSuTaiKhoan).order_by(LichSuTaiKhoan.ma_lich_su.desc()).offset(skip).limit(limit).all()
