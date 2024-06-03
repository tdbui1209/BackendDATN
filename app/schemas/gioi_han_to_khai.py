from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BaseGioiHanToKhai(BaseModel):
    so_luong_gioi_han: int


class GioiHanToKhaiCreate(BaseGioiHanToKhai):
    pass


class GioiHanToKhai(BaseGioiHanToKhai):
    ma_lich_su: int
    thoi_gian: datetime

    class Config:
        from_attributes = True
