import requests
import json
import random
from datetime import datetime


# Config
ENDPOINT = "http://192.168.1.8:8000/api/"
session = requests.Session()


# Payload gioi han to khai
gioi_han_to_khai = {
    "so_luong_gioi_han": 20
}

session.post(ENDPOINT + "gioi-han-to-khai", data=json.dumps(gioi_han_to_khai))
print("Gioi han to khai da duoc tao")


# Payload danh muc don vi
danh_muc_don_vi_list = [
    {
        "ma_danh_muc_don_vi": "CK",
        "ten_danh_muc_don_vi": "Cửa khẩu"
    },
    {
        "ma_danh_muc_don_vi": "DN",
        "ten_danh_muc_don_vi": "Doanh nghiệp"
    },
    {
        "ma_danh_muc_don_vi": "AD",
        "ten_danh_muc_don_vi": "Admin"
    }
]

for danh_muc_don_vi in danh_muc_don_vi_list:
    session.post(ENDPOINT + "danh-muc-don-vi", data=json.dumps(danh_muc_don_vi))
    print(f"Danh muc don vi {danh_muc_don_vi['ma_danh_muc_don_vi']} da duoc tao")


# Payload don vi
don_vi_list = [
    {
        "ma_don_vi": "CK1",
        "ten_don_vi": "Cửa khẩu Móng Cái",
        "email": "cuakhau.mongcai@cuakhau.org",
        "so_dien_thoai": "0345678901",
        "ma_danh_muc_don_vi": "CK"
    },
    { 
        "ma_don_vi": "TID",
        "ten_don_vi": "Công ty TNHH Thương mại và Dịch vụ Tiến Doanh",
        "email": "admin@tiendoanh.vn",
        "so_dien_thoai": "0987654321",
        "ma_danh_muc_don_vi": "DN"
    },
    {
        "ma_don_vi": "ABC",
        "ten_don_vi": "Công ty TNHH Xuất nhập khẩu ABC",
        "email": "admin@abc.com",
        "so_dien_thoai": "0123456789",
        "ma_danh_muc_don_vi": "DN"
    },
    {
        "ma_don_vi": "AD1",
        "ten_don_vi": "Admin 1",
        "email": "admin@admin.com",
        "so_dien_thoai": "0245678901",
        "ma_danh_muc_don_vi": "AD"
    },
    {
        "ma_don_vi": "PLA",
        "ten_don_vi": "Công ty TNHH Phát Lộc An",
        "email": "admin@phatlocan.vn",
        "so_dien_thoai": "1357924680",
        "ma_danh_muc_don_vi": "DN"
    },
    {
        "ma_don_vi": "TAK",
        "ten_don_vi": "Công ty TNHH Thương mại và Dịch vụ Tiến An Khang",
        "email": "admin@tienankhang.vn",
        "so_dien_thoai": "2468013579",
        "ma_danh_muc_don_vi": "DN"
    },
    {
        "ma_don_vi": "ANM",
        "ten_don_vi": "Công ty TNHH Anh Minh",
        "email": "admin@anhminh.com",
        "so_dien_thoai": "3579246801",
        "ma_danh_muc_don_vi": "DN"
    },
    {
        "ma_don_vi": "BN",
        "ten_don_vi": "Công ty TNHH Bình Nguyên",
        "email": "admin@binhnguyen.com",
        "so_dien_thoai": "4680135792",
        "ma_danh_muc_don_vi": "DN"
    }
]

for don_vi in don_vi_list:
    session.post(ENDPOINT + "don-vi", data=json.dumps(don_vi))
    print(f"Don vi {don_vi['ma_don_vi']} da duoc tao")


