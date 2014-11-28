# -----------------------------------------------------------------------------
# Graphic.py
#
# Compiladores - ITESM
# Eduardo Banuelos - Carlos Elizondo
# Interfaz grafica para lenguaje CAT 2014
#
#
''' 
    Graphic.py contiene la interfaz grafica para la implementacion del compilador.
    Se utilzan botones para el control de esta y se muestran dos
    espacios principales uno de input y otro de output.
'''
# -----------------------------------------------------------------------------

from Tkinter import *
#import sys
#sys.path.insert(0,"../")
from code import cat
from code import vm
from random import randint

photo = ""
theCat = ''
toy_list = []
play = False

# *************** BUTTONS ACTIONS ********************

def compile_Start():
    print "compiling..."
    texto = codex.get("1.0", 'end-1c')

    #Clean file
    open('input.txt', 'w+').close()

    #Add code to file
    intext = open('input.txt', 'w+')
    intext.write(texto)
    intext.close()
    
    #Start compilation
    cat.startCompilation()
    cat.output()
    
def execute_Start():
    print "executing..."
    vm.start()
    #Llama VM

    #Animation from the execution output.
    startAnimation()

# *************** ANIMATION ACTIONS ********************

#Cat animation 
def animCat(xPos, yPos):
    global theCat

    #CAT position if new or existing
    photo = PhotoImage(file="cat.gif")
    cat = Label(win, image=photo)
    cat.photo = photo
    if theCat != '':
        theCat.place(x=810 + xPos, y=260 + yPos, width=120, height=132)
    else:
        cat.place(x=810 + xPos, y=260 + yPos, width=120, height=132)
        theCat = cat

#Ball animation 
def animToy():
    global photo
    global toy
    global play 

    play = True

    #BACKGROUND
    xR = randint(-220,200)
    yR = randint(-290,160)
    photo = PhotoImage(file="ball.gif")
    toy = Label(win, image=photo)
    toy.photo = photo
    toy.place(x=850 + xR, y=380 + yR, width=45, height=50)
    toy_list.append(toy)

#Movement of "toy" on screen
def animPlay():
    global play

    if play:
        i = 0
        #Animation timelapse
        while (i < 100):
            for x in toy_list:
                xR = randint(-220, 200)
                yR = randint(-290, 160)
                ball = x
                ball.place(x=850 + xR, y=380 + yR, width=45, height=50)
                canvas.update()
            i += 1

#Start of the animation sequence
def startAnimation():
    global photo 

    #Open instrucction file
    with open('output.txt', 'r+') as animation:
        print "Start Animation:"
        #Iterate through file
        for command in animation:
            command = command.replace("\n", "")
            command = str(command)
            line = command.split(",")
            print line
            #Animation cases
            if line[0] == "newCat":
                print "newCat"
                animCat(0, 0)
            if line[0] == "move":
                animCat(int(line[1]), int(line[2]))
                print line[0]
            if line[0] == "toy":
                animToy()
                print "newToy"
            if line[0] == "clean":
                print "clean"
                canvas.delete("all")
            if line[0] == "play":
                print "LETS PLAY!"
                animPlay()

    animation.close()

# *************** SET GRAPHIC ENVIRONMENT ***************

#Window
win = Tk()
win.title("CAT")
win.minsize(1280, 800)

#BACKGROUND
photo = PhotoImage(file="wall.gif")
pic = Label(win, image=photo)
pic.photo = photo
pic.place(x=0, y=0, relwidth=1, relheight=1)

#BUTTONS SECTION
b1 = Button(win, text="Compile", command = compile_Start)
b2 = Button(win, text="Execute", command = execute_Start)
b3 = Button(win, text="Let's Play!", command = animPlay)
b1.place(x=225, y=40, width=120, height=25)
b2.place(x=775, y=40, width=120, height=25)
b3.place(x=935, y=40, width=120, height=25)

#codex SECTION
codex = Text(win, width=65, height=25) #65, 37
#codex.insert(INSERT, "#Your code goes here... :D")
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

canvas.create_rectangle(0, 0, 450, 510, fill="black")
canvas.create_rectangle(10, 10, 440, 490, fill="white")
canvas.place(bordermode=OUTSIDE, x=630, y=90, width=450, height=500)
#showCat()

win.mainloop()










