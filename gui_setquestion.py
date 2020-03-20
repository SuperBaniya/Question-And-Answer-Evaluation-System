from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
from sqlcode import *

window = Tk()

window.title("question ZONE")

window.geometry('450x550')

tab_control = Notebook(window)

tab1 = Frame(tab_control)

tab2 = Frame(tab_control)

tab_control.add(tab1, text='ADD MCQ')

tab_control.add(tab2, text='ADD SUBJECTIVE')

tab3 = Frame(tab_control)

tab4 = Frame(tab_control)

tab_control.add(tab3, text='ANSWER MCQ')

tab_control.add(tab4, text='ANSWER SUBJECTIVE')

tab5 = Frame(tab_control)

tab_control.add(tab5, text='EVALUATE')


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
a = []
for i in get_subs():
    g.append(str(i[3]))
    a.append(int(i[0]))

comboans['values'] = g

comboans.current(0)  # set the selected item
comboans.pack()

lbl15 = Label(tab4, text="")
lbl15.pack()
lbl16 = Label(tab4, text="TYPE ANSWER BELOW")
lbl16.pack()

txtans = scrolledtext.ScrolledText(tab4, width=40, height=10)
txtans.insert(INSERT, '')
txtans.pack()

lbl16 = Label(tab4, text="TYPE YOUR NAME BELOW")
lbl16.pack()

opsubans = Entry(tab4, width=10)
opsubans.pack()


def subans():
    sub_ans_sub(a[g.index(comboans.get())],
                opsubans.get(), txtans.get(1.0, END))
    print(comboans.get())
    print(a[g.index(comboans.get())])


btnanssub = Button(tab4, text="SUBMIT ANSWER", command=subans)
btnanssub.pack()

comboansmcq = Combobox(tab3, width=70)
r = []
b = []
ch = []
ans = []
qids = []
for i in get_mcqs():
    r.append(str(i[3]))
    b.append(int(i[0]))
    ch.append([str(i[5]), str(i[6]), str(i[7]), str(i[8])])
    ans.append(str(i[9]))

comboansmcq['values'] = r

comboansmcq.current(0)  # set the selected item
comboansmcq.pack()

lbl15mcq = Label(tab3, text="")
lbl15mcq.pack()


def update():
    comboansmcqch['values'] = ch[r.index(comboansmcq.get())]


btnansmcqup = Button(tab3, text="Update Options", command=update)
btnansmcqup.pack()

lbl17mcq = Label(tab3, text="choose ANSWER BELOW")
lbl17mcq.pack()
comboansmcqch = Combobox(tab3, width=70)
comboansmcqch['values'] = ch[r.index(comboansmcq.get())]

comboansmcqch.current(0)  # set the selected item
comboansmcqch.pack()


lbl16mcq = Label(tab3, text="TYPE YOUR NAME BELOW")
lbl16mcq.pack()

opmcqans = Entry(tab3, width=10)
opmcqans.pack()


def mcqans():
    ansmcq = comboansmcqch.get()
    qidmcq = b[r.index(comboansmcq.get())]
    realans = ans[r.index(comboansmcq.get())]
    if(ansmcq == realans):
        marksmcq = 4
    else:
        marksmcq = 0
    sub_ans_mcq(qidmcq, opmcqans.get(), ansmcq, marksmcq)


btnansmcq = Button(tab3, text="SUBMIT ANSWER", command=mcqans)
btnansmcq.pack()


evalcombobox = Combobox(tab5, width=70)
substoeval = get_subs_toeval()
cbeval = []
aids = []
quidev = []
ansev = []
for i in substoeval:
    cbeval.append(str(i[3])+" "+str(i[5]))
    quidev.append(i[0])
    ansev.append(i[7])
    aids.append(i[5])
evalcombobox['values'] = cbeval

evalcombobox.pack()

labelevq = Label(tab5)
labelevq.pack()
labeleva = Label(tab5)
labeleva.pack()


def evupdate():
    index = cbeval.index(evalcombobox.get())
    labelevq.config(text=evalcombobox.get())
    labeleva.config(text=""+str(ansev[index]))


evupdate = Button(tab5, text="update", command=evupdate)
evupdate.pack()

enter_marks = Entry(tab5, width=5)
enter_marks.pack()

enter_eval_name = Entry(tab5, width=10)
enter_eval_name.pack()


def updatemarks():
    index = cbeval.index(evalcombobox.get())
    add_marks_for_sub(aids[index], quidev[index],
                      enter_eval_name.get(), enter_marks.get())


marksbtn = Button(tab5, text="enter marks", command=updatemarks)
marksbtn.pack()


tab_control.pack(expand=1, fill='both')


window.mainloop()