# Payload danh muc hang hoa
danh_muc_hang_hoa_list = [
    {
        "ma_danh_muc_hang_hoa": "09022010",
        "ten_danh_muc_hang_hoa": "Lá chè xanh"
    },
    {
        "ma_danh_muc_hang_hoa": "09024010",
        "ten_danh_muc_hang_hoa": "Lá chè đen"
    },
    {
        "ma_danh_muc_hang_hoa": "07020000",
        "ten_danh_muc_hang_hoa": "Cà chua, tươi hoặc ướp lạnh"
    },
    {
        "ma_danh_muc_hang_hoa": "07031000",
        "ten_danh_muc_hang_hoa": "Hành, củ hành, tỏi, củ tỏi, củ hẹ"
    },
    {
        "ma_danh_muc_hang_hoa": "07041000",
        "ten_danh_muc_hang_hoa": "Cải bắp, cải cầu vồng, cải thảo, cải bắp cải"
    }
]

for danh_muc_hang_hoa in danh_muc_hang_hoa_list:
    session.post(ENDPOINT + "danh-muc-hang-hoa", data=json.dumps(danh_muc_hang_hoa))
    print(f"Danh muc hang hoa {danh_muc_hang_hoa['ma_danh_muc_hang_hoa']} da duoc tao")


# Payload nguoi dung
nguoi_dung_list = [
    {
        "email": "nhanvien@abc.com",
        "ho_va_ten": "Nhân Viên",
        "so_dien_thoai": "1357924680",
        "thuoc_don_vi": "ABC",
        "ma_vai_tro": 5,
        "mat_khau": "nhanvienabc"
    },
    {
        "email": "admin@admin.com",
        "ho_va_ten": "Admin",
        "so_dien_thoai": "2468135790",
        "thuoc_don_vi": "AD",
        "ma_vai_tro": 1,
        "mat_khau": "admin"
    },
    {
        "email": "nhanvien@tiendoanh.vn",
        "ho_va_ten": "Nhân Viên",
        "so_dien_thoai": "3579246801",
        "thuoc_don_vi": "TID",
        "ma_vai_tro": 5,
        "mat_khau": "nhanvientiendoanh"
    },
    {
        "email": "nhanvien@phatlocan.vn",
        "ho_va_ten": "Nhân Viên",
        "so_dien_thoai": "4680135792",
        "thuoc_don_vi": "PLA",
        "ma_vai_tro": 5,
        "mat_khau": "nhanvienphatlocan"
    },
    {
        "email": "nhanvien@tienankhang.vn",
        "ho_va_ten": "Nhân Viên",
        "so_dien_thoai": "5792468013",
        "thuoc_don_vi": "TAK",
        "ma_vai_tro": 5,
        "mat_khau": "nhanvientienankhang"
    },
    {
        "email": "nhanvien@anhminh.com",
        "ho_va_ten": "Nhân Viên",
        "so_dien_thoai": "6803579241",
        "thuoc_don_vi": "ANM",
        "ma_vai_tro": 5,
        "mat_khau": "nhanvienanhminh"
    },
    {
        "email": "nhanvien@binhnguyen.com",
        "ho_va_ten": "Nhân Viên",
        "so_dien_thoai": "7914680132",
        "thuoc_don_vi": "BN",
        "ma_vai_tro": 5,
        "mat_khau": "nhanvienbinhnguyen"
    },
    {
        "email": "canbo@langson.vn",
        "ho_va_ten": "Cán bộ",
        "so_dien_thoai": "0245678901",
        "thuoc_don_vi": "CK1",
        "ma_vai_tro": 4,
        "mat_khau": "canbolangson"
    }
]

for nguoi_dung in nguoi_dung_list:
    session.post(ENDPOINT + "nguoi-dung", data=json.dumps(nguoi_dung))
    print(f"Nguoi dung {nguoi_dung['email']} da duoc tao")


