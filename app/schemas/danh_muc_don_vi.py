from pydantic import BaseModel
from typing import Optional


class BaseDanhMucDonVi(BaseModel):
    ma_danh_muc_don_vi: str
    ten_danh_muc_don_vi: str


class DanhMucDonViCreate(BaseDanhMucDonVi):
    pass


class DanhMucDonVi(BaseDanhMucDonVi):
    
    class Config:
        from_attributes = True
