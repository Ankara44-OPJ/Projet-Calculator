

import unittest
from Expression import evaluer_expression


class TestExpressions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(
            evaluer_expression("2+3"), 5
        )

    def test_priorite(self):
        self.assertEqual(
            evaluer_expression("2+3*4"), 14
        )

    def test_parentheses(self):
        self.assertEqual(
            evaluer_expression("(2+3)*4"), 20
        )

    def test_puissance(self):
        self.assertEqual(
           evaluer_expression("2^3"), 8
        )

    def test_decimales(self):
        self.assertEqual(
            evaluer_expression("2.5*4"), 10
        )

    def test_division_zero(self):
        with self.assertRaises(ValueError):
            evaluer_expression("10 / 0")

    def test_expression_vide(self):
        with self.assertRaises(ValueError):
            evaluer_expression("")

    def test_expression_invalide(self):
        with self.assertRaises(ValueError):
           evaluer_expression("2 +")

    def test_parentheses_invalides(self):
        with self.assertRaises(ValueError):
            evaluer_expression("(2 + 3")

if __name__ == "__main__":
    unittest.main()
