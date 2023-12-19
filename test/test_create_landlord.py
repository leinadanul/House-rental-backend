from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_landlord_registration():
    landloard_data ={
        "id": 2,
        "firstName": "pepe",
        "lastName": "jota",
        "email": "pepejota@m",
        "phoneNumber": 123456789,
        "mobileNumber": 987654321,
        "companyName": "Company",
        "picture": "picture.jpg",
    }
    response = client.post("/landlord_registred", json=landloard_data)
    assert response.status_code == 200
    assert response.json() == landloard_data







