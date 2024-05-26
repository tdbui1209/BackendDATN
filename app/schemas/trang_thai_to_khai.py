from pydantic import BaseModel
from typing import Optional


class BaseTrangThaiToKhai(BaseModel):
    ten_trang_thai: str

class TrangThaiToKhaiCreate(BaseTrangThaiToKhai):   
    pass    

class TrangThaiToKhai(BaseTrangThaiToKhai):
    ma_trang_thai: int

    class Config:
        from_attributes = True
