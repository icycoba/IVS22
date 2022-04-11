
from mathlib import MathOperations

def fact (x):
    calculator = MathOperations(int(x))
    return calculator.factorial()
def mypow (x,num):
    calculator = MathOperations(int(x))
    return calculator.pow(int(num))
def mysin (x):
    calculator = MathOperations(int(x))
    return calculator.sin()
def root (x,num):
    calculator = MathOperations(int(x))
    return calculator.root(int(num))

def usefunc(func,expression):
                    #/////////////////////
                    # TODO float or int check
                    # ///////////////////// 

    if func == "fact":
        expression = fact(float(expression))
    elif func == "pow":
        funcargs = expression.split()
        expression = pow(float(funcargs[0]),funcargs[1])
        pass
    elif func == "root":
        funcargs = expression.split()
        expression = root(float(funcargs[0]),funcargs[1])
        pass
    elif func == "sin":
        expression = mysin(float(expression))
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

                tocheck = mid.split(",")
                if func == "fact" and mid.isdigit():
                    #/////////////////////
                    # TODO float or int check
                    # ///////////////////// 
                    mid = fact(float(mid))
                    pass
                elif func == "pow" and len(tocheck) == 2 and tocheck[1].isdigit() and tocheck[0].isdigit() :
                    #/////////////////////
                    # TODO float or int check
                    # ///////////////////// 
                    mid = mypow(float(tocheck[0]),float(tocheck[1]))
                    pass
                elif func == "root" and len(tocheck) == 2 and tocheck[1].isdigit() and tocheck[0].isdigit() :
                    #/////////////////////
                    # TODO float or int check
                    # ///////////////////// 
                    mid = root(float(tocheck[0]),float(tocheck[1]))
                    pass
                elif func == "sin" and mid.isdigit():
                    #/////////////////////
                    # TODO float or int check
                    # ///////////////////// 
                    mid = mysin(float(tocheck[0]),float(tocheck[1]))
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


def rmuldiv(myexpression):
    leave = 0
    return_num = myexpression
    for idx1, i in enumerate(myexpression):
        if leave:
            break

        if i == "*" or i == "/" :
            
            endposition = 0
            startposition = 0
            for idx2, j in enumerate(reversed(myexpression[:idx1])):
                if ((not j.isdigit()) and j != ".") or idx2+1 == len(myexpression[:idx1]):
                     x = myexpression[idx1-idx2-1:idx1]
                     startposition = idx1-idx2-1
                     break
                pass
            y=""
            for idx2, j in enumerate((myexpression[idx1+1:])):
                endposition = idx1+idx2+1
                if ((not j.isdigit()) and j != "."):
                    break
                y+=j

            if i == "*":
                x = str(float(x)*float(y))
            else:
                x = str(float(x)/float(y))

            return_num = myexpression[0:startposition] + x + myexpression[endposition:]
            
            
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
            startposition = 0
            for idx2, j in enumerate(reversed(myexpression[:idx1])):
                if ((not j.isdigit()) and j != ".") or idx2+1 == len(myexpression[:idx1]):
                     x = myexpression[idx1-idx2-1:idx1]
                     startposition = idx1-idx2-1
                     break
                pass
            y=""
            for idx2, j in enumerate((myexpression[idx1+1:])):
                endposition = idx1+idx2+1
                if ((not j.isdigit()) and j != "."):
                    break
                y+=j

            if i == "+":
                x = str(float(x)+float(y))
            else:
                x = str(float(x)-float(y))

            return_num = myexpression[0:startposition] + x + myexpression[endposition:]
            
            
            leave = 1
            break
        pass

    mydict = {"expression" : return_num, "value" : leave}
    return mydict


def etn (expression):
    mydict = { "expression": expression, "value":0}

    while(not mydict["expression"].isdigit()):
        mydict = rfunc(mydict["expression"])
        if(mydict["value"]==0):
            break

    while(not mydict["expression"].isdigit()):
        mydict = rparenthesis(mydict["expression"])
        if(mydict["value"]==0):
            break

    while(not mydict["expression"].isdigit()):
        mydict = rmuldiv(mydict["expression"])
        if(mydict["value"]==0):
            break

    while(not mydict["expression"].isdigit()):
        mydict = raddsub(mydict["expression"])
        if(mydict["value"]==0):
            break

    expression = mydict["expression"]
    return expression

print(etn("1*fact(3)*2"))