# -----------------------------------------------------------------------------
# Graphich.py
#
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
# Interfaz grafica para lenguaje CAT 2014
#
# -----------------------------------------------------------------------------

from Tkinter import *
import sys
sys.path.insert(0,"../")
from code import cat
from code import vm

texto = ""

def compile_Start():
    print "compiling..."
    global texto

    #fo = open("input.txt", "w+")
    texto = codex.get("1.0", END)
    #fo.write(texto)

    #cat.cleanTables()
    print texto
    cat.startCompilation(texto)
    cat.output()

    for x in cat.cuadruplos_list:
        x.print_cuadruplo()
    #fo.close()
    print "FINISH!"

def execute_Start():
    print "executing..."
    vm.start()
    #Llama VM

def showCat():
    #BACKGROUND
    photo = PhotoImage(file="cat.gif")
    pic = Label(win, image=photo)
    pic.photo = photo
    pic.place(x=850, y=280, width=45, height=50)
    #canvas.place(bordermode=OUTSIDE, x=630, y=90, width=450, height=500)


#Window
win = Tk()
win.title("CAT")
win.minsize(1100, 650)

#BACKGROUND
photo = PhotoImage(file="wall.gif")
pic = Label(win, image=photo)
pic.photo = photo
pic.place(x=0, y=0, relwidth=1, relheight=1)

#Subtitle
f_title = Frame(win)
f_title.pack()
l = Label(win, text="Welcome to CAT!")
l.place(x=510, y=10)

#BUTTONS SECTION
b1 = Button(win, text="Compile", command = compile_Start)
b2 = Button(win, text="Execute", command = execute_Start)
b1.place(x=225, y=40, width=120, height=25)
b2.place(x=775, y=40, width=120, height=25)

#codex SECTION
codex = Text(win, width=65, height=25) #65, 37
codex.insert(INSERT, "#Your codex goes here... :D")
codex.place(bordermode=OUTSIDE, x=80, y=90, width=450, height=500)
        #Scroll Bar
sb = Scrollbar(win, orient=VERTICAL)
codex.configure(yscrollcommand=sb.set)
#sb.pack(side=LEFT,fill=Y)
sb.place(x=520, y=92, width=10, height=497)
'''
texto = Entry(win)
texto.place(bordermode=OUTSIDE, x=80, y=90, width=450, height=500) '''

#PAINT SECTION
f_paint = Frame(win)
f_paint.pack(side=LEFT)
canvas = Canvas(win, width=450, height=475)

canvas.create_rectangle(0, 0, 450, 475, fill="blue")
canvas.place(bordermode=OUTSIDE, x=630, y=90, width=450, height=500)
showCat()

win.mainloop()










