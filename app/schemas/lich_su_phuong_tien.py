from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.trang_thai_phuong_tien import TrangThaiPhuongTien


class BaseLichSuPhuongTien(BaseModel):
    bien_so: str
    ma_trang_thai: int
    anh: Optional[str] = None,
    anh_crop: Optional[str] = None

class LichSuPhuongTienCreate(BaseLichSuPhuongTien):
    pass

class LichSuPhuongTien(BaseLichSuPhuongTien):
    ma_lich_su: int
    thoi_gian: datetime
    trang_thai_phuong_tien: Optional[TrangThaiPhuongTien]

    class Config:
        from_attributes = True
