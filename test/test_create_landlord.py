from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_create_landlord_registration(self):
    landlord_data ={
        "id":               2,
        "first_name":        "pepe",
        "lastName":         "jota",
        "email":            "pepejota@m",
        "phoneNumber":      123456789,
        "mobileNumber":     987654321,
        "companyName":      "Company",
        "picture": "        picture.jpg",
    }
    response = self.client.post("/landlord", json=landlord_data)
    assert response.status_code == 200
    assert response.json() == landlord_data







