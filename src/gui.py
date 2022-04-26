"""
Soubor:     gui.py
Autor:      xxx
Projekt:    IVS #2 - Tvorba kalkulačky
Popis:      Grafické rozhraní pro kalkulačku
"""

#TODO: OUTPUT CHECK, FIX HELP 

from tkinter import *
from expression_to_num import MathSolver #řešení výrazů

import subprocess, os, platform #pro otevření nápovědy

########################################################
#PARAMS
buttonwidth = 8
buttonheight = 2
bfcolor ="#202020"
normalbuttoncolor = "#111111"
normalfontcolor = "#ffffff"
HelpFile = "help.pdf"
########################################################

# BASIC SETUP
root = Tk()
root['bg'] = bfcolor
root.geometry('450x500')
root.resizable(False, False)
root.title('Kalkulačka')

calculator = MathSolver() #Global variable for calculations
#literally magic
root.tk.call('tk', 'scaling', 2.0)

#OKNO TEXTU
TextDisplay = Text(root, fg=normalfontcolor,bg=bfcolor,insertbackground=normalfontcolor)#height='4'
# pruhy pro tlačítka
menu = PanedWindow(bg=normalbuttoncolor)

window0 = PanedWindow(bg=bfcolor)
window1 = PanedWindow(bg=bfcolor)
window2 = PanedWindow(bg=bfcolor)
window3 = PanedWindow(bg=bfcolor)
window4 = PanedWindow(bg=bfcolor)

#Určuje stav Textového pole
TextState = 0

# načtení čísla
def insert(input):
    global TextState

    #deletes unwanted error message
    if(TextState == -1):
        TextDisplay.delete('1.0', END)
        TextState = 0

    #inserts new input
    TextDisplay.insert(END, input)
        
def Delete():
    TextDisplay.delete('end-2c', 'end')
def AllClear():
    TextDisplay.delete('1.0', END)

#solves expression
def CalcError():
    TextDisplay.delete('1.0', END)
    TextDisplay.insert(END, "CALCULATION ERROR")
    global TextState
    TextState = -1


def solve():
    input = TextDisplay.get("1.0",END)
    try:
        calculator.solve(input)
        TextDisplay.delete('1.0', END)

        calculator
    except Exception:
        CalcError()
        return
    try:
        output = float(calculator.ans)
    except:
        CalcError()
        return
    if output%1 == 0: #is integer
        insert(int(output))
    else:
        insert(round(output,5))
    



#ADDS ENTER as key for solve
def EnterKey():
    TextDisplay.delete('end-1c', 'end')
    solve()
root.bind('<Return>', lambda event=None: EnterKey()) 

#end of enter solution


#otevření nápovědy
#
def OpenHelp():
    global HelpFile # soubor obashujici napovedu
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', HelpFile))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(HelpFile)
    else:                                   # linux variants
        subprocess.call(('xdg-open', HelpFile))

    
# přiřazení funkcí tlačítkam
helpbutton = Button(menu,font=("Comicsans", 6), text="Help", width=4,height=1, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: OpenHelp())  #1 cislo = 8 px 3 buttony : 3*8 = 24, celkem/24 = 100/24=4 


b00 = Button(window0, text="0", width=buttonwidth,height=buttonheight, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: insert(0))  #1 cislo = 8 px 3 buttony : 3*8 = 24, celkem/24 = 100/24=4 
b01 = Button(window0, text=".", width=buttonwidth,height=buttonheight, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: insert("."))
b02 = Button(window0, text="(", width=buttonwidth,height=buttonheight, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: insert("("))
b03 = Button(window0, text=")", width=buttonwidth,height=buttonheight, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: insert(")"))
b04 = Button(window0, text="=", width=buttonwidth,height=buttonheight, bg="#6b121e" ,fg=normalfontcolor, borderwidth='0', command=lambda: solve())

