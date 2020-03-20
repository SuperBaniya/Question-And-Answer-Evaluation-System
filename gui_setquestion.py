from tkinter import *
from tkinter.ttk import *
from sqlcode import *

window = Tk()

window.title("question ZONE")

window.geometry('400x500')

tab_control = Notebook(window)

tab1 = Frame(tab_control)

tab2 = Frame(tab_control)

tab_control.add(tab1, text='ADD MCQ')

tab_control.add(tab2, text='ADD SUBJECTIVE')

tab3 = Frame(tab_control)

tab4 = Frame(tab_control)

tab_control.add(tab3, text='ANSWER MCQ')

tab_control.add(tab4, text='ANSWER SUBJECTIVE')


lbl = Label(tab1, text="Enter The Qestion")
lbl.pack()

q = Entry(tab1, width=50)
q.pack()

lbl2 = Label(tab1, text="Enter A Qestion id")
lbl2.pack()


qid = Entry(tab1, width=10)
qid.pack()

lbl3 = Label(tab1, text="Enter options")
lbl3.pack()
op1 = Entry(tab1, width=10)
op1.pack()

op2 = Entry(tab1, width=10)
op2.pack()

op3 = Entry(tab1, width=10)
op3.pack()

op4 = Entry(tab1, width=10)
op4.pack()


def clicked1():
    combo['values'] = (op1.get(), op2.get(), op3.get(), op4.get())


btn1 = Button(tab1, text="SUBMIT options", command=clicked1)

btn1.pack()


combo = Combobox(tab1)
combo['values'] = ("select answer", "select answer",
                   "select answer", "select answer")

combo.current(1)  # set the selected item

combo.pack()

lbl5 = Label(tab1, text="Enter AUTHOR")
lbl5.pack()
auth = Entry(tab1, width=10)
auth.pack()


lbl6 = Label(tab1, text="CLICK SUBMIT TO SUBMIT")
lbl6.pack()


def clicked():
    q_o_insert_mcq(qid.get(), auth.get(), op1.get(),
                   op2.get(), op3.get(), op4.get(), combo.get(), q.get())
    lbl6.config(text="SUBMITTED")


btn = Button(tab1, text="SUBMIT QUESTION", command=clicked)
btn.pack()

lbl11 = Label(tab2, text="Enter The Qestion")
lbl11.pack()

q11 = Entry(tab2, width=50)
q11.pack()

lbl12 = Label(tab2, text="Enter A Qestion id")
lbl12.pack()

qid12 = Entry(tab2, width=10)
qid12.pack()

lbl13 = Label(tab2, text="Enter AUTHOR")
lbl13.pack()

auth11 = Entry(tab2, width=10)
auth11.pack()


def sub():
    q_o_insert_sub(qid12.get(), auth11.get(), q11.get())
    lbl14.config(text='SUBMITTED')


btn11 = Button(tab2, text="SUBMIT QUESTION", command=sub)
btn11.pack()

lbl14 = Label(tab2, text="")
lbl14.pack()

# answer tabs start:::

comboans = Combobox(tab4, width=70)
g = []
for i in get_subs():
    g.append(" Question ID::  "+str(i[0]) + " ->  " +
             str(i[3]) + "   by AUTHOR =  "+str(i[1]))

comboans['values'] = g

comboans.current(1)  # set the selected item

comboans.pack()


tab_control.pack(expand=1, fill='both')


window.mainloop()
