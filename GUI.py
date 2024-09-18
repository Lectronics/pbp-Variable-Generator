from tkinter import *
from Menubar import *
# from generatorFuncts import generateVarFromValue

def createMenu(parent):
    menubar = Menu(parent)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Save", command=SaveVariable)
    filemenu.add_command(label="Write", commmand=WriteVarToFile)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=hello)
    editmenu.add_command(label="Copy", command=hello)
    editmenu.add_command(label="Paste", command=hello)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=hello)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Edit", menu=editmenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    menubar.add_command(label="Quit", command=parent.quit)
    parent.config(menu=menubar)

def createInput(parent):
    name_lbl = Label(parent, text="Var Name: ")
    name_var = StringVar()
    name_entry = Entry(parent, textvariable=name_var)
    name_var.set("MyVar1")
    name_lbl.pack()
    name_entry.pack()

    type_lbl = Label(parent, text="Var Type: ")
    type_spinbox = Spinbox(parent, values=('bit', 'byte', 'word', 'long', 'double'))
    type_lbl.pack()
    type_spinbox.pack()

# def makeEntry(parent, caption, lbl_x, lbl_y, entry_x, entry_y width=None, **options):
#     Label(parent, text=caption).pack(side=LEFT)
#     entry = Entry(parent, **options)
#     if width:
#         entry.config(width=width)
#     entry.pack(side=LEFT)
#     return entry

def hello(self):
    print("hi there, everyone!")


if __name__ == '__main__':

    master = Tk()

    createMenu(master)
    createInput(master)

    mainloop()