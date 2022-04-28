"""
Soubor:     expression_to_num.py
Autor:      Štěpán Nekula   (xnekul04)
Projekt:    IVS #2 - Tvorba kalkulačky
Popis:      Modul pro řešení matematických výrazů
            Používá operace z matematické knihnovny mathlib.py
"""


from mathlib import MathOperations

def strtonum(mystring):
    """
    Funkce strtonum konvertuje řetězec na číslo.
    datový typ čísla je určen podle formátu čísla
    :param mystring: konvertovaný řetězec
    :return: funkce vrací výsledné číslo po konverzi řetězce
    """ 
    if not isinstance(mystring,str):
        num = mystring
    elif "." in mystring:
        num = float(mystring)
    else:
        num = int(mystring)
    return num

def fact (x):
    """
    Funkce fact volá funkci factorial z knihovny mathlib.

    :param x: předávané číslo pro funkci faktoriál
    :return: funkce vraci hodnotu x po použití funkce factorial
    """ 
    calculator = MathOperations(strtonum(x))
    return calculator.factorial()

def mypow (x,num):
    """
    Funkce mypow volá funkci pow z knihovny mathlib.

    :param x: základ pro umocnění
    :param num: exponent pro umocnění
    :return: funkce vrací hodnotu po umocnění čísla x
    """ 
    calculator = MathOperations(strtonum(x))
    return calculator.pow(strtonum(num))


def mysin (x):
    """
    Funkce mysin volá funkci sin z knihovny mathlib.

    :param x: předávané číslo pro funkci sin
    :return: funkce vraci hodnotu x po použití funkce sin
    """ 

    calculator = MathOperations(strtonum(x))
    return calculator.sin()
def root (x,num):
    """
    Funkce root volá funkci pow z knihovny mathlib.

    :param x: základ pro odmocnění
    :param num: exponent pro odmocnění
    :return: funkce vrací hodnotu po odmocnění čísla x
    """ 
    calculator = MathOperations(strtonum(x))
    return calculator.root(strtonum(num))

def simpnum(num):
    """
    Celočíselný float přetypuje na int.
    """
    simp = round(float(num),7)

    if simp%1 == 0: #is integer
        simp = (int(simp))
        return str(simp)
    return



def usefunc(func,expression):
    """
    Funkce zavolá funkci na základě prvního parametru a jako parametr/y ji předá expression rozdělený oddělovačem ","

    :param func: volaná funkce/operace
    :param expression: argumenty pro volanou funkci
    :return: funkce vrací návratovou hodnotu volané funkce
    """ 


    if func == "fact":
        expression = fact(strtonum(simpnum(expression)))
    elif func == "pow":
        funcargs = expression.split(",")
        expression = pow(strtonum(simpnum(funcargs[0])),strtonum(simpnum(funcargs[1])))
        pass
    elif func == "root":
        funcargs = expression.split(",")
        expression = root(strtonum(simpnum(funcargs[0])),strtonum(simpnum(funcargs[1])))
        pass
    elif func == "sin":
        expression = mysin(strtonum(expression))
        pass
    return expression


def myisdigit(var):
    """
    Funkce myisdigit určí zda řetězec var je číslo

    :param var: testovaný řetězec
    :return: funkce vrací boolovu hodnotu tvrzení, že řetězec var reprezentuje číslo
    """ 

    if var.isdigit() or (var[1:].isdigit() and (var[0] == "-" or var[0] == "+" )):
        return True
    return False

#gets x argument for operation
def getx(leftside):
    """
    Funkce getx vyseparuje číslo 'x'  pro použití pro operaci jako argument na konci z řetězce leftside
    x je míněno jako levý argument pro operaci (např. u oprace sčítání: x+y)

    :param leftside: zpracovávaný řetězec
    :return: funkce vrací "dictionary" s klíčem "x" jako hodnota nalezeného 'x' a klíčem "before" s hodnotou zbytku řetězce bez 'x' 
    """ 

    #vrati x a zbytek
    xend = 0
    yend = 0
    x=""
    lastchar = "0"
    for j in reversed(leftside):
        if ((not j.isdigit()) and j != "." and 1!="-" and 1!="+"):
            break
        elif (not j.isdigit()) and (lastchar=="+" or lastchar=="-"):
            break
        elif ( j.isdigit()) and (lastchar=="+" or lastchar=="-"):
            x = x[0:-1]
        x+=j
        lastchar = j
    x = x[::-1]
    returndict = {"x" : x, "before" : leftside[:len(leftside)-len(x)]}

    return returndict

