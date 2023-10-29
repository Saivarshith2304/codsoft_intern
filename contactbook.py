from tkinter import *  

root = Tk()
root.geometry("400x400")
root.config(bg="cyan")
root.resizable(0,0)
root.title("contact book")

contlist=[]

name = StringVar()
number = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame,orient=VERTICAL)
select = Listbox(frame,yscrollcommand=scroll.set,height=12)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT,fill=Y)
select.pack(side=LEFT,fill=BOTH,expand=1)

def selected():
    return int(select.curselection()[0])

def addcontact():
    contlist.append([name.get(),number.get()])
    select_set()

def edit():
    contlist[selected()] = [name.get(),number.get()]
    select_set()

def delete():
    del contlist[selected()]
    select_set()

def view():
    NAME,PHONE = contlist[selected()]
    name.set(NAME)
    number.set(PHONE)

def exit():
    root.destroy()

def select_set():
    contlist.sort()
    selected.clear(0)
    for name,phone in contlist:
        select.insert(END,name)



select_set()

Label(root,text="NAME", font="arial 15 bold",bg="slategray3").place(x=30,y=20)
Entry(root,textvariable=name).place(x=100,y=20)

Label(root,text="PHONE NO:", font="arial 15 bold",bg="slategray3").place(x=30,y=70)
Entry(root,textvariable=number).place(x=130,y=70)

Button(root,text="ADD",font="arial 12 bold",bg="slategray4",command=addcontact).place(x=50,y=110)
Button(root,text="EDIT",font="arial 12 bold",bg="slategray4",command=edit).place(x=50,y=310)
Button(root,text="DELETE",font="arial 12 bold",bg="slategray4",command=delete).place(x=50,y=210)
Button(root,text="VIEW",font="arial 12 bold",bg="slategray4",command=view).place(x=50,y=160)
Button(root,text="EXIT",font="arial 12 bold",bg="slategray4",command=exit).place(x=300,y=320)