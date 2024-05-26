from sqlalchemy.orm import Session
from app.models import LichSuPhuongTien
from app.schemas.lich_su_phuong_tien import LichSuPhuongTienCreate
from datetime import datetime


def create_lich_su_phuong_tien(db: Session, lich_su_phuong_tien: LichSuPhuongTienCreate):
    db_lich_su_phuong_tien = LichSuPhuongTien(
        bien_so=lich_su_phuong_tien.bien_so,
        ma_trang_thai=lich_su_phuong_tien.ma_trang_thai,
        thoi_gian=datetime.now(),
        anh=lich_su_phuong_tien.anh,
        anh_crop=lich_su_phuong_tien.anh_crop
    )
    db.add(db_lich_su_phuong_tien)
    db.commit()
    db.refresh(db_lich_su_phuong_tien)
    return db_lich_su_phuong_tien


def get_lich_su_phuong_tien(db: Session, skip: int = 0, limit: int = 100, search_string: str = None, ma_trang_thai: int = None):
    result = db.query(LichSuPhuongTien)
    if search_string:
        result = result.filter(LichSuPhuongTien.bien_so.like(f"%{search_string}%"))
    if ma_trang_thai:
        result = result.filter(LichSuPhuongTien.ma_trang_thai == ma_trang_thai)
    return result.order_by(LichSuPhuongTien.thoi_gian.desc()).offset(skip).limit(limit).all()


def get_lich_su_phuong_tien_lastest(db: Session):
    return db.query(LichSuPhuongTien).order_by(LichSuPhuongTien.thoi_gian.desc()).first()
