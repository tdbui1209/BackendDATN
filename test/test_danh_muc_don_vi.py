import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_create_danh_muc_don_vi():
    response = client.post(
        "/api/danh-muc-don-vi",
        json={"ma_danh_muc_don_vi": "DV1", "ten_danh_muc_don_vi": "Đơn vị 1"}
    )
    assert response.status_code == 201
    assert response.json() == {"ma_danh_muc_don_vi": "DV1", "ten_danh_muc_don_vi": "Đơn vị 1"}

def test_create_danh_muc_don_vi_duplicate():
    response = client.post(
        "/api/danh-muc-don-vi",
        json={"ma_danh_muc_don_vi": "DV1", "ten_danh_muc_don_vi": "Đơn vị 1"}
    )
    assert response.status_code == 409
    assert response.json() == {"detail": "Tên đơn vị đã tồn tại"}

def test_read_danh_muc_don_vi():
    response = client.get("/api/danh-muc-don-vi")
    assert response.status_code == 200
    assert response.json() == [{"ma_danh_muc_don_vi": "DV1", "ten_danh_muc_don_vi": "Đơn vị 1"}]

def test_read_danh_muc_don_vi_by_ma_danh_muc_don_vi():
    response = client.get("/api/danh-muc-don-vi/DV1")
    assert response.status_code == 200
    assert response.json() == {"ma_danh_muc_don_vi": "DV1", "ten_danh_muc_don_vi": "Đơn vị 1"}

def test_read_danh_muc_don_vi_by_ma_danh_muc_don_vi_not_found():
    response = client.get("/api/danh-muc-don-vi/DV2")
    assert response.status_code == 404
    assert response.json() == {"detail": "Danh mục đơn vị không tồn tại"}

def test_update_danh_muc_don_vi_by_ma_danh_muc_don_vi():
    response = client.patch(
        "/api/danh-muc-don-vi",
        json={"ma_danh_muc_don_vi": "DV1", "ten_danh_muc_don_vi": "Đơn vị 2"}
    )
    assert response.status_code == 200
    assert response.json() == {"ma_danh_muc_don_vi": "DV1", "ten_danh_muc_don_vi": "Đơn vị 2"}

def test_update_danh_muc_don_vi_by_ma_danh_muc_don_vi_not_found():
    response = client.patch(
        "/api/danh-muc-don-vi",
        json={"ma_danh_muc_don_vi": "DV2", "ten_danh_muc_don_vi": "Đơn vị 2"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Danh mục đơn vị không tồn tại"}

def test_read_danh_muc_don_vi_search():
    response = client.get("/api/danh-muc-don-vi?search_string=Đơn vị 2")
    assert response.status_code == 200
    assert response.json() == [{"ma_danh_muc_don_vi": "DV1", "ten_danh_muc_don_vi": "Đơn vị 2"}]

# def test_delete_danh_muc_don_vi_by_ma_danh_muc_don_vi():
#     response = client.delete("/api/danh-muc-don-vi/DV1")
#     assert response.status_code == 204

def test_delete_danh_muc_don_vi_by_ma_danh_muc_don_vi_not_found():
    response = client.delete("/api/danh-muc-don-vi/DV1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Danh mục đơn vị không tồn tại"}

