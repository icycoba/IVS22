import mathlib
import tkinter
from tkinter import *
from tkinter import messagebox

# okno
root = tkinter.Tk()
root['bg'] = '#FAFAFA'
root.geometry('380x600')
root.resizable(False, False)
root.title('Kalkulačka')


ix = 0
iy = 0

vysledek = 0
text = Text(root, height='4')

# pruhy pro tlačítka
qwe = PanedWindow(bg='#ECECEC')
asd = PanedWindow(bg='#ECECEC')
yxc = PanedWindow(bg='#ECECEC')

# proměnné pro výpočty
sety = 0
setx = 0
bignum = 1
num_end = False
op = 0
lastop = 0
opcodes = ["=", "+", "-"]

# načtení čísla
def test(num):
    global ix
    global iy
    global setx
    global sety
    global bignum
    if setx == 1 and sety == 1:
        setx = 0
        sety = 0
    if setx == 0 and sety == 0:
        ix = ix*bignum+num
        bignum = 10
        
    elif setx == 1 and sety == 0:
        iy = iy*bignum+num
        bignum=10
        
    text.delete('1.0', END)
    #text.insert(END,str(ix)+"("+str(setx)+", "+str(sety)+") ")
    text.insert(END, str(ix)+opcodes[lastop]+str(iy))

# načtení a provedení operace
def operace(op):
    global ix
    global iy
    global setx
    global sety
    global bignum
    global operations
    global vysledek
    global lastop
    operations = ["", mathlib.MathOperations(ix).add, mathlib.MathOperations(ix).sub]
    bignum = 1
    if setx == 0 and sety == 0 and op != 0:
        setx = 1
        lastop = op
    elif setx == 1 and sety == 0 and op != 0:
        ix = operations[lastop](iy)
        lastop = op
        iy = 0
    elif setx == 1 and sety == 0 and op == 0:
        sety = 1
        text.delete('1.0', END)
        vysledek = operations[lastop](iy)
        ix = 0
        iy = 0
        text.insert(END,str(vysledek))
    
    
# přiřazení funkcí tlačítkam
q = Button(qwe, text="1", width='12',height='4', borderwidth='1', command=lambda: test(1))  #1 cislo = 8 px 3 buttony : 3*8 = 24, celkem/24 = 100/24=4 
w = Button(qwe, text="2", width='12',height='4', borderwidth='1', command=lambda: test(2))
e = Button(qwe, text="3", width='12',height='4', borderwidth='1', command=lambda: test(3))
r = Button(qwe, text="+", width='12',height='4', borderwidth='1', command=lambda: operace(1))

a = Button(asd, text="4", width='12',height='4', borderwidth='1', command=lambda: test(4))
s = Button(asd, text="5", width='12',height='4', borderwidth='1', command=lambda: test(5))
d = Button(asd, text="6", width='12',height='4', borderwidth='1', command=lambda: test(6))
f = Button(asd, text="-", width='12',height='4', borderwidth='1', command=lambda: operace(2))

y = Button(yxc, text="7", width='12',height='4', borderwidth='1', command=lambda: test(7))
x = Button(yxc, text="8", width='12',height='4', borderwidth='1', command=lambda: test(8))
c = Button(yxc, text="9", width='12',height='4', borderwidth='1', command=lambda: test(9))
v = Button(yxc, text="=", width='12',height='4', borderwidth='1', command=lambda: operace(0))

# pruhy s tlačítky na spodek
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

asd.add(a)
asd.add(s)
asd.add(d)
asd.add(f)

yxc.add(y)
yxc.add(x)
yxc.add(c)
yxc.add(v)


root.mainloop()
