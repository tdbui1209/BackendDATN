from pydantic import BaseModel
from typing import Optional


class BasePhuongTien(BaseModel):
    bien_so: str
    so_khung: str
    so_may: str

class PhuongTienCreate(BasePhuongTien):
    pass

class PhuongTien(BasePhuongTien):

    class Config:
        from_attributes = True