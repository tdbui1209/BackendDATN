from sqlalchemy.orm import Session
from app.models import DanhMucHanhDong
from app.schemas.danh_muc_hanh_dong import DanhMucHanhDongCreate


def create_danh_muc_hanh_dong(db: Session, danh_muc_hanh_dong: DanhMucHanhDongCreate):
    db_danh_muc_hanh_dong = DanhMucHanhDong(
        ten_hanh_dong=danh_muc_hanh_dong.ten_hanh_dong
    )
    db.add(db_danh_muc_hanh_dong)
    db.commit()
    db.refresh(db_danh_muc_hanh_dong)
    return db_danh_muc_hanh_dong


def get_danh_muc_hanh_dong(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DanhMucHanhDong).offset(skip).limit(limit).all()


def get_danh_muc_hanh_dong_by_id(db: Session, ma_hanh_dong: str):
    return db.query(DanhMucHanhDong).filter(DanhMucHanhDong.ma_hanh_dong == ma_hanh_dong).first()


def update_danh_muc_hanh_dong(db: Session, ma_hanh_dong: str, danh_muc_hanh_dong: DanhMucHanhDongCreate):
    db.query(DanhMucHanhDong).filter(DanhMucHanhDong.ma_hanh_dong == ma_hanh_dong).update({
        DanhMucHanhDong.ten_hanh_dong: danh_muc_hanh_dong.ten_hanh_dong
    })
    db.commit()
    return db.query(DanhMucHanhDong).filter(DanhMucHanhDong.ma_hanh_dong == ma_hanh_dong).first()


def delete_danh_muc_hanh_dong(db: Session, ma_hanh_dong: str):
    db.query(DanhMucHanhDong).filter(DanhMucHanhDong.ma_hanh_dong == ma_hanh_dong).delete()
    db.commit()
    return True
