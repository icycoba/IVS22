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
        self.assertEqual(calculator.getvalue(), 0)
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
        self.assertEqual(calculator.getvalue(), 0)
        self.assertEqual(calculator.add(calculator.add(20)), 40)
        self.assertEqual(calculator.add(calculator.add(0)), 80)
        self.assertEqual(calculator.add(calculator.add(-40)), 80)
        self.assertEqual(calculator.add(calculator.add(-80)), 0)

    def test_add_3(self):
        calculator = MathOperations(20)
        calculator2 = MathOperations(10)
        calculator3 = MathOperations("String")
        self.assertEqual(calculator.add(calculator2.getvalue()), 30)
        self.assertEqual(calculator2.add(calculator.getvalue()), 40)

    def test_sub_1(self):
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        self.assertEqual(calculator.sub(10), -10)
        self.assertEqual(calculator.sub(-20), 10)
        self.assertEqual(calculator.sub(9.78), 0.22)
        self.assertEqual(calculator.sub(-19.39), 19.61)
        self.assertEqual(calculator.sub(.5), 19.11)
        self.assertEqual(calculator.sub(-.5), 19.61)
        self.assertEqual(calculator.sub(-5e3), 5019.61)
        self.assertEqual(calculator.sub(5e3), 19.61)
        self.assertEqual(calculator.sub(0), 19.61)
        self.assertEqual(calculator.sub(-0), 19.61)

    def test_mul_1(self):
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        self.assertEqual(calculator.mul(10), 0)
        self.assertEqual(calculator.mul(-20), 0)
        self.assertEqual(calculator.mul(9.78), 0)
        self.assertEqual(calculator.mul(-19.39), 0)
        self.assertEqual(calculator.mul(.5), 0)
        self.assertEqual(calculator.mul(-.5), 0)
        self.assertEqual(calculator.mul(-5e3), 0)
        self.assertEqual(calculator.mul(5e3), 0)
        self.assertEqual(calculator.mul(0), 0)
        self.assertEqual(calculator.mul(-0), 0)

    def test_mul_2(self):
        calculator = MathOperations(1)
        self.assertEqual(calculator.getvalue(), 1)
        self.assertEqual(calculator.mul(10), 10)
        self.assertEqual(calculator.mul(-20), -200)
        self.assertEqual(calculator.mul(9.78), -1956)
        self.assertEqual(calculator.mul(-19.5), 38142)
        self.assertEqual(calculator.mul(.5), 19071)
        self.assertEqual(calculator.mul(-.5), -9535.5)
        self.assertEqual(calculator.mul(-1e-3), 9.5355)
        self.assertEqual(calculator.mul(1e4), 95355)
        self.assertEqual(calculator.mul(0), 0)
        self.assertEqual(calculator.mul(-0), 0)

    def test_div_1(self):
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        self.assertEqual(calculator.div(10), 0)
        self.assertEqual(calculator.div(-20), 0)
        self.assertEqual(calculator.div(9.78), 0)
        self.assertEqual(calculator.div(-19.39), 0)
        self.assertEqual(calculator.div(.5), 0)
        self.assertEqual(calculator.div(-.5), 0)
        self.assertEqual(calculator.div(-5e3), 0)
        self.assertEqual(calculator.div(5e3), 0)
        self.assertRaises(calculator.div(0), ZeroDivisionError)
        self.assertRaises(calculator.div(-0), ZeroDivisionError)

    def test_factorial_1(self):
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        self.assertEqual(calculator.factorial(), 1)

    def test_factorial_2(self):
        calculator = MathOperations(1)
        self.assertEqual(calculator.getvalue(), 1)
        self.assertEqual(calculator.factorial(), 1)

    def test_factorial_3(self):
        calculator = MathOperations(10)
        self.assertEqual(calculator.getvalue(), 10)
        self.assertEqual(calculator.factorial(), 3628800)

    def test_factorial_4(self):
        calculator = MathOperations(20)
        self.assertEqual(calculator.getvalue(), 20)
        self.assertEqual(calculator.factorial(), 2432902008176640000)

    def test_factorial_5(self):
        calculator = MathOperations(-10)
        self.assertEqual(calculator.getvalue(), -10)
        self.assertRaises(calculator.factorial(), ValueError)

    def test_factorial_6(self):
        calculator = MathOperations(5.28)
        self.assertEqual(calculator.getvalue(), 5.28)
        self.assertRaises(calculator.factorial(), ValueError)

    def test_pow_1(self):
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        self.assertEqual(calculator.pow(10), 0)
        self.assertEqual(calculator.pow(-20), 0)
        self.assertEqual(calculator.pow(9.78), 0)
        self.assertEqual(calculator.pow(-19.39), 0)
        self.assertEqual(calculator.pow(.5), 0)
        self.assertEqual(calculator.pow(-.5), 0)
        self.assertEqual(calculator.pow(-5e3), 0)
        self.assertEqual(calculator.pow(5e3), 0)
        self.assertEqual(calculator.pow(0), 0)
        self.assertEqual(calculator.pow(-0), 0)

    def test_sqrt_1(self):
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        self.assertEqual(calculator.sqrt(10), 0)
        self.assertEqual(calculator.sqrt(-20), 0)
        self.assertEqual(calculator.sqrt(9.78), 0)
        self.assertEqual(calculator.sqrt(-19.39), 0)
        self.assertEqual(calculator.sqrt(.5), 0)
        self.assertEqual(calculator.sqrt(-.5), 0)
        self.assertEqual(calculator.sqrt(-5e3), 0)
        self.assertEqual(calculator.sqrt(5e3), 0)
        self.assertEqual(calculator.sqrt(0), 0)
        self.assertEqual(calculator.sqrt(-0), 0)


class TestAdvancedMathOperations(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
