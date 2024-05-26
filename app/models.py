from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, VARCHAR, Float, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base 


Base = declarative_base()


class VaiTro(Base):
    __tablename__ = "vai_tro"

    ma_vai_tro = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ten_vai_tro = Column(VARCHAR(20), nullable=False, unique=True)

    nguoi_dung = relationship("NguoiDung", back_populates="vai_tro")


class DanhMucDonVi(Base):
    __tablename__ = "danh_muc_don_vi"

    ma_danh_muc_don_vi = Column(VARCHAR(10), primary_key=True, index=True)
    ten_danh_muc_don_vi = Column(VARCHAR(30), nullable=False, unique=True)

    don_vi = relationship("DonVi", back_populates="danh_muc_don_vi")


class DonVi(Base):
    __tablename__ = "don_vi"

    ma_don_vi = Column(VARCHAR(10), primary_key=True, index=True)
    ten_don_vi = Column(VARCHAR(30), nullable=False, unique=True)
    email = Column(VARCHAR(20), nullable=False, unique=True)
    so_dien_thoai = Column(VARCHAR(11), nullable=False, unique=True)
    ma_danh_muc_don_vi = Column(VARCHAR(10), ForeignKey("danh_muc_don_vi.ma_danh_muc_don_vi"))

    danh_muc_don_vi = relationship("DanhMucDonVi", back_populates="don_vi")
    nguoi_dung = relationship("NguoiDung", back_populates="don_vi")
    to_khai = relationship("ToKhai", back_populates="don_vi")

class NguoiDung(Base):
    __tablename__ = "nguoi_dung"

    email = Column(VARCHAR(20), primary_key=True, index=True)
    mat_khau = Column(VARCHAR(255), nullable=False)
    ho_va_ten = Column(VARCHAR(50), nullable=False)
    so_dien_thoai = Column(VARCHAR(10), nullable=False, unique=True)
    dang_hoat_dong = Column(Boolean, default=True)
    thuoc_don_vi = Column(VARCHAR(10), ForeignKey("don_vi.ma_don_vi"))
    ma_vai_tro = Column(Integer, ForeignKey("vai_tro.ma_vai_tro"))

    don_vi = relationship("DonVi", back_populates="nguoi_dung")
    vai_tro = relationship("VaiTro", back_populates="nguoi_dung")
    to_khai = relationship("ToKhai", back_populates="nguoi_dung")
    lich_su_tai_khoan = relationship("LichSuTaiKhoan", back_populates="nguoi_dung")
    lich_su_to_khai = relationship("LichSuToKhai", back_populates="nguoi_dung")
    van_don = relationship("VanDon", back_populates="nguoi_dung")


class DanhMucHangHoa(Base):
    __tablename__ = "danh_muc_hang_hoa"

    ma_danh_muc_hang_hoa = Column(VARCHAR(10), primary_key=True, index=True)
    ten_danh_muc_hang_hoa = Column(VARCHAR(100), nullable=False, unique=True)

    van_don = relationship("VanDon", back_populates="danh_muc_hang_hoa")


class TrangThaiToKhai(Base):
    __tablename__ = "trang_thai_to_khai"

    ma_trang_thai = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ten_trang_thai = Column(VARCHAR(20), nullable=False, unique=True)

    to_khai = relationship("ToKhai", back_populates="trang_thai_to_khai")
    lich_su_to_khai = relationship("LichSuToKhai", back_populates="trang_thai_to_khai")


class TrangThaiPhuongTien(Base):
    __tablename__ = "trang_thai_phuong_tien"

    ma_trang_thai = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ten_trang_thai = Column(VARCHAR(20), nullable=False, unique=True)

    lich_su_phuong_tien = relationship("LichSuPhuongTien", back_populates="trang_thai_phuong_tien")