b10 = Button(window1, text="1", width=buttonwidth,height=buttonheight, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: insert(1))
b11 = Button(window1, text="2", width=buttonwidth,height=buttonheight, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: insert(2))
b12 = Button(window1, text="3", width=buttonwidth,height=buttonheight, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: insert(3))
b13 = Button(window1, text="+", width=buttonwidth,height=buttonheight, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: insert("+"))
b14 = Button(window1, text="-", width=buttonwidth,height=buttonheight, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: insert("-"))

b20 = Button(window2, text="4", width=buttonwidth,height=buttonheight, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: insert(4))
b21 = Button(window2, text="5", width=buttonwidth,height=buttonheight, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: insert(5))
b22 = Button(window2, text="6", width=buttonwidth,height=buttonheight, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: insert(6))
b23 = Button(window2, text="×", width=buttonwidth,height=buttonheight, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: insert("*"))
b24 = Button(window2, text="÷", width=buttonwidth,height=buttonheight, borderwidth='0',bg=normalbuttoncolor,fg=normalfontcolor, command=lambda: insert("/"))

b30 = Button(window3, text="7", width=buttonwidth,height=buttonheight, borderwidth='0',         bg=normalbuttoncolor,fg=normalfontcolor,command=lambda: insert("7"))
b31 = Button(window3, text="8", width=buttonwidth,height=buttonheight, borderwidth='0',         bg=normalbuttoncolor,fg=normalfontcolor,command=lambda: insert("8"))
b32 = Button(window3, text="9", width=buttonwidth,height=buttonheight, borderwidth='0',         bg=normalbuttoncolor,fg=normalfontcolor,command=lambda: insert("9"))
b33 = Button(window3, text="DEL", width=buttonwidth,height=buttonheight, borderwidth='0',       bg=normalbuttoncolor,fg=normalfontcolor,command=lambda: Delete())
b34 = Button(window3, text="AC", width=buttonwidth,height=buttonheight, borderwidth='0',        bg=normalbuttoncolor,fg=normalfontcolor,command=lambda: AllClear())

b40 = Button(window4, text="sin(x)", width=buttonwidth,height=buttonheight, borderwidth='0',    bg=normalbuttoncolor,fg=normalfontcolor,command=lambda: insert("sin("))
b41 = Button(window4, text="fact(x)", width=buttonwidth,height=buttonheight, borderwidth='0',   bg=normalbuttoncolor,fg=normalfontcolor,command=lambda: insert("fact("))
b42 = Button(window4, text="pow(x,y)", width=buttonwidth,height=buttonheight, borderwidth='0',  bg=normalbuttoncolor,fg=normalfontcolor,command=lambda: insert("pow("))
b43 = Button(window4, text="root(x,y)", width=buttonwidth,height=buttonheight, borderwidth='0', bg=normalbuttoncolor,fg=normalfontcolor,command=lambda: insert("root("))
b44 = Button(window4, text=",", width=buttonwidth,height=buttonheight, borderwidth='0',         bg=normalbuttoncolor,fg=normalfontcolor,command=lambda: insert(","))

# okna pack
menu.pack(
    side=TOP,
    anchor=NW,
    fill=X
        )

window0.pack(
    side=BOTTOM,
    fill=X
    )
window1.pack(
    side=BOTTOM,
    fill=X
    )

window2.pack(
    side=BOTTOM,
    fill=X
    )
window3.pack(
    side=BOTTOM,
    fill=X
    )
window4.pack(
    side=BOTTOM,
    fill=X
    )

TextDisplay.pack( 
    side=BOTTOM,
    fill=BOTH,
)

# přiřazení tlačítek do pruhů
menu.add(helpbutton)

window0.add(b00)
window0.add(b01)
window0.add(b02)
window0.add(b03)
window0.add(b04)
############b#
window1.add(b10)
window1.add(b11)
window1.add(b12)
window1.add(b13)
window1.add(b14)
############b#### 
window2.add(b20)
window2.add(b21)
window2.add(b22)
window2.add(b23)
window2.add(b24)
############b##
window3.add(b30)
window3.add(b31)
window3.add(b32)
window3.add(b33)
window3.add(b34)
############b#####
window4.add(b40)
window4.add(b41)
window4.add(b42)
window4.add(b43)
window4.add(b44)


root.mainloop()
