from sqlalchemy.orm import Session
from app.models import DanhMucHangHoa, VanDon
from app.schemas.danh_muc_hang_hoa import DanhMucHangHoaCreate


def create_danh_muc_hang_hoa(db: Session, danh_muc_hang_hoa: DanhMucHangHoaCreate):
    db_danh_muc_hang_hoa = DanhMucHangHoa(
        ma_danh_muc_hang_hoa=danh_muc_hang_hoa.ma_danh_muc_hang_hoa,
        ten_danh_muc_hang_hoa=danh_muc_hang_hoa.ten_danh_muc_hang_hoa
    )
    db.add(db_danh_muc_hang_hoa)
    db.commit()
    db.refresh(db_danh_muc_hang_hoa)
    return db_danh_muc_hang_hoa


def get_danh_muc_hang_hoa_by_ma_danh_muc_hang_hoa(db: Session, ma_danh_muc_hang_hoa: str):
    return db.query(DanhMucHangHoa).filter(DanhMucHangHoa.ma_danh_muc_hang_hoa == ma_danh_muc_hang_hoa).first()


def get_danh_muc_hang_hoa(db: Session, skip: int = 0, limit: int = 100, search_string: str = None):
    if search_string:
        return db.query(DanhMucHangHoa).filter(DanhMucHangHoa.ten_danh_muc_hang_hoa.like(f"%{search_string}%")).offset(skip).limit(limit).all()
    return db.query(DanhMucHangHoa).offset(skip).limit(limit).all()


def update_danh_muc_hang_hoa(db: Session, danh_muc_hang_hoa_id: int, danh_muc_hang_hoa: DanhMucHangHoaCreate):
    db.query(DanhMucHangHoa).filter(DanhMucHangHoa.ma_danh_muc_hang_hoa == danh_muc_hang_hoa_id).update({
        DanhMucHangHoa.ma_danh_muc_hang_hoa: danh_muc_hang_hoa.ma_danh_muc_hang_hoa,
        DanhMucHangHoa.ten_danh_muc_hang_hoa: danh_muc_hang_hoa.ten_danh_muc_hang_hoa
    })
    db.commit()
    return db.query(DanhMucHangHoa).filter(DanhMucHangHoa.ma_danh_muc_hang_hoa == danh_muc_hang_hoa_id).first()


def delete_danh_muc_hang_hoa(db: Session, danh_muc_hang_hoa_id: int):
    if db.query(VanDon).filter(VanDon.ma_danh_muc_hang_hoa == danh_muc_hang_hoa_id).first():
        return {"status": "fail", "message": "Danh mục hàng hóa này đang được sử dụng"}
    db.query(DanhMucHangHoa).filter(DanhMucHangHoa.ma_danh_muc_hang_hoa == danh_muc_hang_hoa_id).delete()
    db.commit()
    return True
