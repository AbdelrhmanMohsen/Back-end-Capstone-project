from django.test import TestCase
from restaurant.models import Menu, Booking
from decimal import Decimal
from datetime import datetime


class MenuTest(TestCase):

    def test_create_item(self):
        item = Menu.objects.create(title="Ice Cream", price=Decimal('800'), inventory=100)
        self.assertEqual(str(item), "Ice Cream : 800")

    def test_default_inventory(self):
        item = Menu.objects.create(title="Cheese Cake", price=Decimal('500'))
        self.assertEqual(item.inventory, 1)


class BookingTest(TestCase):

    def test_create_booking(self):
        booking = Booking.objects.create(
            name="Abdelrhman Mohsen",
            number_of_guests=9,
            booking_date=datetime(2024, 8, 24, 18, 0)
        )
        expected_str = "Abdelrhman Mohsen for 9 guests on 2024-08-24 18:00:00"
        self.assertEqual(str(booking), expected_str)

    def test_default_number_of_guests(self):
        booking = Booking.objects.create(
            name="Abdelrhman Mohsen",
            booking_date=datetime(2024, 11, 24, 19, 0)
        )
        self.assertEqual(booking.number_of_guests, 6)
