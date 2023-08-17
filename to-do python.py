import tkinter
from tkinter import *

root= Tk()
root.title("To-Do list")
root.geometry("400x700+400+100")
root.resizable(FALSE,FALSE)

tasklist = []

def openTaskFile():

    try:
        global tasklist
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                tasklist.append(task)
                listbox.insert(END,task)


    except:
        file= open('tasklist.txt', 'w')
        file.close()

def add():
    task  = taskentry.get()
    taskentry.delete(0, END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        tasklist.append(task)
        listbox.insert(END, task)

def delete():
    global tasklist
    task = str(listbox.get(ANCHOR))
    if task in tasklist:
        tasklist.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in tasklist:
                taskfile.write(task+ "\n")

        listbox.delete(ANCHOR)


Imageicon = PhotoImage(file="task.png")
root.iconphoto(False, Imageicon)
Topbar = PhotoImage(file="topbar.png")
Label(root, image=Topbar).pack()
Dotimage = PhotoImage(file="dot.png")
Label(root, image=Dotimage, bg= "#ff9cde").place(x=30, y=25)
heading = Label(root, text="All Tasks", font= "arial 20 bold", fg="black", bg= "#ff9cde")
heading.place(x=130,y=10 )

#main frame
frame =  Frame(root, width=400, height=50, bg ="#ffdddc" )
frame.place(x=0, y=180)
task= StringVar()
taskentry= Entry(frame, width=18, font="arial 20", bg ="#ffdddc", bd=0)
taskentry.place(x=10, y=7)
taskentry.focus()

#add button
button= Button(frame, text="Add", font= "arial 20 bold", width=6, bg="#e05656", fg="#fff", bd=0, command=add)
button.place(x=300,y=0)

#listbox
frame1 = Frame(root, bd=3, width=700, height=500, bg="#ff9cde")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1, font=('arial',13), width=40, height=16, bg="#ff9cde", fg="black", cursor="hand2", selectbackground="#e05656")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

#scrollbar
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete function
Deleteicon = PhotoImage(file="delete.png")
Button(root, image=Deleteicon,bd=0, command= delete).pack(side=BOTTOM,pady=20)

root.mainloop()