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
    if isinstance(var,bool):
        return 0
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
        #exception to handle float limits
        try:
            self.ans = self.ans+num
        except OverflowError:
            self.ans = int(self.ans)+int(num)

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
        
        #exception to handle float limits
        try:
            self.ans = self.ans-num
        except OverflowError:
            self.ans = int(self.ans)-int(num)

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
        #exception to handle float limits
        try:
            self.ans = self.ans*num
        except OverflowError:
            self.ans = int(self.ans)*int(num)
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
        #exception to handle float limits
        try:
            self.ans = self.ans/num
        except OverflowError:
            if int(num)==0:
                raise ZeroDivisionError()
            self.ans = int(self.ans)/int(num)

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

        #exception to handle float limit
        try:
            self.ans = self.ans**num
        except OverflowError:   
            self.ans = int(self.ans)**int(num)

        return self.ans


    def root(self, num):
        """

        Odmocneni promenne ans hodnotou num

        ans = ans^(1/num)

        :param num: hodnota, kterou se bude odmocnovat
        :return: funkce vraci hodnotu ans po odmocneni hodnotou num
        """
        if not(isnum(self.ans) and isnum(num)):
            raise TypeError()

        if (num%2 == 0 and self.ans<0 ) or (not isinstance(num, int)) :
            #(or num<0)
            raise ValueError()

        if((self.ans==0 and num < 0) or num==0):
            raise ZeroDivisionError()

        negative = False
        if num < 0:
            negative = True
            num = -num

        if self.ans > 0:
            bot = 0
            top = self.ans
        else:
            bot = self.ans
            top = 0

        result = self.ans
        while abs(result**num - self.ans) > EPSILON:
            if result**num > self.ans:
                top = result
            else:
                bot = result
            result = (bot+top)/2
            
        if negative and result != 0:
            result = 1/result


        self.ans = round(result,ROUNDED_TO)
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



