import mathlib
import tkinter
from tkinter import *
from tkinter import messagebox

# okno
root = tkinter.Tk()
root['bg'] = '#FAFAFA'
root.geometry('405x600')
root.resizable(False, False)
root.title('Kalkulačka')



ix = 0
iy = 0
iz = 0

stridacka = 0

vysledek = 0
text = Text(root, height='4')



# pruhy pro tlačítka
qwe = PanedWindow(bg='#ECECEC')
asd = PanedWindow(bg='#ECECEC')
yxc = PanedWindow(bg='#ECECEC')
uio = PanedWindow(bg='#ECECEC')

# proměnné pro výpočty
sety = 0
setx = 0
setz = 0
bignum = 1
num_end = False
op = 0
lastop = [0, 0]
opcodes = ["=", "+", "-", "×", "÷", "^", "^1/", "!", "sin "]

# načtení čísla
def test(num):
    global ix
    global iy
    global iz
    global setx
    global sety
    global setz
    global bignum
    global stridacka
    if setx == 1 and sety == 1 and setz == 1:
        ix = 0
        setx = 0
        sety = 0
        setz = 0
        text.delete('1.0', END)
    
    if stridacka != 2:
        if setx == 0 and sety == 0:
            ix = ix*bignum+num
            bignum = 10
            
        elif setx == 1 and sety == 0:
            iy = iy*bignum+num
            bignum=10
            
        elif setx == 1 and sety == 1:
            iz = iz*bignum+num
            bignum=10
    
    
        text.insert(END, num)
        
        # dobrý výpis pro hledání chyb
        #text.delete('1.0', END)
        #text.insert(END, str(ix)+opcodes[lastop[0]]+str(iy)+opcodes[lastop[1]]+str(iz))
        stridacka = 1
    
# načtení a provedení operace
def operace(op):
    
    global stridacka
    if stridacka == 1 or stridacka == 2:
        global ix
        global iy
        global iz
        global setx
        global sety
        global setz
        global bignum
        global operations
        global vysledek
        global lastop
        
        
        operations_x = ["",
                      mathlib.MathOperations(ix).add,       mathlib.MathOperations(ix).sub,
                      mathlib.MathOperations(ix).mul,       mathlib.MathOperations(ix).div,
                      mathlib.MathOperations(ix).pow,       mathlib.MathOperations(ix).root,
                      mathlib.MathOperations(ix).factorial, mathlib.MathOperations(ix).sin
                      
                      ]
        
        operations_y = ["",
                      mathlib.MathOperations(iy).add,       mathlib.MathOperations(iy).sub,
                      mathlib.MathOperations(iy).mul,       mathlib.MathOperations(iy).div,
                      mathlib.MathOperations(iy).pow,       mathlib.MathOperations(iy).root,
                      mathlib.MathOperations(iy).factorial, mathlib.MathOperations(iy).sin
                      
                      ]
        operations_z = ["",
                   "","",
                   "","",
                   "","",
                   mathlib.MathOperations(iz).factorial, mathlib.MathOperations(iz).sin  
                   ]
        
        
        text.insert(END, opcodes[op])
        bignum = 1
        if setx == 1 and sety == 1 and setz == 1:
            setx = 0
            sety = 0
            setz = 0
        
        
        if setx == 0 and sety == 0 and op <= 6 and op >= 1:
            setx = 1
            lastop[0] = op
            #bignum = 1
        elif op == 7 or op == 8:
            stridacka = 2
            if setx == 0:
                #setx = 1
                ix = operations_x[op]()
            elif setx == 1 and sety == 0:
                #sety = 1
                iy = operations_y[op]()
            elif setx == 1 and sety == 1:
                iz = operations_z[op]()
        elif setx == 1 and sety == 0 and lastop[0] >= 3 and lastop[0] <= 6 and op != 0:
            ix = operations_x[lastop[0]](iy)
            iy = 0
            lastop[0] = op
        elif setx == 1 and sety == 0 and op == 1 or op == 2:
            ix = operations_x[lastop[0]](iy)
            iy = 0
            lastop[0] = op
        elif setx == 1 and sety == 0 and op >= 3 and op <= 6:
            sety = 1
            lastop[1] = op
        elif setx == 1 and sety == 1 and op >= 3 and op <= 6:
            if lastop[0] < 3 and lastop[1] < 3:
                ix = operations_x[lastop[0]](iy)
                iy = iz
                lastop[0] = lastop[1]
            else:
                iy = operations_y[lastop[1]](iz)
            lastop[1] = op
            iz = 0
        elif setx == 1 and sety == 1 and setz == 0 and op == 0:
            iy = operations_y[lastop[1]](iz)
            vysledek = operations_x[lastop[0]](iy)
            ix = vysledek
            iy = 0
            iz = 0
            setz = 1
            text.delete('1.0', END)
            text.insert(END,vysledek)
        elif setx == 1 and sety == 0 and op == 0:
            """try:
                vysledek = operations_x[lastop[0]](iy)
                text.delete('1.0', END)
                text.insert(END,vysledek)
            except (TypeError, ZeroDivisionError, ValueError):
                text.delete('1.0', END)
                text.insert(END,"Chyba v zadání výpočtu!")
                pass"""
            """if stridacka == 2:
                vysledek = ix
            else:
                """
            vysledek = operations_x[lastop[0]](iy)
            text.delete('1.0', END)
            text.insert(END,vysledek)
            ix = vysledek
            iy = 0
            iz = 0
            sety = 1
            setz = 1
        elif op == 0:
            if ix == 0:
                ix = vysledek
            text.delete('1.0', END)
            text.insert(END,str(ix))
            setx = 1
            sety = 1
            setz = 1
            #ix = 0
    if op == 0:
        stridacka = 1
    elif op == 7 or op == 8:
        stridacka = 2
    else:
        stridacka = 0

    
