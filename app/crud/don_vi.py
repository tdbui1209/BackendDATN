from sqlalchemy.orm import Session
from app.models import DonVi, NguoiDung, ToKhai, DanhMucDonVi
from app.schemas.don_vi import DonViCreate


def create_don_vi(db: Session, don_vi: DonViCreate):
    db_don_vi = DonVi(
        ma_don_vi=don_vi.ma_don_vi,
        ten_don_vi=don_vi.ten_don_vi,
        email=don_vi.email,
        so_dien_thoai=don_vi.so_dien_thoai,
        ma_danh_muc_don_vi=don_vi.ma_danh_muc_don_vi
    )
    db.add(db_don_vi)
    db.commit()
    db.refresh(db_don_vi)
    return db_don_vi


def get_don_vi(db: Session, skip: int = 0, limit: int = 100, search_string: str = None, ma_danh_muc_don_vi: str = None):
    result = db.query(DonVi)
    if search_string:
        result = result.filter(DonVi.ma_don_vi.like(f'%{search_string}%') | DonVi.ten_don_vi.like(f'%{search_string}%') | DonVi.email.like(f'%{search_string}%') | DonVi.so_dien_thoai.like(f'%{search_string}%'))
    if ma_danh_muc_don_vi:
        result = result.filter(DonVi.ma_danh_muc_don_vi == ma_danh_muc_don_vi)
    return result.offset(skip).limit(limit).all()


def get_don_vi_by_ma_don_vi(db: Session, ma_don_vi: str):
    don_vi = db.query(DonVi).filter(DonVi.ma_don_vi == ma_don_vi).first()
    if don_vi:
        return don_vi
    return None


def update_don_vi(db: Session, ma_don_vi: int, don_vi: DonViCreate):
    db_don_vi = db.query(DonVi).filter(DonVi.ma_don_vi == ma_don_vi).first()
    db_don_vi.ten_don_vi = don_vi.ten_don_vi
    db_don_vi.email = don_vi.email
    db_don_vi.so_dien_thoai = don_vi.so_dien_thoai
    db_don_vi.ma_danh_muc_don_vi = don_vi.ma_danh_muc_don_vi
    db.commit()
    db.refresh(db_don_vi)
    return db_don_vi


def delete_don_vi_by_ma_don_vi(db: Session, ma_don_vi: str):
    if db.query(NguoiDung).filter(NguoiDung.thuoc_don_vi == ma_don_vi).first():
        return {"status": "fail", "message": "Đơn vị này đang được sử dụng"}
    
    if db.query(ToKhai).filter(ToKhai.don_vi_dang_ky == ma_don_vi).first():
        return {"status": "fail", "message": "Đơn vị này đang được sử dụng"}
    
    db_don_vi = db.query(DonVi).filter(DonVi.ma_don_vi == ma_don_vi).first()
    db.delete(db_don_vi)
    db.commit()
    return db_don_vi
