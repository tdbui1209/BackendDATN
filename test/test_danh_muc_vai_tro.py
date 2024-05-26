import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_create_vai_tro():
    response = client.post(
        "/api/danh-muc-vai-tro",
        json={"ten_vai_tro": "Vai trò 1"}
    )
    assert response.status_code == 201
    assert response.json() == {"ma_vai_tro": 1, "ten_vai_tro": "Vai trò 1"}

def test_create_vai_tro_duplicate():
    response = client.post(
        "/api/danh-muc-vai-tro",
        json={"ten_vai_tro": "Vai trò 1"}
    )
    assert response.status_code == 409
    assert response.json() == {"detail": "Tên vai trò đã tồn tại"}

def test_read_vai_tro():
    response = client.get("/api/danh-muc-vai-tro")
    assert response.status_code == 200
    assert response.json() == [{"ma_vai_tro": 1, "ten_vai_tro": "Vai trò 1"}]

def test_read_vai_tro_by_ma_vai_tro():
    response = client.get("/api/danh-muc-vai-tro/1")
    assert response.status_code == 200
    assert response.json() == {"ma_vai_tro": 1, "ten_vai_tro": "Vai trò 1"}

def test_read_vai_tro_by_ma_vai_tro_not_found():
    response = client.get("/api/danh-muc-vai-tro/2")
    assert response.status_code == 404
    assert response.json() == {"detail": "Vai trò không tồn tại"}

def test_update_vai_tro_by_ma_vai_tro():
    response = client.patch(
        "/api/danh-muc-vai-tro/1",
        json={"ten_vai_tro": "Vai trò 2"}
    )
    assert response.status_code == 200
    assert response.json() == {"ma_vai_tro": 1, "ten_vai_tro": "Vai trò 2"}

def test_update_vai_tro_by_ma_vai_tro_not_found():
    response = client.patch(
        "/api/danh-muc-vai-tro/2",
        json={"ten_vai_tro": "Vai trò 2"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Vai trò không tồn tại"}

def test_read_vai_tro_search():
    response = client.get("/api/danh-muc-vai-tro?search_string=Vai trò 2")
    assert response.status_code == 200
    assert response.json() == [{"ma_vai_tro": 1, "ten_vai_tro": "Vai trò 2"}]

def test_read_vai_tro_search_not_found():
    response = client.get("/api/danh-muc-vai-tro?search_string=Vai trò 3")
    assert response.status_code == 404
    assert response.json() == {"detail": "Không tìm thấy vai trò nào"}
