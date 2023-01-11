#add widgets to create a UI application program

from tkinter import *
window = Tk()
window.geometry("500x400+10+20")

window.title("My first Python GUI")

#add label widget
#lbl = Label(window, text= "My First UI Python Program",fg = "red",font =("Verdana,16"))
#lbl.place(x=60,y=70)
#add button widget

btn = Button(window,text = "Submit", bg="Blue")
btn.place(x=100, y =150)

#add text field

txtfld = Entry(window,text="This is an entry widget", bd =5)
txtfld.place(x=80,y=100)
def sel():
    selection = "You selected the option" + str(var.get())
    label.config(text = selection)
var = IntVar()
r1 = Radiobutton(window,text="Male", variable= var,value=1,command = sel)
r1.pack(anchor=W)

r2 = Radiobutton(window,text="Female", variable= var,value=2,command = sel)

r2.pack(anchor=W)

label = Label(window)
label.pack()
window.mainloop()