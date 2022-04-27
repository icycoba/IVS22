"""
Soubor:     mathlibtests.py
Autor:      Martin Hlinský  (xhlins01)
            Petra Dudová    (xdudov02)
Projekt:    IVS #2 - Tvorba kalkulačky
Popis:      Testy pro tvorbu matematické knihovny
"""


from expression_to_num import MathOperations, MathSolver
import unittest

validkeys = [1, -1, 3.5, -6.2, 2e5, -6e7, 2e-3, 0, -0, 1+1, 3-5, 1*5, 52/5]
validkeysdiv = [1, -1, 3.5, -6.2, 2e5, -6e7, 2e-3, 1+1, 3-5, 1*5, 52/5]
validkeyspow = [1, 5-3, 3, 4, 5, -3+6, 7, 8, 9, 10, 100, 0, 5]
invalidkeyspow = [1.1, -1, -5.5, 13/3, 4/2, 1/2, 0.00001]
invalidkeys = ['1', '-1', '0', 'asd', '10asd', True, False, [1, 3, 5], (3, 4, 5), {1, 3, 5}, {"number": 1, "next": 4}]
invalidkeys2 = [3j, range(6), frozenset({1, 3, 5}), b"byteString", bytearray(5), memoryview(bytes(5))]


class TestBasicMathOperations(unittest.TestCase):
    def test_init_1(self):
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        for key in validkeys:
            calculator = MathOperations(key)
            self.assertEqual(calculator.getvalue(), key)

    def test_init_2(self):
        for key in invalidkeys:
            with self.assertRaises(TypeError):
                MathOperations(key)

    def test_init_3(self):
        for key in invalidkeys2:
            with self.assertRaises(TypeError):
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
        zippedkeys = zip(restofkeys, results)
        calculator = MathOperations(1)
        self.assertEqual(calculator.getvalue(), 1)
        for key, result in zippedkeys:
            self.assertEqual(calculator.mul(key), result)

    def test_mul_4(self):
        calculator = MathOperations(5)
        with self.assertRaises(TypeError):
            calculator.mul('abc')

    def test_div_1(self):
        results = [0] * len(validkeys)
        zippedkeys = zip(validkeys, results)
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        for key, result in zippedkeys:
            if key == 0:
                with self.assertRaises(ZeroDivisionError):
                    calculator.div(key)
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
                with self.assertRaises(ZeroDivisionError):
                    calculator.div(key)
            else:
                self.assertEqual(calculator.div(key), result)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(-0)

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
        with self.assertRaises(ValueError):
            calculator.factorial()

    def test_factorial_6(self):
        calculator = MathOperations(5.28)
        self.assertEqual(calculator.getvalue(), 5.28)
        with self.assertRaises(ValueError):
            calculator.factorial()

    def test_pow_1(self):
        results = [0] * len(validkeyspow)
        for i, _ in enumerate(validkeyspow):
            if i == 0:
                results[i] = results[i] ** validkeyspow[i]
            else:
                results[i] = results[i-1] ** validkeyspow[i]
        zippedkeys = zip(validkeyspow, results)
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        for key, result in zippedkeys:
            self.assertEqual(calculator.pow(key), result)

    def test_pow_2(self):
        results = [2] * len(validkeyspow)
        for i, _ in enumerate(validkeyspow):
            if i == 0:
                results[i] = results[i] ** validkeyspow[i]
            else:
                results[i] = results[i-1] ** validkeyspow[i]
        zippedkeys = zip(validkeyspow, results)
        calculator = MathOperations(2)
        self.assertEqual(calculator.getvalue(), 2)
        for key, result in zippedkeys:
            self.assertEqual(calculator.pow(key), result)

    def test_pow_3(self):
        calculator = MathOperations()
        for key in invalidkeyspow:
            with self.assertRaises(ValueError):
                calculator.pow(key)

    def test_root_1(self):
        results = [0] * len(validkeys)
        zippedkeys = zip(validkeys, results)
        calculator = MathOperations()
        self.assertEqual(calculator.getvalue(), 0)
        for key, result in zippedkeys:
            self.assertEqual(calculator.root(key), result)

    def test_root_2(self):
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
            self.assertEqual(calculator.root(key), result)
        with self.assertRaises(ZeroDivisionError):
            calculator.root(0)


class TestAdvancedMathOperations(unittest.TestCase):
    pass


class TestStringExpressionsMathOperations(unittest.TestCase):
    def test_string_expression_1(self):
        calculator = MathSolver()
        self.assertEqual(float(calculator.solve("1+1")), 2)
        self.assertEqual(float(calculator.solve("3-1")), 2)
        self.assertEqual(float(calculator.solve("4/2")), 2)
        self.assertEqual(float(calculator.solve("2*1")), 2)

    def test_string_expression_2(self):
        calculator = MathSolver()
        self.assertEqual(float(calculator.solve("1+(-3)")), -2)
        self.assertEqual(float(calculator.solve("4-(-5)")), 9)
        self.assertEqual(float(calculator.solve("32/(8/4)")), 16)
        self.assertEqual(float(calculator.solve("(32/8)/4")), 1)
        self.assertEqual(float(calculator.solve("1*2*4*8")), 64)

    def test_string_expression_3(self):
        calculator = MathSolver()
        self.assertEqual(float(calculator.solve("root(4,2)")), 2)
        self.assertEqual(float(calculator.solve("fact(7)")), 5040)
        self.assertEqual(float(calculator.solve("pow(2,3)")), 8)
        self.assertEqual(float(calculator.solve("7!")), 5040)
        self.assertEqual(float(calculator.solve("3^2")), 9)
        self.assertEqual(float(calculator.solve("1+2*3")), 7)

    def test_string_expression_4(self):
        calculator = MathSolver()
        self.assertEqual(float(calculator.solve("((16-4)*2)/8")), 3)
        self.assertEqual(float(calculator.solve("((1+3)/(5-4))*(2/2)!")), 24)
        self.assertEqual(float(calculator.solve("root((2*36)/(3*3), 3)")), 2)
        self.assertEqual(float(calculator.solve("pow((2^2-2*8+3*11)/(5!-30*root(4,2)/2)*1/2-8,2)")), 49)

    def test_string_expression_5(self):
        calculator = MathSolver()
        self.assertEqual(float(calculator.solve("   r  o   o     t          (4      ,      2)")), 2)
        self.assertEqual(float(calculator.solve("f     act(   7   )")), 5040)
        self.assertEqual(float(calculator.solve("pow(    2  ,    3)")), 8)
        self.assertEqual(float(calculator.solve("7               !                          ")), 5040)
        self.assertEqual(float(calculator.solve("3           ^2")), 9)
        self.assertEqual(float(calculator.solve("1+2                                        *3")), 7)

    def test_string_expression_6(self):
        calculator = MathSolver()
        self.assertEqual(float(calculator.solve("2e3")), 2000)
        self.assertEqual(float(calculator.solve("0")), 0)
        self.assertEqual(float(calculator.solve("0^0")), 1)
        self.assertEqual(float(calculator.solve("0!")), 1)
        self.assertEqual(float(calculator.solve("root(0,2)")), 0)
        self.assertEqual(float(calculator.solve("3*4*5*0")), 0)
        with self.assertRaises(ZeroDivisionError):
            calculator.solve("(1+2+3)/(3-2-1)")
        with self.assertRaises(ZeroDivisionError):
            calculator.solve("(1+2+3)/0")


if __name__ == "__main__":
    unittest.main()
