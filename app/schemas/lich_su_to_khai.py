from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.trang_thai_to_khai import TrangThaiToKhai
from app.schemas.nguoi_dung import NguoiDung


class BaseLichSuToKhai(BaseModel):
    ma_to_khai: int
    ma_trang_thai: int
    email: str
    thoi_gian: datetime

class LichSuToKhaiCreate(BaseLichSuToKhai):
    pass

class LichSuToKhai(BaseLichSuToKhai):
    ma_lich_su: int
    trang_thai_to_khai: Optional[TrangThaiToKhai]
    nguoi_dung: Optional[NguoiDung]
    
    class Config:
        from_attributes = True
