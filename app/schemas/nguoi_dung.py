from pydantic import BaseModel
from typing import Optional
from app.schemas.vai_tro import VaiTro


class NguoiDungBase(BaseModel):
    email: str
    ho_va_ten: str
    so_dien_thoai: str
    thuoc_don_vi: str
    ma_vai_tro: int


class NguoiDungInDB(NguoiDungBase):
    mat_khau: str


class NguoiDungCreate(NguoiDungBase):
    mat_khau: str


class NguoiDung(NguoiDungBase):
    dang_hoat_dong: bool
    vai_tro: Optional[VaiTro]

    class Config:
        from_attributes = True