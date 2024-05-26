from sqlalchemy.orm import Session
from app.models import DanhMucDonVi, DonVi
from app.schemas.danh_muc_don_vi import DanhMucDonViCreate


def create_danh_muc_don_vi(db: Session, danh_muc_don_vi: DanhMucDonViCreate):
    data = db.query(DanhMucDonVi).filter(DanhMucDonVi.ten_danh_muc_don_vi == danh_muc_don_vi.ten_danh_muc_don_vi).first()
    if data:
        return None
    db_danh_muc_don_vi = DanhMucDonVi(
        ma_danh_muc_don_vi=danh_muc_don_vi.ma_danh_muc_don_vi,
        ten_danh_muc_don_vi=danh_muc_don_vi.ten_danh_muc_don_vi
    )
    db.add(db_danh_muc_don_vi)
    db.commit()
    db.refresh(db_danh_muc_don_vi)
    return db_danh_muc_don_vi

def get_danh_muc_don_vi(db: Session, skip: int = 0, limit: int = 100, search_string: str = None):
    data = db.query(DanhMucDonVi)
    if search_string:
        data = data.filter(DanhMucDonVi.ten_danh_muc_don_vi.like(f"%{search_string}%"))
    if not data:
        return None
    return data.offset(skip).limit(limit).all()

def get_danh_muc_don_vi_by_ma_danh_muc_don_vi(db: Session, ma_danh_muc_don_vi: str):
    data = db.query(DanhMucDonVi).filter(DanhMucDonVi.ma_danh_muc_don_vi == ma_danh_muc_don_vi).first()
    if not data:
        return None
    return data

def update_danh_muc_don_vi(db: Session, danh_muc_don_vi: DanhMucDonViCreate):
    data = db.query(DanhMucDonVi).filter(DanhMucDonVi.ma_danh_muc_don_vi == danh_muc_don_vi.ma_danh_muc_don_vi).first()
    if not data:
        return None
    data.ten_danh_muc_don_vi = danh_muc_don_vi.ten_danh_muc_don_vi
    db.commit()
    db.refresh(data)
    return data

def delete_danh_muc_don_vi_by_ma_danh_muc_don_vi(db: Session, ma_danh_muc_don_vi: str):
    data = db.query(DanhMucDonVi).filter(DanhMucDonVi.ma_danh_muc_don_vi == ma_danh_muc_don_vi).first()
    if data:
        return None
    db.query(DanhMucDonVi).filter(DanhMucDonVi.ma_danh_muc_don_vi == ma_danh_muc_don_vi).delete()
    db.commit()