# přiřazení funkcí tlačítkam
q = Button(qwe, text="1", width='10',height='4', borderwidth='1', command=lambda: test(1))  #1 cislo = 8 px 3 buttony : 3*8 = 24, celkem/24 = 100/24=4 
w = Button(qwe, text="2", width='10',height='4', borderwidth='1', command=lambda: test(2))
e = Button(qwe, text="3", width='10',height='4', borderwidth='1', command=lambda: test(3))
r = Button(qwe, text="+", width='10',height='4', borderwidth='1', command=lambda: operace(1))
t = Button(qwe, text="-", width='10',height='4', borderwidth='1', command=lambda: operace(2))

a = Button(asd, text="4", width='10',height='4', borderwidth='1', command=lambda: test(4))
s = Button(asd, text="5", width='10',height='4', borderwidth='1', command=lambda: test(5))
d = Button(asd, text="6", width='10',height='4', borderwidth='1', command=lambda: test(6))
f = Button(asd, text="×", width='10',height='4', borderwidth='1', command=lambda: operace(3))
g = Button(asd, text="÷", width='10',height='4', borderwidth='1', command=lambda: operace(4))


y = Button(yxc, text="7", width='10',height='4', borderwidth='1', command=lambda: test(7))
x = Button(yxc, text="8", width='10',height='4', borderwidth='1', command=lambda: test(8))
c = Button(yxc, text="9", width='10',height='4', borderwidth='1', command=lambda: test(9))
v = Button(yxc, text="a^n", width='10',height='4', borderwidth='1', command=lambda: operace(5))
b = Button(yxc, text="n√a", width='10',height='4', borderwidth='1', command=lambda: operace(6))

u = Button(uio, text="0", width='10',height='4', borderwidth='1', command=lambda: test(0))
i = Button(uio, text="a!", width='10',height='4', borderwidth='1', command=lambda: operace(7))
o = Button(uio, text="sin a", width='10',height='4', borderwidth='1', command=lambda: operace(8))
p = Button(uio, text="=", width='20',height='4', borderwidth='1', command=lambda: operace(0))

# pruhy s tlačítky na spodek
uio.pack(
    side=BOTTOM,
    fill=X
    )

yxc.pack(
    side=BOTTOM,
    fill=X
    )
asd.pack(
    side=BOTTOM,
    fill=X
    )
qwe.pack(
    side=BOTTOM,
    fill=X
    )

text.pack( 
    side=BOTTOM,
    fill=BOTH,
)

# přiřazení tlačítek do pruhů
qwe.add(q)
qwe.add(w)
qwe.add(e)
qwe.add(r)
qwe.add(t)

asd.add(a)
asd.add(s)
asd.add(d)
asd.add(f)
asd.add(g)

yxc.add(y)
yxc.add(x)
yxc.add(c)
yxc.add(v)
yxc.add(b)

uio.add(u)
uio.add(i)
uio.add(o)
uio.add(p)


root.mainloop()
