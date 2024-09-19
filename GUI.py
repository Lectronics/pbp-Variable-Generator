from tkinter import *
from Menubar import *
# from generatorFuncts import generateVarFromValue
class VariableGenerator(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createMenu()
        self.createInput()
        self.createOutput()

        

        self.name_lbl.grid(row=0, column=0, columnspan=2, padx=3, pady=20)
        self.name_entry.grid(row=0, column=2, columnspan=4, padx=3, pady=20)

        self.type_lbl.grid(row=1, column=0, columnspan=2, padx=3, pady=10)
        self.type_spinbox.grid(row=1, column=2, columnspan=4, padx=3, pady=10)

        self.var_value_lbl.grid(row=2, column=0, columnspan=2)
        self.custom_var_chkbtn.grid(row=2, column=3)
        self.pattern_var_chkbtn.grid(row=2, column=4)

        self.custom_lbl.grid(row=3, column=1, columnspan=2)
        self.custom_entry.grid(row=3, column=3, columnspan=2)

        self.pattern_lbl.grid(row=4, column=1, columnspan=2)
        self.pattern_entry.grid(row=4, column=3, columnspan=2)

        self.output_lbl.grid(row=5, column=0, columnspan=2, padx=3, pady=3)
        self.output_textbox.grid(row=6, column=0, rowspan=5, columnspan=6, padx=3, pady=3)
        self.output_scrollbar.grid(row=6, column=6, rowspan=5, padx=2, pady=3)


    def createMenu(self):
        # Using self.master because the menubar has to go on the top-level window. If you try to put the menu on a frame, you get errors
        self.master.menubar = Menu(self.master)

        # Creating the file dropdown menu
        self.master.filemenu = Menu(self.master.menubar, tearoff=0)
        self.master.filemenu.add_command(label="Save", command=saveVariable)
        self.master.filemenu.add_command(label="Write", command=writeVar)

        # Creating the Edit Dropdown menu
        self.master.editmenu = Menu(self.master.menubar, tearoff=0)
        # editmenu.add_command(label="Cut", command=hello) # Decided not to use the CUT option
        self.master.editmenu.add_command(label="Copy", command=copyVarToClipboard)
        self.master.editmenu.add_command(label="Paste", command=pasteVarToVarbox)

        # Creating the Help Menu which will have an about tab and a help tab
        #   The help tab wil bring up a popUp that walks you through how to use the generator
        self.master.helpmenu = Menu(self.master.menubar, tearoff=0)
        self.master.helpmenu.add_command(label="About", command=popUpHelp)

        # Adding the subMenus made above to the main menu (menubar)
        self.master.menubar.add_cascade(label="File", menu=self.master.filemenu)
        self.master.menubar.add_cascade(label="Edit", menu=self.master.editmenu)
        self.master.menubar.add_cascade(label="Help", menu=self.master.helpmenu)
        self.master.menubar.add_command(label="Quit", command=self.master.quit)

        # Assigning this menubar to self.master which is the root Tk window
        self.master.config(menu=self.master.menubar)


    def createInput(self):
        self.name_lbl = Label(self, text="Var Name:")
        self.name_var = StringVar()
        self.name_entry = Entry(self, textvariable=self.name_var, width=60)
        self.name_var.set("MyVar1")

        self.type_lbl = Label(self, text="Var Type: ")
        self.type_spinbox = Spinbox(self, values=('bit', 'byte', 'word', 'long', 'double'), wrap=True)

        self.var_value_lbl = Label(self, text='Variable Value:')

        self.custom_var = IntVar()
        self.custom_var_chkbtn = Checkbutton(self, text="Custom", variable=self.custom_var, command=self.command_flip_flop)
        self.custom_lbl = Label(self, text="Custom:")
        self.custom_entry_var = StringVar()
        self.custom_entry = Entry(self, textvariable=self.custom_entry_var, width=60)

        self.pattern_var = IntVar()
        self.pattern_var_chkbtn = Checkbutton(self, text="Pattern", variable=self.pattern_var, command=self.pattern_flip_flop)
        self.pattern_lbl = Label(self, text="Pattern:")
        self.pattern_entry_var = StringVar()
        self.pattern_entry = Entry(self, textvariable=self.pattern_entry_var, width=60)

    # def makeEntry(parent, caption, lbl_x, lbl_y, entry_x, entry_y width=None, **options):
    #     Label(parent, text=caption).pack(side=LEFT)
    #     entry = Entry(parent, **options)
    #     if width:
    #         entry.config(width=width)
    #     entry.pack(side=LEFT)
    #     return entry

    def createOutput(self):
        self.output_lbl = Label(self, text="Output:")

        self.output_string = StringVar()
        self.output_scrollbar = Scrollbar(self)
        self.output_textbox = Text(self)
        self.output_string.set("MyVar1 var byte\nMyVar1 = $7f")


    def command_flip_flop(self):
        pass


    def pattern_flip_flop(self):
        pass


if __name__ == '__main__':

    root = Tk()
    root.geometry("600x700")
    app = VariableGenerator(master=root)
    app.mainloop()