from pydantic import BaseModel
from typing import Optional
from app.schemas.danh_muc_don_vi import DanhMucDonVi


class BaseDonVi(BaseModel):
    ma_don_vi: str
    ten_don_vi: str
    email: str
    so_dien_thoai: str
    ma_danh_muc_don_vi: str


class DonViCreate(BaseDonVi):
    pass


class DonVi(BaseDonVi):
    danh_muc_don_vi: Optional[DanhMucDonVi]

    class Config:
        from_attributes = True
