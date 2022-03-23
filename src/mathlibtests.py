"""
Soubor:     mathlibtests.py
Autor:      Martin Hlinský  (xhlins01)
            Petra Dudová    (xdudov02)
Projekt:    IVS #2 - Tvorba kalkulačky
Popis:      Testy pro tvorbu matematické knihovny
"""


from mathlib import MathOperations
import unittest

validkeys = [1, -1, 3.5, -6.2, 2e5, -6e7, 2e-3, 0, -0, 1+1, 3-5, 1*5, 52/5]
validkeysdiv = [1, -1, 3.5, -6.2, 2e5, -6e7, 2e-3, 1+1, 3-5, 1*5, 52/5]
invalidkeys = ['1', '-1', '0', 'asd', '10asd', True, False, [1, 3, 5], (3, 4, 5), {1, 3, 5}, {"number": 1, "next": 4}]
invalidkeys2 = [3j, range(6), frozenset({1, 3, 5}), b"byteString", bytearray(5), memoryview(bytes(5))]


class TestBasicMathOperations(unittest.TestCase):
    def test_init_1(self):
        MathOperations()
        for key in validkeys:
            MathOperations(key)

    def test_init_2(self):
        for key in invalidkeys:
            MathOperations(key)

    def test_init_3(self):
        for key in invalidkeys2:
            MathOperations(key)

    def test_add_1(self):
        results = [0] * len(validkeys)
        for i, _ in enumerate(validkeys):
            if i == 0:
                results[i] += validkeys[i]
            else:
                results[i] = results[i-1] + validkeys[i]
        zippedkeys = zip(validkeys, results)
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        for key, result in zippedkeys:
            self.assertEqual(calculator.add(key), result)

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
        self.assertEqual(calculator.add(calculator2.getvalue()), 30)
        self.assertEqual(calculator2.add(calculator.getvalue()), 40)

    def test_sub_1(self):
        results = [0] * len(validkeys)
        for i, _ in enumerate(validkeys):
            if i == 0:
                results[i] -= validkeys[i]
            else:
                results[i] = results[i-1] - validkeys[i]
        zippedkeys = zip(validkeys, results)
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        for key, result in zippedkeys:
            self.assertEqual(calculator.sub(key), result)

    def test_mul_1(self):
        results = [0] * len(validkeys)
        zippedkeys = zip(validkeys, results)
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        for key, result in zippedkeys:
            self.assertEqual(calculator.mul(key), result)

    def test_mul_2(self):
        results = [1] * len(validkeys)
        for i, _ in enumerate(validkeys):
            if i == 0:
                results[i] *= validkeys[i]
            else:
                results[i] = results[i-1] * validkeys[i]
        zippedkeys = zip(validkeys, results)
        calculator = MathOperations(1)
        self.assertEqual(calculator.getvalue(), 1)
        for key, result in zippedkeys:
            self.assertEqual(calculator.mul(key), result)

    def test_mul_3(self):
        results = [1] * 4
        restofkeys = validkeys[-4:]
        for i, _ in enumerate(restofkeys):
            if i == 0:
                results[i] *= restofkeys[i]
            else:
                results[i] = results[i-1] * restofkeys[i]
        zippedkeys = zip(validkeys, results)
        calculator = MathOperations(1)
        self.assertEqual(calculator.getvalue(), 1)
        for key, result in zippedkeys:
            self.assertEqual(calculator.mul(key), result)

    def test_div_1(self):
        results = [0] * len(validkeys)
        zippedkeys = zip(validkeys, results)
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        for key, result in zippedkeys:
            if key == 0:
                self.assertRaises(calculator.div(key), ZeroDivisionError)
            else:
                self.assertEqual(calculator.div(key), result)

    def test_div_2(self):
        results = [1] * len(validkeysdiv)
        for i, _ in enumerate(validkeysdiv):
            if i == 0:
                results[i] /= validkeysdiv[i]
            else:
                results[i] = results[i-1] / validkeysdiv[i]
        zippedkeys = zip(validkeysdiv, results)
        calculator = MathOperations(1)
        self.assertEqual(calculator.getvalue(), 1)
        for key, result in zippedkeys:
            if key == 0:
                self.assertRaises(calculator.div(key), ZeroDivisionError)
            else:
                self.assertEqual(calculator.div(key), result)
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
        results = [0] * len(validkeys)
        zippedkeys = zip(validkeys, results)
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        for key, result in zippedkeys:
            self.assertEqual(calculator.pow(key), result)

    def test_pow_2(self):
        results = [2] * len(validkeys)
        for i, _ in enumerate(validkeys):
            if i == 0:
                results[i] = results[i] ** validkeys[i]
            else:
                results[i] = results[i-1] ** validkeys[i]
        zippedkeys = zip(validkeys, results)
        calculator = MathOperations(2)
        self.assertEqual(calculator.getvalue(), 2)
        for key, result in zippedkeys:
            self.assertEqual(calculator.pow(key), result)

    def test_sqrt_1(self):
        results = [0] * len(validkeys)
        zippedkeys = zip(validkeys, results)
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        for key, result in zippedkeys:
            self.assertEqual(calculator.sqrt(key), result)

    def test_sqrt_2(self):
        results = [2] * len(validkeysdiv)
        for i, _ in enumerate(validkeysdiv):
            if i == 0:
                results[i] = results[i] ** (1 / validkeysdiv[i])
            else:
                results[i] = results[i-1] ** (1 / validkeysdiv[i])
        zippedkeys = zip(validkeysdiv, results)
        calculator = MathOperations(2)
        self.assertEqual(calculator.getvalue(), 2)
        for key, result in zippedkeys:
            self.assertEqual(calculator.sqrt(key), result)
        self.assertRaises(calculator.sqrt(0), ZeroDivisionError)


class TestAdvancedMathOperations(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