class VanDon(Base):
    __tablename__ = "van_don"

    ma_van_don = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nguoi_tao = Column(VARCHAR(20), ForeignKey("nguoi_dung.email"))
    so_luong = Column(Integer, nullable=False)
    trong_luong = Column(Float, nullable=False)
    ten_hang_hoa = Column(VARCHAR(100), nullable=False)
    mo_ta = Column(String, nullable=False)
    ma_danh_muc_hang_hoa = Column(VARCHAR(10), ForeignKey("danh_muc_hang_hoa.ma_danh_muc_hang_hoa"))
    don_vi_xuat_khau = Column(VARCHAR(10), ForeignKey("don_vi.ma_don_vi"))
    don_vi_nhap_khau = Column(VARCHAR(10), ForeignKey("don_vi.ma_don_vi"))
    ngay_tao_van_don = Column(TIMESTAMP, nullable=False)
    bien_so = Column(VARCHAR(10), nullable=False)

    danh_muc_hang_hoa = relationship("DanhMucHangHoa", back_populates="van_don")
    to_khai = relationship("ToKhai", back_populates="van_don")
    nguoi_dung = relationship("NguoiDung", back_populates="van_don")


class ToKhai(Base):
    __tablename__ = "to_khai"

    ma_to_khai = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(VARCHAR(20), ForeignKey("nguoi_dung.email"))
    don_vi_dang_ky = Column(VARCHAR(10), ForeignKey("don_vi.ma_don_vi"))
    ngay_tao_to_khai = Column(TIMESTAMP, nullable=False)
    ngay_dang_ky = Column(TIMESTAMP, nullable=False)
    ma_trang_thai = Column(Integer, ForeignKey("trang_thai_to_khai.ma_trang_thai"))
    ma_van_don = Column(Integer, ForeignKey("van_don.ma_van_don"))

    nguoi_dung = relationship("NguoiDung", back_populates="to_khai")
    don_vi = relationship("DonVi", back_populates="to_khai")
    trang_thai_to_khai = relationship("TrangThaiToKhai", back_populates="to_khai")
    van_don = relationship("VanDon", back_populates="to_khai")
    lich_su_to_khai = relationship("LichSuToKhai", back_populates="to_khai")


class LichSuPhuongTien(Base):
    __tablename__ = "lich_su_phuong_tien"

    ma_lich_su = Column(Integer, primary_key=True, index=True, autoincrement=True)
    bien_so = Column(VARCHAR(10), nullable=False)
    ma_trang_thai = Column(Integer, ForeignKey("trang_thai_phuong_tien.ma_trang_thai"))
    thoi_gian = Column(TIMESTAMP, nullable=False)
    anh = Column(String, nullable=False)
    anh_crop = Column(String, nullable=False)

    trang_thai_phuong_tien = relationship("TrangThaiPhuongTien", back_populates="lich_su_phuong_tien")


class LichSuToKhai(Base):
    __tablename__ = "lich_su_to_khai"

    ma_lich_su = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ma_to_khai = Column(Integer, ForeignKey("to_khai.ma_to_khai"))
    ma_trang_thai = Column(Integer, ForeignKey("trang_thai_to_khai.ma_trang_thai"))
    email = Column(VARCHAR(20), ForeignKey("nguoi_dung.email"))
    thoi_gian = Column(TIMESTAMP, nullable=False)

    to_khai = relationship("ToKhai", back_populates="lich_su_to_khai")
    trang_thai_to_khai = relationship("TrangThaiToKhai", back_populates="lich_su_to_khai")
    nguoi_dung = relationship("NguoiDung", back_populates="lich_su_to_khai")


class DanhMucHanhDong(Base):
    __tablename__ = "danh_muc_hanh_dong"

    ma_hanh_dong = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ten_hanh_dong = Column(VARCHAR(20), nullable=False, unique=True)

    lich_su_tai_khoan = relationship("LichSuTaiKhoan", back_populates="danh_muc_hanh_dong")


class LichSuTaiKhoan(Base):
    __tablename__ = "lich_su_tai_khoan"

    ma_lich_su = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(VARCHAR(20), ForeignKey("nguoi_dung.email"))
    thoi_gian = Column(TIMESTAMP, nullable=False)
    ma_hanh_dong = Column(Integer, ForeignKey("danh_muc_hanh_dong.ma_hanh_dong"))

    nguoi_dung = relationship("NguoiDung", back_populates="lich_su_tai_khoan")
    danh_muc_hanh_dong = relationship("DanhMucHanhDong", back_populates="lich_su_tai_khoan")
