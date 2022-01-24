import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Ozzy", "Osbourne", 100)

    def test_guest_has_f_name(self):
        self.assertEqual("Ozzy", self.guest.f_name)

    def test_guest_has_l_name(self):
        self.assertEqual("Osbourne", self.guest.l_name)

    def test_guest_has_wallet(self):
        self.assertEqual(100, self.guest.wallet)

    def test_pay_to_check(self):
        self.guest.pay_to_check_in(10)
        self.assertEqual(90, self.guest.wallet)