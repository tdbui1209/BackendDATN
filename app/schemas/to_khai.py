from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date
from app.schemas.trang_thai_to_khai import TrangThaiToKhai
from app.schemas.van_don import VanDon


class BaseToKhai(BaseModel):
    email: str
    don_vi_dang_ky: str
    ma_van_don: int
    ngay_dang_ky: date

class ToKhaiCreate(BaseToKhai):
    pass

class ToKhai(BaseToKhai):
    ma_to_khai: int
    ma_trang_thai: int
    ngay_tao_to_khai: datetime
    trang_thai_to_khai: Optional[TrangThaiToKhai]
    van_don: Optional[VanDon]
    
    class Config:
        from_attributes = True
