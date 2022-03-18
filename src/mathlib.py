"""
Soubor:     mathlib.py
Autor:      Štěpán Nekula   (xnekul04)
            Jan Kundrata    (xkundr07)
Projekt:    IVS #2 - Tvorba kalkulačky
Popis:      Knihovna pro matematické operace
"""


class MathOperations:
    """Trida slouzici pro praci s matematickou knihovnou"""

    def __init__(self, num=0):
        """Inicializace promenne ans, defaultni hodnota je 0"""
        self.ans = num

    def getvalue(self):
        """Ziskani hodnoty promenne ans"""
        pass

    def add(self, num):
        """
        Pricteni hodnoty num k promenne ans

        ans = ans + num

        :param num: hodnota, ktera bude prictena
        :return: funkce vraci hodnotu ans po secteni s hodnotou num
        """
        pass

    def sub(self, num):
        """
        Odecteni hodnoty num od promenne ans

        ans = ans - num

        :param num: hodnota, ktera bude odectena
        :return: funkce vraci hodnotu ans po odecteni hodnoty num
        """
        pass

    def mul(self, num):
        """
        Nasobeni hodnoty num s promennou ans

        ans = ans * num

        :param num: hodnota, kterou se bude nasobit
        :return: funkce vraci hodnotu ans po vynasobeni hodnotou num
        """
        pass

    def div(self, num):
        """
        Deleni promenne ans hodnotou num

        ans = ans / num

        :param num: hodnota, kterou se bude delit
        :return: funkce vraci hodnotu ans po vydeleni hodnotou num
        """
        pass

    def pow(self, num):
        """
        Umocneni promenne ans hodnotou num

        ans = ans^num

        :param num: hodnota, kterou se bude umocnovat
        :return: funkce vraci hodnotu ans po umocneni hodnotou num
        """
        pass

    def sqrt(self, num):
        """
        Odmocneni promenne ans hodnotou num

        ans = ans^(1/num)

        :param num: hodnota, kterou se bude odmocnovat
        :return: funkce vraci hodnotu ans po odmocneni hodnotou num
        """
        pass
