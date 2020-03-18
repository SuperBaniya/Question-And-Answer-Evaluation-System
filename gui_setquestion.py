from tkinter import *
from tkinter.ttk import *
from sqlcode import *


window = Tk()

window.title("question ZONE")

window.geometry('350x700')

lbl = Label(window, text="Enter The Qestion")
lbl.pack()

q = Entry(window, width=50)
q.pack()

lbl2 = Label(window, text="Enter A Qestion id")
lbl2.pack()

qid = Entry(window, width=10)
qid.pack()

lbl3 = Label(window, text="Enter options")
lbl3.pack()
op1 = Entry(window, width=10)
op1.pack()

op2 = Entry(window, width=10)
op2.pack()

op3 = Entry(window, width=10)
op3.pack()

op4 = Entry(window, width=10)
op4.pack()


def clicked1():
    combo['values'] = (op1.get(), op2.get(), op3.get(), op4.get())


btn1 = Button(window, text="SUBMIT options", command=clicked1)

btn1.pack()


combo = Combobox(window)
combo['values'] = ("select answer", "select answer",
                   "select answer", "select answer")

combo.current(1)  # set the selected item

combo.pack()

lbl5 = Label(window, text="Enter AUTHOR")
lbl5.pack()
auth = Entry(window, width=10)
auth.pack()


lbl6 = Label(window, text="CLICK SUBMIT TO SUBMIT")
lbl6.pack()


def clicked():
    q_o_insert(qid.get(), auth.get(), op1.get(),
               op2.get(), op3.get(), op4.get(), combo.get())
    lbl6.config(text="SUBMITTED")


btn = Button(window, text="SUBMIT QUESTION", command=clicked)

btn.pack()

window.mainloop()