#gets y argument for operation
def gety(rightside):
    """
    Funkce gety vyseparuje číslo 'y'  pro použití pro operaci jako argument na začátku z řetězce rightside
    y je míněno jako pravý argument pro operaci (např. u oprace sčítání: x+y)

    :param rightside: zpracovávaný řetězec
    :return: funkce vrací "dictionary" s klíčem "y" jako hodnota nalezeného 'y' a klíčem "after" s hodnotou zbytku řetězce bez 'y' 
    """ 

    #vrati y a zbytek
    y=""
    for idx2, j in enumerate(rightside):
        if ((not j.isdigit()) and j != "." and (not(idx2==0 and (j == "+" or j == "-")))):
            break
        y+=j
    returndicty = {"y" : y, "after" : rightside[len(y):]}
    return returndicty

def rdupli(myexpression):
    """
    Funkce rdupli zkrátí (resp. vyhodnotí) všechna opakující se znaménka +/- v řetězci

    :param myexpression: zpracovávaný řetězec
    :return: funkce vrací řetězec myexpression, ale s upravenými znaménky
    """ 

    myexpression = myexpression.replace("--","+")
    myexpression = myexpression.replace("++","+")
    myexpression = myexpression.replace("-+","-")
    myexpression = myexpression.replace("+-","-")
    return myexpression

def rfunc(myexpression):
    """
    Funkce rfunc vyhodnotí první nalezenou zleva operaci typu funkce v řetězci myexpression, které jsou zapsané slovně
    vyhodnocované funkce: fact(),pow(),root(),sin()
    pokud argumenty funkcí nejsou vyhodnoceny, nejdříve se vyhodnotí a potom až se vyhodnocuje samotná funkce

    :param myexpression: zpracovávaný řetězec
    :return: funkce vrací řetězec myexpression, ale s vyhodnocenou první zleva nalezenou operací typu funkce + hodnotu leave, zda vyhodnocování vůbec proběhlo
    """ 

    funclist = ["fact","pow","root","sin"]
    return_num = myexpression
    leave = 0


    for idx1, i in enumerate(myexpression):
        if leave:
            break

        for func in funclist:
            name = myexpression[idx1:idx1+len(func)]
            if name == func :
                before = myexpression[0:idx1]
                endposition = 0
                rightp = 0
                leftp = 0
                
                for idx2, j in enumerate(myexpression[idx1+len(func):]):
                    if j == "(":
                        rightp +=1
                    if j == ")":
                        leftp +=1
                    if rightp == leftp:
                        endposition = idx2
                        break
                mid = myexpression[idx1+len(func)+1:idx1+len(func)+endposition]
                after = myexpression[idx1+len(func)+endposition+1:]

                argsplit = mid.split(",")
                if func == "fact" and myisdigit(mid):
                    mid = fact(mid)
                    pass
                elif func == "pow" and len(argsplit) == 2 and myisdigit(argsplit[1]) and myisdigit(argsplit[0]) :
                    mid = mypow(argsplit[0],argsplit[1])
                    pass
                elif func == "root" and len(argsplit) == 2 and myisdigit(argsplit[1]) and myisdigit(argsplit[0]) :
                    mid = root(argsplit[0],argsplit[1])
                    pass
                elif func == "sin" and myisdigit(mid):
                    mid = mysin(mid)
                    pass
                else:
                    if "," in mid:
                        
                        mid = exprtonum(argsplit[0]) + "," + exprtonum(argsplit[1])
                        mid=usefunc(func,mid)

                        pass
                    else:
                        mid = exprtonum(mid)
                        mid=usefunc(func,mid)
                
                return_num = before + str(mid) + after
                
                
                leave = 1
                break
            
            
        pass

    mydict = {"expression" : rdupli(return_num), "value" : leave}
    return mydict