# Payload van don
van_don_list = []
ten_hang_hoa_list = [
    "Chè Thái Nguyên", "Chè Cổ Thụ", "Cà chua", "Hành", "Cải bắp",
    "Lá chè xanh", "Lá chè đen", "Hành củ", "Tỏi củ", "Cải thảo"
]
for i in range(1, 100000):
    van_don = {
        "so_luong": random.randint(1, 300),
        "trong_luong": random.randint(50, 500),
        "ten_hang_hoa": random.choice(ten_hang_hoa_list),
        "mo_ta": f"{random.choice(ten_hang_hoa_list)} ngon nhất",
        "ma_danh_muc_hang_hoa": random.choice(["09022010", "09024010", "07020000", "07031000", "07041000"]),
        "don_vi_xuat_khau": random.choice(["TID", "ABC", "PLA", "TAK", "ANM", "BN"]),
        "don_vi_nhap_khau": random.choice(["TID", "ABC", "PLA", "TAK", "ANM", "BN"]),
        "bien_so": f"{random.randint(10, 99)}{random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z'])}{random.randint(10000, 99999)}",
        "nguoi_tao": f"nhanvien@{random.choice(['abc.com', 'tiendoanh.vn', 'phatlocan.vn', 'tienankhang.vn', 'anhminh.com', 'binhnguyen.com'])}"
    }
    van_don_list.append(van_don)

bien_so_list = ["15C34033", "15A23744", "15C07193", "15C76194", "30E13724"]

for i in range(len(bien_so_list)):
    van_don = {
        "so_luong": random.randint(1, 300),
        "trong_luong": random.randint(50, 500),
        "ten_hang_hoa": random.choice(ten_hang_hoa_list),
        "mo_ta": f"{random.choice(ten_hang_hoa_list)} ngon nhất",
        "ma_danh_muc_hang_hoa": random.choice(["09022010", "09024010", "07020000", "07031000", "07041000"]),
        "don_vi_xuat_khau": random.choice(["TID", "ABC", "PLA", "TAK", "ANM", "BN"]),
        "don_vi_nhap_khau": random.choice(["TID", "ABC", "PLA", "TAK", "ANM", "BN"]),
        "bien_so": bien_so_list[i],
        "nguoi_tao": f"nhanvien@{random.choice(['abc.com', 'tiendoanh.vn', 'phatlocan.vn', 'tienankhang.vn', 'anhminh.com', 'binhnguyen.com'])}"
    }
    van_don_list.append(van_don)

for van_don in van_don_list:
    session.post(ENDPOINT + "van-don", data=json.dumps(van_don))
    print(f"Van don {van_don['bien_so']} da duoc tao")

for i in range(1, len(van_don_list)):
    thang = random.randint(1, 5)
    ngay = random.randint(1, 31)
    if ngay > 28 and thang == 2:
        ngay = 28
    if ngay == 31 and thang in [4, 6, 9, 11]:
        ngay = 30
        
    if thang == 5 and ngay > 29:
        ngay = 29

    session.patch(ENDPOINT + f"van-don/{i}/ngay-tao/{f'2024-{thang}-{ngay}'}")
    print(f"Ngay tao cua van don {van_don_list[i]['bien_so']} da duoc cap nhat")

# Payload vai tro
vai_tro_list = [
    {
        "ten_vai_tro": "Admin hệ thống"
    },
    {
        "ten_vai_tro": "Admin cửa khẩu"
    },
    {
        "ten_vai_tro": "Admin doanh nghiệp"
    },
    {
        "ten_vai_tro": "Cán bộ cửa khẩu"
    },
    {
        "ten_vai_tro": "Nhân viên doanh nghiệp"
    }
]

for vai_tro in vai_tro_list:
    session.post(ENDPOINT + "danh-muc-vai-tro", data=json.dumps(vai_tro))
    print(f"Vai tro {vai_tro['ten_vai_tro']} da duoc tao")


# Payload danh muc hanh dong
danh_muc_hanh_dong_list = [
    {
        "ten_hanh_dong": "Đăng nhập"
    },
    {
        "ten_hanh_dong": "Đăng xuất"
    },
    {
        "ten_hanh_dong": "Đổi mật khẩu"
    },
    {
        "ten_hanh_dong": "Khóa tài khoản"
    },
    {
        "ten_hanh_dong": "Mở khóa tài khoản"
    },
    {
        "ten_hanh_dong": "Tạo tài khoản"
    },
    {
        "ten_hanh_dong": "Khôi phục mật khẩu"
    }
]

