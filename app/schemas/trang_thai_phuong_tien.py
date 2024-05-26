from pydantic import BaseModel
from typing import Optional


class BaseTrangThaiPhuongTien(BaseModel):
    pass

class TrangThaiPhuongTienCreate(BaseTrangThaiPhuongTien):
    ten_trang_thai: str

class TrangThaiPhuongTien(BaseTrangThaiPhuongTien):
    ma_trang_thai: int
    ten_trang_thai: str
    
    class Config:
        from_attributes = True