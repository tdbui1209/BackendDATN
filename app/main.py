from fastapi import FastAPI

from . import models
from .database import engine
from .routes import nguoi_dung, vai_tro, danh_muc_don_vi, login , don_vi, phuong_tien, trang_thai_phuong_tien, lich_su_phuong_tien, danh_muc_hang_hoa, van_don, to_khai, trang_thai_to_khai
from .routes import danh_muc_hanh_dong, lich_su_tai_khoan, thong_ke, lich_su_to_khai

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(danh_muc_don_vi.router)
app.include_router(vai_tro.router)
app.include_router(nguoi_dung.router)
app.include_router(login.router)
app.include_router(don_vi.router)
# app.include_router(phuong_tien.router)
app.include_router(trang_thai_phuong_tien.router)
app.include_router(lich_su_phuong_tien.router)
app.include_router(danh_muc_hang_hoa.router)
app.include_router(van_don.router)
app.include_router(to_khai.router)
app.include_router(trang_thai_to_khai.router)
app.include_router(danh_muc_hanh_dong.router)
app.include_router(lich_su_tai_khoan.router)
app.include_router(lich_su_to_khai.router)
app.include_router(thong_ke.router)
