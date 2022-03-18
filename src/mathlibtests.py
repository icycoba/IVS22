"""
Soubor:     mathlibtests.py
Autor:      Martin Hlinský  (xhlins01)
            Petra Dudová    (xdudov02)
Projekt:    IVS #2 - Tvorba kalkulačky
Popis:      Testy pro tvorbu matematické knihovny
"""


from mathlib import MathOperations
import unittest


class TestBasicMathOperations(unittest.TestCase):
    def test_add_1(self):
        calculator = MathOperations()
        self.assertEqual(calculator.add(9.21), 9.21)
        self.assertEqual(calculator.add(0.79), 10)
        self.assertEqual(calculator.add(.5), 10.5)
        self.assertEqual(calculator.add(-.5), 10)
        self.assertEqual(calculator.add(2e2), 210)
        self.assertEqual(calculator.add(-2e2), 10)
        self.assertEqual(calculator.add(0), 10)
        self.assertEqual(calculator.add(-0), 10)

    def test_add_2(self):
        calculator = MathOperations()
        self.assertEqual(calculator.add(calculator.add(20)), 40)
        self.assertEqual(calculator.add(calculator.add(0)), 80)
        self.assertEqual(calculator.add(calculator.add(-40)), 80)
        self.assertEqual(calculator.add(calculator.add(-80)), 0)


if __name__ == "__main__":
    unittest.main()
