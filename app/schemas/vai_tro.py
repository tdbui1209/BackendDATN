from pydantic import BaseModel
from typing import Optional


class BaseVaiTro(BaseModel):
    ten_vai_tro: str


class VaiTroCreate(BaseVaiTro):
    pass


class VaiTro(BaseVaiTro):
    ma_vai_tro: int
    
    class Config:
        from_attributes = True
