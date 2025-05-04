import unittest
from unittest.mock import patch, MagicMock
from hotel import (
    HotelManager, StandardRoom, SuiteRoom, Guest,
    RoomUnavailableError, RoomNotFoundError, DuplicateRoomError
)


class TestHotelManager(unittest.TestCase):

    def setUp(self):
        self.hotel = HotelManager()
        self.standard_room = StandardRoom(101)
        self.suite_room = SuiteRoom(201)
        self.hotel.add_room(self.standard_room)
        self.hotel.add_room(self.suite_room)

    def create_guest_and_check_in(self, guest_name: str, room_type):
        guest = Guest(guest_name)
        room = self.hotel.check_in_guest(guest, room_type)
        return guest, room

    def test_add_duplicate_room_raises_error(self):
        with self.assertRaises(DuplicateRoomError):
            self.hotel.add_room(StandardRoom(101))

    def test_check_in_guest_to_standard_room(self):
        guest, room = self.create_guest_and_check_in("John", StandardRoom)
        self.assertTrue(room.is_occupied())
        self.assertEqual(room.guest.name, "John")

    def test_check_in_guest_no_available_room(self):
        self.create_guest_and_check_in("John", StandardRoom)
        with self.assertRaises(RoomUnavailableError):
            self.hotel.check_in_guest(Guest("Jane"), StandardRoom)

    def test_check_out_guest_successful(self):
        _, room = self.create_guest_and_check_in("John", SuiteRoom)
        self.hotel.check_out_guest(room.room_number)
        self.assertFalse(room.is_occupied())

    def test_check_out_guest_invalid_room(self):
        with self.assertRaises(RoomNotFoundError):
            self.hotel.check_out_guest(999)

    def test_provide_room_service_success(self):
        _, room = self.create_guest_and_check_in("John", SuiteRoom)
        message = self.hotel.provide_room_service(room.room_number)
        self.assertEqual(message, "Room service has been provided.")

    def test_provide_food_service_success(self):
        _, room = self.create_guest_and_check_in("John", StandardRoom)
        message = self.hotel.provide_food(room.room_number, "pizza")
        self.assertEqual(message, "Food service has been provided with pizza.")

    def test_provide_service_to_empty_room_fails(self):
        # Ensure the room is unoccupied before providing service
        self.hotel.check_out_guest(self.standard_room.room_number)
        with self.assertRaises(RoomNotFoundError):
            self.hotel.provide_room_service(self.standard_room.room_number)

    @patch("hotel.Service")
    def test_mocked_service_called(self, MockService):
        _, room = self.create_guest_and_check_in("John", StandardRoom)
        mock_service = MockService()
        mock_service.provide_service.return_value = "Mocked service called."
        result = self.hotel.service_manager.provide_service(room.room_number, mock_service)

        mock_service.provide_service.assert_called_once()
        self.assertEqual(result, "Mocked service called.")

    def test_provide_service_with_magicmock(self):
        _, room = self.create_guest_and_check_in("John", SuiteRoom)
        mock_service = MagicMock()
        mock_service.provide_service.return_value = "MagicMock service used."

        result = self.hotel.service_manager.provide_service(room.room_number, mock_service)

        mock_service.provide_service.assert_called_once()
        self.assertEqual(result, "MagicMock service used.")


if __name__ == '__main__':
    unittest.main()