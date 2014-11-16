#     t k P h o n e . p y
#
from Tkinter import *


def compile_Start():
    print "compiling..."

def execute_Start():
    print "executing..."

#Window
win = Tk()
win.title("CAT")
win.minsize(1100, 650)

#BACKGROUND
photo = PhotoImage(file="wall.gif")
pic = Label(win, image=photo)
pic.photo = photo
pic.place(x=0, y=0, relwidth=1, relheight=1)

'''photo = Image.open("wall.jpg")
wall = ImageTk.PhotoImage(photo)
label = Label(win, image=wall)
label.image = wall
label.place(x=20, y=20)'''

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

#CODE SECTION
code = Text(win, width=65, height=25) #65, 37
code.insert(INSERT, "#Your code goes here... :D")
code.place(bordermode=OUTSIDE, x=80, y=90, width=450, height=500)
        #Scroll Bar
sb = Scrollbar(win, orient=VERTICAL)
code.configure(yscrollcommand=sb.set)
#sb.pack(side=LEFT,fill=Y)
sb.place(x=520, y=92, width=10, height=497)

#PAINT SECTION
f_paint = Frame(win)
f_paint.pack(side=LEFT)
canvas = Canvas(win, width=450, height=475)
canvas.create_rectangle(0, 25, 450, 475, fill="blue")
canvas.place(bordermode=OUTSIDE, x=630, y=90, width=450, height=500)



win.mainloop()