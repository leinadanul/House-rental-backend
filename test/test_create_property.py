import unittest
from  unittest.mock import MagicMock
from services.property_services import PropertyService
from models.property import Property

class TestPropertyServices(unittest.TestCase):
    def setUp(self):
        self.mock_data_manager = MagicMock()
        self.property_service = PropertyService(self.mock_data_manager)


    def test_property_added_successfully_to_database(self):
        new_property = Property(
            name="Lemuel",
            country="Tierra caliente",
            state="Rie",
            city="Serpiente",
            address="AV tierra caliente",
            capacity=12,
            unavailable_days="available",
            description="crema dental",
            price=89.000,
            host={
                "id": 1,
                "name": "Lorenzo",
                "phone_number": 2112333,
                "email": "mail@mail"
            },
            landlord_id=2,
            fees=[
                {
                    "id": 2,
                    "name": "Taxes",
                    "description": "Your money",
                    "price": 199
                }
            ],
            features=[
                {
                    "id": 1,
                    "name": "Kitchen",
                    "icon": "MicrowaveIcon"
                }
            ],
            distributions=[
                {
                    "id": 1,
                    "name": "Bed",
                    "description": "Single bed",
                    "quantity": 2
                }
            ],
            property_type={
                "id": 10,
                "name": "House",
                "description": "Crazy house"
            }
        )

        new_property_2 = Property(
            id= 1,
            name="Lemuel",
            country="Tierra caliente",
            state="Rie",
            city="Serpiente",
            address="AV tierra caliente",
            capacity=12,
            unavailable_days="available",
            description="crema dental",
            price=89.000,
            host={
                "id": 1,
                "name": "Lorenzo",
                "phone_number": 2112333,
                "email": "mail@mail"
            },
            landlord_id=2,
            fees=[
                {
                    "id": 2,
                    "name": "Taxes",
                    "description": "Your money",
                    "price": 199
                }
            ],
            features=[
                {
                    "id": 1,
                    "name": "Kitchen",
                    "icon": "MicrowaveIcon"
                }
            ],
            distributions=[
                {
                    "id": 1,
                    "name": "Bed",
                    "description": "Single bed",
                    "quantity": 2
                }
            ],
            property_type={
                "id": 10,
                "name": "House",
                "description": "Crazy house"
            }
        )

        self.mock_data_manager.add_property.return_value = new_property_2
        response = self.property_service.add_property(new_property)
        self.assertEqual(response, new_property_2)
        self.mock_data_manager.add_property.assert_called_once_with(new_property)

    def test_property_store_when_database_connection_is_down(self):
        new_property = Property(
            id= 1,
            name="Lemuel",
            country="Tierra caliente",
            state="Rie",
            city="Serpiente",
            address="AV tierra caliente",
            capacity=12,
            unavailable_days="available",
            description="crema dental",
            price=89.000,
            host={
                "id": 1,
                "name": "Lorenzo",
                "phone_number": 2112333,
                "email": "mail@mail"
            },
            landlord_id=2,
            fees=[
                {
                    "id": 2,
                    "name": "Taxes",
                    "description": "Your money",
                    "price": 199
                }
            ],
            features=[
                {
                    "id": 1,
                    "name": "Kitchen",
                    "icon": "MicrowaveIcon"
                }
            ],
            distributions=[
                {
                    "id": 1,
                    "name": "Bed",
                    "description": "Single bed",
                    "quantity": 2
                }
            ],
            property_type={
                "id": 10,
                "name": "House",
                "description": "Crazy house"
            }
        )

        self.mock_data_manager.add_property.side_effect = Exception ("Test")
        with self.assertRaises(Exception):
            self.property_service.add_property(new_property)
        self.mock_data_manager.add_property.assert_called_once_with(new_property)
