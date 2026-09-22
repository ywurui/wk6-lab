import unittest

from duckFine import DuckFine


class TestDuckFine(unittest.TestCase):
    def test_member_id_is_stored(self):
        fine = DuckFine("member-001")
        self.assertEqual(fine.member_id, "member-001")

    def test_total_owed_starts_at_zero(self):
        fine = DuckFine("member-001")
        self.assertEqual(fine.total_owed, 0.0)

    def test_negative_days_late_raise_value_error(self):
        fine = DuckFine("member-001")
        with self.assertRaises(ValueError):
            fine.charge(-1)

    def test_grace_period_has_no_fee(self):
        fine = DuckFine("member-001")
        self.assertEqual(fine.charge(2), 0.0)

    def test_standard_fee_is_charged_after_grace_period(self):
        fine = DuckFine("member-001")
        self.assertEqual(fine.charge(3), 0.50)

    def test_deluxe_fee_is_double_standard_fee(self):
        fine = DuckFine("member-001")
        self.assertEqual(fine.charge(3, deluxe=True), 1.00)

    def test_fee_does_not_exceed_maximum(self):
        fine = DuckFine("member-001")
        self.assertEqual(fine.charge(20), 5.00)

    def test_deluxe_fee_also_does_not_exceed_maximum(self):
        fine = DuckFine("member-001")
        self.assertEqual(fine.charge(20, deluxe=True), 5.00)

    def test_charge_is_added_to_total_owed(self):
        fine = DuckFine("member-001")
        fine.charge(3)
        self.assertEqual(fine.total_owed, 0.50)

    def test_multiple_charges_accumulate(self):
        fine = DuckFine("member-001")
        fine.charge(3)
        fine.charge(4)
        self.assertEqual(fine.total_owed, 1.50)


if __name__ == "__main__":
    unittest.main()
