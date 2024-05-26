import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_nguoi_dung():
    response = client.post("/api/nguoi-dung", json={
        "email": "test@test.com",
        "ho_va_ten": "Test",
        "so_dien_thoai": "0123456789",
        "thuoc_don_vi": "CK1",
        "ma_vai_tro": 1,
        "mat_khau": "test"
    })
    assert response.status_code == 201
    assert response.json() == {
        "email": "test@test.com",
        "ho_va_ten": "Test",
        "so_dien_thoai": "0123456789",
        "thuoc_don_vi": "CK1",
        "ma_vai_tro": 1,
        "dang_hoat_dong": True,
        "vai_tro": {
            "ma_vai_tro": 1,
            "ten_vai_tro": "Vai trò 2"
        }
    }

def test_create_nguoi_dung_duplicate():
    response = client.post("/api/nguoi-dung", json={
        "email": "test@test.com",
        "ho_va_ten": "Test",
        "so_dien_thoai": "0123456789",
        "thuoc_don_vi": "CK1",
        "ma_vai_tro": 1,
        "mat_khau": "test",
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Email đã tồn tại"}

def test_read_nguoi_dung():
    response = client.get("/api/nguoi-dung")
    assert response.status_code == 200
    assert response.json() == [{
        "email": "test@test.com",
        "ho_va_ten": "Test",
        "so_dien_thoai": "0123456789",
        "thuoc_don_vi": "CK1",
        "ma_vai_tro": 1,
        "dang_hoat_dong": True,
        "vai_tro": {
            "ma_vai_tro": 1,
            "ten_vai_tro": "Vai trò 2"
        }
    }]

def test_read_nguoi_dung_by_email():
    response = client.get("/api/nguoi-dung/test@test.com")
    assert response.status_code == 200
    assert response.json() == {
        "email": "test@test.com",
        "ho_va_ten": "Test",
        "so_dien_thoai": "0123456789",
        "thuoc_don_vi": "CK1",
        "ma_vai_tro": 1,
        "dang_hoat_dong": True,
        "vai_tro": {
            "ma_vai_tro": 1,
            "ten_vai_tro": "Vai trò 2"
        }
    }

def test_read_nguoi_dung_by_email_not_found():
    response = client.get("/api/nguoi-dung/test1@test.com")
    assert response.status_code == 404
    assert response.json() == {"detail": "Không tìm thấy người dùng"}

def test_read_nguoi_dung_role():
    response = client.get("/api/nguoi-dung/test@test.com/vai-tro")
    assert response.status_code == 200
    assert response.json() == 1

def test_update_nguoi_dung_by_email():
    response = client.put("/api/nguoi-dung/test@test.com", json={
        "email": "test@test.com",
        "ho_va_ten": "Test 2",
        "so_dien_thoai": "0123456789",
        "thuoc_don_vi": "CK1",
        "ma_vai_tro": 1
    })
    assert response.status_code == 200
    assert response.json() == {
        "email": "test@test.com",
        "ho_va_ten": "Test 2",
        "so_dien_thoai": "0123456789",
        "thuoc_don_vi": "CK1",
        "ma_vai_tro": 1,
        "dang_hoat_dong": True,
        "vai_tro": {
            "ma_vai_tro": 1,
            "ten_vai_tro": "Vai trò 2"
        }
    }

def test_update_nguoi_dung_by_email_not_found():
    response = client.put("/api/nguoi-dung/test1@test.com", json={
        "email": "test@test.com",
        "ho_va_ten": "Test 2",
        "so_dien_thoai": "0123456789",
        "thuoc_don_vi": "CK1",
        "ma_vai_tro": 1,
        "dang_hoat_dong": True,
        "vai_tro": {
            "ma_vai_tro": 1,
            "ten_vai_tro": "Vai trò 2"
        }
    })
    assert response.status_code == 404
    assert response.json() == {"detail": "Không tìm thấy người dùng"}
