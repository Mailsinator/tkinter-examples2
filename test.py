

import tkinter as tk
from tkinter import *
from tkinter import ttk

class karl( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Karlos")
        self.button1 = Button( self, text = "CLICK HERE", width = 25,
                               command = self.new_window )
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
    def new_window(self):
        self.newWindow = karl2()
class karl2(Frame):
    def __init__(self):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("karlos More Window")
        new.button = tk.Button(  text = "PRESS TO CLOSE", width = 25,
                                 command = self.close_window )
        new.button.pack()
    def close_window(self):
        self.destroy()
def main():
    karl().mainloop()
if __name__ == '__main__':
    main()

    from tkinter import *

    window = Tk()

    window.title("Hello custom")
    window.geometry('1200x600')

    lbl = Label(window, text="TEST WINDOW")
    lbl.grid(column=10, row=0)

    lbl1 = Label(window, text="Hello")
    lbl1.grid(column=1, row=1)
    txt = Entry(window, width=10)
    txt.grid(column=1, row=2)


    def clicked():
        lbl1.configure(text="You have changed something")
        btn = Button(window, text="Click me", command=clicked)
        btn.grid(colum=1, row=0)
        lbl2 = Label(window, text="Dont press next button ")
        lbl2.grid(colum=1, row=6)
        txt = Entry(window, width=10)
        txt.grid(colum=1, row=7)
        txt.config = lbl2


    window.mainloop()

from tkinter import *

window = Tk()

window.title("Hello custom")
window.geometry('1200x600')

lbl = Label(window , text = "TEST WINDOW")
lbl.grid(column = 10,row = 0)

lbl1 = Label(window , text = "Hello")
lbl1.grid(column = 1,row = 1)
txt = Entry(window,width = 10)
txt.grid(column = 1, row = 2)

def clicked():
    lbl1.configure(text =  "You have changed something")
    btn = Button(window,text = "Click me" , command = clicked )
    btn.grid(colum =1, row= 0)
    lbl2 = Label(window,text = "Dont press next button ")
    lbl2.grid(colum = 1, row = 6)
    txt= Entry(window,width = 10 )
    txt.grid(colum = 1, row = 7 )
    txt.config = lbl2

window.mainloop()

from tkinter import *
from tkinter import messagebox


def top():
    if entry1.get() == "messagebox":
       log.destroy()
       root.deiconify()
    else:
       messagebox.showerror("error", "try again")
       messagebox.showinfo("my message","this is an example of showinfo\nmessagebox")
       messagebox.showwarning("warning", "show warning example in tkinter" )


root = Tk()
root.geometry("400x400")

log = Toplevel(root)
log.geometry("200x200")


label1 = Label(log, text="password")
entry1 = Entry(log)
button1 = Button(log, text="login", command=top)

label1.pack()
entry1.pack()
button1.pack(side="bottom")

lab = Label(root, text="welcome bro").pack()


root.withdraw()
root.mainloop()
