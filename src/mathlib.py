"""
Soubor:     mathlib.py
Autor:      Štěpán Nekula   (xnekul04)
            Jan Kundrata    (xkundr07)
Projekt:    IVS #2 - Tvorba kalkulačky
Popis:      Knihovna pro matematické operace
"""


# Calculation accuracy parameters
ROUNDED_TO = 5
EPSILON = 0.0000001
# Exception messages
EXCEPTION_MESSAGE = 'Undefined operation'
TypeErrormsg = 'TypeError'
ZeroDivisionErrormsg = 'ZeroDivisionError'
ValueErrormsg = 'ValueError'

def isnum(var):
    """
    Funkce sloužící k určení datového typu číslo
    :param var: testovaná proměnná
    :return: boolova hodnota výroku, že proměnná je číslo
    """
    if( isinstance(var, int)  or isinstance(var, float)  ):
        return 1
    return 0



class MathOperations:
    """Trida slouzici pro praci s matematickou knihovnou"""





    def __init__(self, num=0):
        """
        Inicializace promenne ans

        :param num: volitelny parametr; defaultni hodnota je 0
        """
        if not(isnum(num)):
            raise TypeError()
        self.ans = num

    def getvalue(self):
        """
        Ziskani hodnoty promenne ans

        :return: funkce vraci hodnotu ans
        """
        return self.ans

    def add(self, num):
        """
        Pricteni hodnoty num k promenne ans

        ans = ans + num

        :param num: hodnota, ktera bude prictena
        :return: funkce vraci hodnotu ans po secteni s hodnotou num
        """
        if not(isnum(self.ans) and isnum(num)):
            raise TypeError()
    
        self.ans = self.ans+num
        return self.ans


    def sub(self, num):
        """
        Odecteni hodnoty num od promenne ans

        ans = ans - num

        :param num: hodnota, ktera bude odectena
        :return: funkce vraci hodnotu ans po odecteni hodnoty num
        """
        if not(isnum(self.ans) and isnum(num)):
            raise TypeError()
        self.ans = self.ans-num
        return self.ans


    def mul(self, num):
        """
        Nasobeni hodnoty num s promennou ans

        ans = ans * num

        :param num: hodnota, kterou se bude nasobit
        :return: funkce vraci hodnotu ans po vynasobeni hodnotou num
        """
        if not(isnum(self.ans) and isnum(num)):
            raise TypeError()
        self.ans = self.ans*num
        return self.ans

    def div(self, num):
        """
        Deleni promenne ans hodnotou num

        ans = ans / num

        :param num: hodnota, kterou se bude delit
        :return: funkce vraci hodnotu ans po vydeleni hodnotou num
        """
        if (not isnum(self.ans)) or (not isnum(num)):
               raise TypeError()
        if num == 0 or num == -0 :
             raise ZeroDivisionError()
        self.ans = self.ans/num
        return self.ans

    def factorial(self):
        """
        Faktorial promenne ans

        ans = ans!

        :return: funkce vraci faktorial hodnoty ans
        """
        
        if not(isnum(self.ans)):
            raise TypeError()        
        
        if (not isinstance(self.ans, int)):
            raise ValueError()
        if self.ans<0 : #ERROR if self is nonnatural number
            raise ValueError()

        count = self.ans
        total = 1
        while count > 1:
            total = total * count
            count = count - 1

        self.ans = total
        return self.ans

    def pow(self, num):
        """
        Umocneni promenne ans hodnotou num

        ans = ans^num

        :param num: hodnota, kterou se bude umocnovat
        :return: funkce vraci hodnotu ans po umocneni hodnotou num
        """
        if not(isnum(self.ans) and isnum(num)):
            raise TypeError()

        if num<0 or (not isinstance(num, int)): #ERROR if num is nonnatural number
            raise ValueError()

        result = 1
        while num > 0:
            result *= self.ans
            num-=1
        self.ans = round(result,ROUNDED_TO)
        return self.ans


    def root(self, num):
        """

        Odmocneni promenne ans hodnotou num

        ans = ans^(1/num)

        :param num: hodnota, kterou se bude odmocnovat
        :return: funkce vraci hodnotu ans po odmocneni hodnotou num
        """
#        if not(isnum(self.ans) and isnum(num)):
#            raise TypeError()
#
#        if (num%2 == 0 and self.ans<0 ) or (not isinstance(num, int)) or num<0:
#            raise ValueError()
#
 #       tmp = self.ans
 #       x1 = 0
 #       x2 = (num-1)/num*x1+tmp/(num*pow(tmp,num-1))
 #       tmp=num-1
 #       x1 = x2
 #       x2 = (num-1)/num*x1+tmp/(num*pow(tmp,num-1))
 #       tmp=num-1
#
   #     while(abs(x1-x2)<EPSILON):
   #         x1 = x2
   #         x2 = (num-1)/num*x1+tmp/(num*pow(tmp,num-1))
   #         tmp=num-1
   #     self.ans = round(x2,ROUNDED_TO)
        return self.ans


    def sin(self):
        """
        Použití funkce sin na proměnnou ans

        ans = sin(ans)

        :return: funkce vraci hodnotu ans po použití funkce sin
        """
        if not(isnum(self.ans)):
            raise TypeError()


        counter = 1
        result = 0
        difference = self.ans
        while(abs(difference)>EPSILON):
            result = result + difference
            counter+=2
            difference = difference /(-counter+1)/(counter) *self.ans*self.ans

        self.ans = round(result,ROUNDED_TO)
        return self.ans

    def solve(self, expression):
        pass
