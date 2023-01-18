from tkinter import *
win = Tk()

#add widgets
class MyWin:
    def __init__(self,win):
        self.lbl1 = Label(win,text="My First Standard Calculator")
        self.lbl1.place(x=200,y=20)
        self.lbl2 = Label(win,text="1st No.")
        self.lbl2.place(x=100,y=50)
        self.txt1 = Entry(win,bd=2)
        self.txt1.place(x=150,y=50)
        self.lbl3 = Label(win,text="2nd No.")
        self.lbl3.place(x=100,y=80)
        self.txt2 = Entry(win,bd=2)
        self.txt2.place(x=150,y=80)
        self.lbl4= Label(win,text="Result")
        self.lbl4.place(x=100,y=120)
        self.txt3 = Entry(win,bd=2)
        self.txt3.place(x=150,y=120)
        self.btn1 = Button(win,text="Addition")
        self.btn1.bind('<Button-1>',self.addition)
        self.btn1.place(x=150,y=150)
        self.btn2 = Button(win, text="Subtraction", command = self.subtraction)
        self.btn2.place(x=220, y=150)

    def addition(self,event):
        self.txt3.delete(0,'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1+num2
        self.txt3.insert(END,str(result))

    def subtraction(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 - num2
        self.txt3.insert(END, str(result))
mywin = MyWin(win)


win.geometry("500x400+10+10")
win.title("Standard Calculator")
win.mainloop()
