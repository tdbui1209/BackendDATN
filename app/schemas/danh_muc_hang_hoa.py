from pydantic import BaseModel
from typing import Optional


class BaseDanhMucHangHoa(BaseModel):
    ma_danh_muc_hang_hoa: str
    ten_danh_muc_hang_hoa: str

class DanhMucHangHoaCreate(BaseDanhMucHangHoa):
    pass

class DanhMucHangHoa(BaseDanhMucHangHoa):
    
    class Config:
        from_attributes = True