def rparenthesis(myexpression):
    """
    Funkce rparenthesis vyhodnotí první nalezenou zleva dvojici kulatých závorek
    pokud obsah závorek není vyhodnocen, nejdříve se vyhodnotí a potom až se odstraní samotné závorky

    :param myexpression: zpracovávaný řetězec
    :return: funkce vrací řetězec myexpression, ale s vyhodnoceným obsahem závorek a odebranými samotnými závorkami + hodnotu leave, zda vyhodnocování vůbec proběhlo
    """ 

    leave = 0
    return_num = myexpression
    for idx1, i in enumerate(myexpression):
        if leave:
            break

        if i == "(" :
            before = myexpression[0:idx1]
            endposition = 0
            rightp = 0
            leftp = 0
            
            for idx2, j in enumerate(myexpression[idx1:]):
                if j == "(":
                    rightp +=1
                if j == ")":
                    leftp +=1
                if rightp == leftp:
                    endposition = idx2
                    break
            mid = myexpression[idx1+1:idx1+endposition]
            after = myexpression[idx1+endposition+1:]
            if mid.isdigit():
                pass
            else:
                mid = exprtonum(mid)            
            return_num = before + str(mid) + after
            
            
            leave = 1
            break
            
            
        pass

    mydict = {"expression" : rdupli(return_num), "value" : leave}
    return mydict

def altfunc(myexpression):
    """
    Funkce altfunc vyhodnotí první nalezenou zleva operaci typu funkce v řetězci myexpression, které jsou zapsané symbolicky
    vyhodnocované funkce, příklad: x**y (umocnění), x! (faktoriál)
    pokud argumenty funkcí nejsou vyhodnoceny, nejdříve se vyhodnotí a potom až se vyhodnocuje samotná funkce

    :param myexpression: zpracovávaný řetězec
    :return: funkce vrací řetězec myexpression, ale s vyhodnocenou první zleva operací typu funkce  + hodnotu leave, zda vyhodnocování vůbec proběhlo
    """ 

    leave = 0
    return_num = myexpression
    for idx1, i in enumerate(myexpression):
        if leave:
            break

        if i == "^" or i == "!" :
            
            endposition = 0
            startposition = 0
            xend = 0
            yend = 0

            x=""
            for idx2, j in enumerate(reversed(myexpression[:idx1])):
                startposition = idx1-idx2
                if ((not j.isdigit()) and j != "."):
                    xend = 1
                    break
                x+=j
            x = x[::-1]

            y=""
            for idx2, j in enumerate((myexpression[idx1+1:])):
                endposition = idx1+idx2+1
                if ((not j.isdigit()) and j != "."):
                    yend = 1
                    break
                y+=j

            if i == "!":
                result = str(fact(simpnum(x)))
            else:
                result = str(mypow(simpnum(x),simpnum(y)))

            return_num = ""
            if xend:
                return_num += myexpression[0:startposition]
            return_num += result
            if yend:
                return_num += myexpression[endposition:]            
            
            leave = 1
            break
        pass

    mydict = {"expression" : rdupli(return_num), "value" : leave}
    return mydict



def rmuldiv(myexpression):
    """
    Funkce rmuldiv vyhodnotí první nalezenou zleva operaci násobení nebo dělení

    :param myexpression: zpracovávaný řetězec 
    :return: funkce vrací řetězec myexpression, ale s vyhodnocenou první operaci násobení nebo dělení + hodnotu leave, zda vyhodnocování vůbec proběhlo
    """ 
    leave = 0
    return_num = myexpression
    for idx1, i in enumerate(myexpression):
        if leave:
            break

        if i == "*" or i == "/" :

            returnx = getx(myexpression[:idx1])
            returny = gety(myexpression[idx1+1:])
            calculator = MathOperations(strtonum(returnx["x"]))
            if i == "*":
                result = str(calculator.mul(strtonum(returny["y"])))
            else:
                result = str(calculator.div(strtonum(returny["y"])))

            return_num = returnx["before"] + result + returny["after"]            
            
            leave = 1
            break
        pass

    mydict = {"expression" : rdupli(return_num), "value" : leave}
    return mydict


