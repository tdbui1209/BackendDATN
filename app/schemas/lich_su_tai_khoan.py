from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.danh_muc_hanh_dong import DanhMucHanhDong


class BaseLichSuTaiKhoan(BaseModel):
    email: str
    ma_hanh_dong: int


class LichSuTaiKhoanCreate(BaseLichSuTaiKhoan):
    pass


class LichSuTaiKhoan(BaseLichSuTaiKhoan):
    ma_lich_su: int
    thoi_gian: datetime
    danh_muc_hanh_dong: Optional[DanhMucHanhDong]

    class Config:
        from_attributes = True
