"""
Soubor:     expression_to_num.py
Autor:      Štěpán Nekula   (xnekul04)
Projekt:    IVS #2 - Tvorba kalkulačky
Popis:      Modul pro řešení matematických výrazů
            Používá operace z matematické knihnovny mathlib.py
"""


from mathlib import MathOperations

def strtonum(mystring):
    if not isinstance(mystring,str):
        num = mystring
    elif "." in mystring:
        num = float(mystring)
    else:
        num = int(mystring)
    return num

def fact (x):
    calculator = MathOperations(strtonum(x))
    return calculator.factorial()

def mypow (x,num):
    calculator = MathOperations(strtonum(x))
    return calculator.pow(strtonum(num))
def mysin (x):
    calculator = MathOperations(strtonum(x))
    return calculator.sin()
def root (x,num):
    calculator = MathOperations(strtonum(x))
    return calculator.root(strtonum(num))

def usefunc(func,expression):

    if func == "fact":
        expression = fact(strtonum(expression))
    elif func == "pow":
        funcargs = expression.split(",")
        expression = pow(strtonum(funcargs[0]),strtonum(funcargs[1]))
        pass
    elif func == "root":
        funcargs = expression.split(",")
        expression = root(strtonum(funcargs[0]),strtonum(funcargs[1]))
        pass
    elif func == "sin":
        expression = mysin(strtonum(expression))
        pass
    return expression


def myisdigit(var):
    if var.isdigit() or (var[1:].isdigit() and (var[0] == "-" or var[0] == "+" )):
        return True
    return False

#gets x argument for operation
def getx(leftside):
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
    #vrati y a zbytek
    y=""
    for idx2, j in enumerate(rightside):
        if ((not j.isdigit()) and j != "." and (not(idx2==0 and (j == "+" or j == "-")))):
            break
        y+=j
    returndicty = {"y" : y, "after" : rightside[len(y):]}
    return returndicty

def rdupli(myexpression):
    myexpression = myexpression.replace("--","+")
    myexpression = myexpression.replace("++","+")
    myexpression = myexpression.replace("-+","-")
    myexpression = myexpression.replace("+-","-")
    return myexpression

def rfunc(myexpression):
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
                result = str(fact(x))
            else:
                result = str(mypow(x,y))

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
#            endposition = 0
#            startposition = 0
#            xend = 0
#            yend = 0
#            
#            x=""
#            for idx2, j in enumerate(reversed(myexpression[:idx1])):
#                startposition = idx1-idx2
#                if ((not j.isdigit()) and j != "."):
#                    xend = 1
#                    break
#                x+=j
#            x = x[::-1]
#
#            y=""
#            for idx2, j in enumerate((myexpression[idx1+1:])):
#                endposition = idx1+idx2+1
#                if ((not j.isdigit()) and j != "."):
#                    yend = 1
#                    break
#                y+=j
#
#            if i == "*":
#                result = str(strtonum(x)*strtonum(y))
#            else:
#                result = str(strtonum(x)/strtonum(y))
#
#            return_num = ""
#            if xend:
#                return_num += myexpression[0:startposition]
#            return_num += result
#            if yend:
#                return_num += myexpression[endposition:]            
            
            leave = 1
            break
        pass

    mydict = {"expression" : rdupli(return_num), "value" : leave}
    return mydict


def raddsub(myexpression):
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


#///////////////            for idx2, j in enumerate((myexpression[idx1+1:])):
#///////////////                endposition = idx1+idx2+1
#///////////////                if ((not j.isdigit()) and j != "."):
#///////////////                    endstyle = 1
#///////////////                    break
#///////////////                y+=j
#///////////////            #choose operation
#///////////////            if i == "+":
#///////////////                result = str(strtonum(x)+strtonum(y))
#///////////////            else:
#///////////////                result = str(strtonum(x)-strtonum(y))
#///////////////            #return value
#///////////////            if endstyle:
#///////////////                return_num = result  + myexpression[endposition:]
#///////////////            else:
#///////////////                return_num = result
            
            
            leave = 1
            break
        pass

    mydict = {"expression" : rdupli(return_num), "value" : leave}
    return mydict



def exprtonum (expression):

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

