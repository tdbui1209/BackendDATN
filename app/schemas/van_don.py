from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.danh_muc_hang_hoa import DanhMucHangHoa
from app.schemas.nguoi_dung import NguoiDung


class BaseVanDon(BaseModel):
    so_luong: int
    trong_luong: float
    ten_hang_hoa: str
    mo_ta: str
    ma_danh_muc_hang_hoa: str
    don_vi_xuat_khau: str
    don_vi_nhap_khau: str
    bien_so: str
    

class VanDonCreate(BaseVanDon):
    nguoi_tao: str

class VanDon(BaseVanDon):
    ma_van_don: int
    ngay_tao_van_don: datetime
    danh_muc_hang_hoa: Optional[DanhMucHangHoa]
    nguoi_dung: Optional[NguoiDung]
    
    class Config:
        from_attributes = True
