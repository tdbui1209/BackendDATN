from pydantic import BaseModel
from typing import Optional


class BaseDanhMucHanhDong(BaseModel):
    
    ten_hanh_dong: str


class DanhMucHanhDongCreate(BaseDanhMucHanhDong):
    pass


class DanhMucHanhDong(BaseDanhMucHanhDong):
    ma_hanh_dong: int
    
    class Config:
        from_attributes = True
