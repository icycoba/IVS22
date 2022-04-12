
from mathlib import MathOperations

def strtonum(mystring):
    if not isinstance(mystring,str):
        num = mystring
    elif "." in mystring:
        num = float(mystring)
    else:
        num = int(mystring)
    return num

#TODO remove int()
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
                if func == "fact" and mid.isdigit():
                    mid = fact(mid)
                    pass
                elif func == "pow" and len(argsplit) == 2 and argsplit[1].isdigit() and argsplit[0].isdigit() :
                    mid = mypow(argsplit[0],argsplit[1])
                    pass
                elif func == "root" and len(argsplit) == 2 and argsplit[1].isdigit() and argsplit[0].isdigit() :
                    mid = root(argsplit[0],argsplit[1])
                    pass
                elif func == "sin" and mid.isdigit():
                    mid = mysin(mid)
                    pass
                else:
                    if "," in mid:
                        
                        mid = etn(argsplit[0]) + "," + etn(argsplit[1])
                        mid=usefunc(func,mid)

                        pass
                    else:
                        mid = etn(mid)
                        mid=usefunc(func,mid)
                
                return_num = before + str(mid) + after
                
                
                leave = 1
                break
            
            
        pass

    mydict = {"expression" : return_num, "value" : leave}
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
                mid = etn(mid)            
            return_num = before + str(mid) + after
            
            
            leave = 1
            break
            
            
        pass

    mydict = {"expression" : return_num, "value" : leave}
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

            #for idx2, j in enumerate(reversed(myexpression[:idx1])):
            #    if ((not j.isdigit()) and j != ".") or idx2+1 == len(myexpression[:idx1]):
            #         x = myexpression[idx1-idx2:idx1]
            #         startposition = idx1-idx2
            #         if (not j.isdigit()) and j != ".":
            #            xend=1
            #         break
            #    pass
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

    mydict = {"expression" : return_num, "value" : leave}
    return mydict



def rmuldiv(myexpression):
    leave = 0
    return_num = myexpression
    for idx1, i in enumerate(myexpression):
        if leave:
            break

        if i == "*" or i == "/" :
            
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

            #for idx2, j in enumerate(reversed(myexpression[:idx1])):
            #    if ((not j.isdigit()) and j != ".") or idx2+1 == len(myexpression[:idx1]):
            #         x = myexpression[idx1-idx2:idx1]
            #         startposition = idx1-idx2
            #         if (not j.isdigit()) and j != ".":
            #            xend=1
            #         break
            #    pass
            y=""
            for idx2, j in enumerate((myexpression[idx1+1:])):
                endposition = idx1+idx2+1
                if ((not j.isdigit()) and j != "."):
                    yend = 1
                    break
                y+=j

            if i == "*":
                result = str(strtonum(x)*strtonum(y))
            else:
                result = str(strtonum(x)/strtonum(y))

            return_num = ""
            if xend:
                return_num += myexpression[0:startposition]
            return_num += result
            if yend:
                return_num += myexpression[endposition:]            
            
            leave = 1
            break
        pass

    mydict = {"expression" : return_num, "value" : leave}
    return mydict


def raddsub(myexpression):
    leave = 0
    return_num = myexpression
    for idx1, i in enumerate(myexpression):
        if leave:
            break

        if i == "+" or i == "-" :
            endposition = 0
            endstyle = 0
            #+- are last evaluated operations, therefore first parameter is always right 
            x = myexpression[0:idx1] 
            #load parameter y
            y=""
            for idx2, j in enumerate((myexpression[idx1+1:])):
                endposition = idx1+idx2+1
                if ((not j.isdigit()) and j != "."):
                    endstyle = 1
                    break
                y+=j
            #choose operation
            if i == "+":
                result = str(strtonum(x)+strtonum(y))
            else:
                result = str(strtonum(x)-strtonum(y))
            #return value
            if endstyle:
                return_num = result  + myexpression[endposition:]
            else:
                return_num = result
            
            
            leave = 1
            break
        pass

    mydict = {"expression" : return_num, "value" : leave}
    return mydict


def etn (expression):

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

#print(etn("pow(2,2*2)*2+1"))

def printex(var, eq):
    print(etn(var)+" = " + eq)



print(etn("1+2*3!*2+1")  + " = 7")