def raddsub(myexpression):
    """
    Funkce raddsub vyhodnotí první nalezenou zleva operaci sčítání nebo odčítání

    :param myexpression: zpracovávaný řetězec
    :return: funkce vrací řetězec myexpression, ale s vyhodnocenou první operaci sčítání nebo odčítání + hodnotu leave, zda vyhodnocování vůbec proběhlo
    """ 
    leave = 0
    return_num = myexpression
    for idx1, i in enumerate(myexpression):
        if leave:
            break

        if (i == "+" or i == "-") and myexpression[idx1-1].isdigit() and idx1!=0 :
            endposition = 0
            endstyle = 0
            #+- are last evaluated operations, therefore first parameter is always right 
            x = myexpression[0:idx1]

            if x=="":
                x=0
            #load parameter y
            returny = gety(myexpression[idx1+1:])

            calculator = MathOperations(strtonum(x))
            if i == "+":
                result = str(calculator.add(strtonum(returny["y"])))
            else:
                result = str(calculator.sub(strtonum(returny["y"])))
            #return value
            return_num = result  + returny["after"]
            
            leave = 1
            break
        pass

    mydict = {"expression" : rdupli(return_num), "value" : leave}
    return mydict



def exprtonum (expression):
    """
    Funkce exprtonum vyhodnotí zadaný výraz
    Povolené části výrazu jsou: čísla v desítkové soustavě, závorky, sčítání, násobení, dělené, odčítání ...a funkce: fact(x),sin(x),root(x,y),pow(x,y)
            - přičemž pow(x,y) a fact(x) mohou být zapsány symbolicky: x**y, x! 

    :param myexpression: zpracovávaný výraz
    :return: funkce vrací číslo, které je výsledkem výrazu
    """ 


    #Přidává funkcionalitu PI
    expression = expression.replace("PI","3.141592653589793")
    mydict = { "expression": expression.replace(" ",""), "value":0}
# evaluate functions
    while(not mydict["expression"].isdigit()):
        mydict = rfunc(mydict["expression"])
        if(mydict["value"]==0):
            break
# evaluate parenthesis
    while(not mydict["expression"].isdigit()):
        mydict = rparenthesis(mydict["expression"])
        if(mydict["value"]==0):
            break

# evaluate alt version of function notation ! ^
    while(not mydict["expression"].isdigit()):
        mydict = altfunc(mydict["expression"])
        if(mydict["value"]==0):
            break

# evaluate mul div
    while(not mydict["expression"].isdigit()):
        mydict = rmuldiv(mydict["expression"])
        if(mydict["value"]==0):
            break
# evaluate add sub
    while(not mydict["expression"].isdigit()):
        mydict = raddsub(mydict["expression"])
        if(mydict["value"]==0):
            break

    expression = mydict["expression"]
    return expression




class MathSolver:
    """Třída sloužící pro řešení matematických výrazů"""
    
    # podpopruje:
    # 1) "+x" "-x"
    # 2) "x+y" "x-y"
    # 3) "(x)"
    # 4) "fact(x)" "sin(x)" "pow(x)" "root(x)"
    # 5) "x**y" "x!"
    # 6) "x*y" "x/y"
    # 7) "PI" // PI = 3.141592653589793

    def __init__(self, num=0):
        """
        Inicializace proměnné ans

        :param num: volitelny parametr; defaultni hodnota je 0
        """
        if not(isinstance(num,int) or isinstance(num,float)):
            raise TypeError()
        self.ans = num

    def solve(self,expression):
        """
        Použití metody solve na proměnnou expression

        Vyřeší matematický výraz a přiřadí hodnotě ans

        :return: metoda vrací hodnotu ans po vyřešení výrazu
        """
        if not(isinstance(expression,str)):
            raise TypeError()

        self.ans = exprtonum(expression)
        return self.ans



def printex(var):
    var = var.split("=")
    print(exprtonum(var[0])+" = " + var[1])
