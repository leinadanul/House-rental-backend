import unittest
from unittest.mock import MagicMock
from services.landlord_services import LandlordServices
from models.landlord import Landlord


class TestLandlordService(unittest.TestCase):
    def setUp(self):
        self.mock_data_manager = MagicMock()
        self.landlord_service = LandlordServices(self.mock_data_manager)

    def test_landlord_added_successfully_to_database(self):
        new_landlord = Landlord(
            first_name="Peter",
            last_name="Eel",
            email="peter@theeel.com",
            phone_number=1234,
            mobile_number=567,
            company_name="Eel factory",
            picture="picture",
        )

        new_landlord_2 = Landlord(
            id=1,
            first_name="Peter",
            last_name="Eel",
            email="peter@theeel.com",
            phone_number=1234,
            mobile_number=567,
            company_name="Eel factory",
            picture="picture",
        )

        self.mock_data_manager.insert_landlord.return_value = new_landlord_2
        response = self.landlord_service.create_landlord(new_landlord)
        self.assertEqual(response, new_landlord_2)
        self.mock_data_manager.insert_landlord.assert_called_once_with(new_landlord)

    def test_landlord_store_when_database_connection_is_down(self):
        new_landlord = Landlord(
            id=1,
            first_name="Peter",
            last_name="Eel",
            email="peter@theeel.com",
            phone_number=1234,
            mobile_number=567,
            company_name="Eel factory",
            picture="picture",
        )

        self.mock_data_manager.insert_landlord.side_effect = Exception("Test")
        with self.assertRaises(Exception):
            self.landlord_service.create_landlord(new_landlord)
        self.mock_data_manager.insert_landlord.assert_called_once_with(new_landlord)