for danh_muc_hanh_dong in danh_muc_hanh_dong_list:
    session.post(ENDPOINT + "danh-muc-hanh-dong", data=json.dumps(danh_muc_hanh_dong))
    print(f"Danh muc hanh dong {danh_muc_hanh_dong['ten_hanh_dong']} da duoc tao")


# Payload trang thai to khai
trang_thai_to_khai_list = [
    {
        "ten_trang_thai": "Chờ thông quan"
    },
    {
        "ten_trang_thai": "Đăng ký thất bại"
    },
    {
        "ten_trang_thai": "Bị hủy"
    },
    {
        "ten_trang_thai": "Đã thông quan"
    }
]

for trang_thai_to_khai in trang_thai_to_khai_list:
    session.post(ENDPOINT + "trang-thai-to-khai", data=json.dumps(trang_thai_to_khai))
    print(f"Trang thai to khai {trang_thai_to_khai['ten_trang_thai']} da duoc tao")


# Payload trang thai phuong tien
trang_thai_phuong_tien_list = [
    {
        "ten_trang_thai": "Hợp lệ"
    },
    {
        "ten_trang_thai": "Không hợp lệ"
    }
]

for trang_thai_phuong_tien in trang_thai_phuong_tien_list:
    session.post(ENDPOINT + "danh-muc/trang-thai-phuong-tien", data=json.dumps(trang_thai_phuong_tien))
    print(f"Trang thai phuong tien {trang_thai_phuong_tien['ten_trang_thai']} da duoc tao")


# Payload to khai
to_khai_list = []
for i in range(1, 10000):
    don_vi_dang_ky = ""
    for nguoi_dung in nguoi_dung_list:
        if nguoi_dung["email"] == van_don_list[i]["nguoi_tao"]:
            don_vi_dang_ky = nguoi_dung["thuoc_don_vi"]
            break
    
    # thang = random.randint(1, 5)
    thang = random.choice([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 8, 9, 10, 11, 12])
    ngay = random.randint(1, 31)
    if ngay > 29 and thang == 2:
        ngay = 29
    if ngay == 31 and thang in [4, 6, 9, 11]:
        ngay = 30

    # if thang == 6 and ngay > :
    #     ngay = 29

    thang = str(thang)
    ngay = str(ngay)
    if int(thang) < 10:
        thang = '0' + thang
    if int(ngay) < 10:
        ngay = '0' + ngay
    ngay_dang_ky = f"2024-{thang}-{ngay}"

    to_khai = {
        "email": van_don_list[i]["nguoi_tao"],
        "don_vi_dang_ky": don_vi_dang_ky,
        "ma_van_don": i,
        "ngay_dang_ky": ngay_dang_ky
    }
    to_khai_list.append(to_khai)

for to_khai in to_khai_list:
    session.post(ENDPOINT + "to-khai", data=json.dumps(to_khai))
    print(f"To khai {to_khai['ma_van_don']} da duoc tao")

for i in range(1, len(van_don_list)-5):
    van_don_response = session.get(ENDPOINT + f"van-don/{i}")
    session.patch(ENDPOINT + f"to-khai/{i}/ngay-tao/{van_don_response.json()['ngay_tao_van_don']}")
    if session.get(ENDPOINT + f"to-khai/{i}").json()["ma_trang_thai"] == 1:
        session.patch(ENDPOINT + f"to-khai/{i}/trang-thai/{random.choice([1, 3, 3, 4, 4, 4, 4, 4, 4])}")
    print(f"Ngay tao cua to khai {i} da duoc cap nhat")


to_khai_list = []
for i in range(len(bien_so_list)):
    to_khai = {
        "email": van_don_list[len(van_don_list) - i - 1]["nguoi_tao"],
        "don_vi_dang_ky": van_don_list[len(van_don_list) - i - 1]["don_vi_xuat_khau"],
        "ma_van_don": len(van_don_list) - i,
        "ngay_dang_ky": datetime.now().strftime("%Y-%m-%d")
    }
    to_khai_list.append(to_khai)

for to_khai in to_khai_list:
    session.post(ENDPOINT + "to-khai", data=json.dumps(to_khai))
    print(f"To khai {to_khai['ma_van_don']} da duoc tao")
