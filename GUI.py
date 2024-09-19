from tkinter import *
from Menubar import *
from generatorFuncts import generateVarFromValue as gen
from GUI_Vars import placeGrid
from GUI_Vars import custom_entry_initial_value as ceiv
# from generatorFuncts import generateVarFromValue


class VariableGenerator(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createMenu()
        self.createInput()
        self.createOutput()
        self.gridWidgets()


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
        self.name_lbl = Label(self, text="Var Name:", anchor='e')
        self.name_var = StringVar()
        self.name_entry = Entry(self, textvariable=self.name_var, width=60)
        self.name_var.set("MyVar1")

        self.type_lbl = Label(self, text="Var Type:", anchor='e')
        self.type_spinbox = Spinbox(self, values=('byte', 'word', 'long', 'double', 'bit'), wrap=True)

        self.var_value_lbl = Label(self, text='Variable Value:', anchor='e')

        self.custom_var = IntVar()
        self.custom_var_chkbtn = Checkbutton(self, text="Custom", variable=self.custom_var, command=self.command_flip_flop)
        self.custom_var_chkbtn.select()
        self.custom_lbl = Label(self, text="Custom:", anchor='e')
        self.custom_entry = Entry(self, width=60)
        self.custom_entry.insert(0, ceiv)

        self.pattern_var = IntVar()
        self.pattern_var_chkbtn = Checkbutton(self, text="Pattern", variable=self.pattern_var, command=self.pattern_flip_flop)
        self.pattern_lbl = Label(self, text="Pattern:", anchor='e')
        self.pattern_entry = Entry(self, width=35)
        self.pattern_entry.insert(0, "0x00, 0xff, 0x00, 0x00, 0xff")
        self.pattern_entry.config(state=DISABLED)
        self.pattern_repeat_spinbox = Spinbox(self, from_=2, to=256, state=DISABLED)

    # def makeEntry(parent, caption, lbl_x, lbl_y, entry_x, entry_y width=None, **options):
    #     Label(parent, text=caption).pack(side=LEFT)
    #     entry = Entry(parent, **options)
    #     if width:
    #         entry.config(width=width)
    #     entry.pack(side=LEFT)
    #     return entry

    def createOutput(self):
        self.output_lbl = Label(self, text="Output:", anchor='e')

        self.output_string = "MyVar1 var byte\nMyVar1 = $7f\n" * 40

        # self.output_string = StringVar()
        self.output_textbox = Text(self, height=40)
        self.output_scrollbar = Scrollbar(self, command=self.output_textbox.yview)
        self.output_textbox.insert(index='1.0', chars=self.output_string)
        self.output_textbox['yscrollcommand'] = self.output_scrollbar.set
        # self.output_string.set("MyVar1 var byte\nMyVar1 = $7f")

        self.generate_var = Button(self, text='Make Var!', command=self.makeVar)


    def gridWidgets(self):

        self.name_lbl.grid(                 row=0, column=1,            columnspan=1, padx=20, pady=10)
        self.name_entry.grid(               row=0, column=2,            columnspan=3, padx=10, pady=10)

        self.type_lbl.grid(                 row=1, column=0,            columnspan=2, padx=3, pady=10)
        self.type_spinbox.grid(             row=1, column=0,            columnspan=4, padx=146, pady=10)

        self.var_value_lbl.grid(            row=2, column=0,            columnspan=2)
        self.custom_var_chkbtn.grid(        row=2, column=3,                          padx=3, pady=10)            
        self.pattern_var_chkbtn.grid(       row=2, column=4,                          padx=3, pady=10)            

        self.custom_lbl.grid(               row=3, column=1,            columnspan=2, padx=3, pady=10)
        self.custom_entry.grid(             row=3, column=3,            columnspan=2, padx=3, pady=10)

        self.pattern_lbl.grid(              row=4, column=1,            columnspan=2, padx=3, pady=10)
        self.pattern_entry.grid(            row=4, column=3,            columnspan=1, padx=3, pady=10)
        self.pattern_repeat_spinbox.grid(   row=4, column=4)

        self.generate_var.grid(             row=5, column=4,                          padx=3, pady=10)

        self.output_lbl.grid(               row=6, column=1,                          padx=10, pady=40)
        self.output_textbox.grid(           row=7, column=0, rowspan=5, columnspan=6, padx=3, pady=3)
        self.output_scrollbar.grid(         row=7, column=6, rowspan=6,               padx=2, pady=3)


    def placeWidgets(self):

        self.name_lbl.place(x=placeGrid[0][0], y=placeGrid[1][0], anchor='w')
        self.name_entry.place(x=placeGrid[0][1], y=placeGrid[1][0], anchor='w')
     
        self.type_lbl.place(x=placeGrid[0][0], y=placeGrid[1][1], anchor='w')
        self.type_spinbox.place(x=placeGrid[0][1], y=placeGrid[1][1], anchor='w')

        self.var_value_lbl.place(x=placeGrid[0][0], y=placeGrid[1][2], anchor='w')

        self.custom_var_chkbtn.place(x=placeGrid[0][2], y=placeGrid[1][2], anchor='w')
        self.pattern_var_chkbtn.place(x=placeGrid[0][4], y=placeGrid[1][2], anchor='w')

        self.custom_lbl.place(x=placeGrid[0][1], y=placeGrid[1][3], anchor='w')
        self.custom_entry.place(x=placeGrid[0][3], y=placeGrid[1][3], anchor='w')

        self.pattern_lbl.place(x=placeGrid[0][1], y=placeGrid[1][4], anchor='w')
        self.pattern_entry.place(x=placeGrid[0][3], y=placeGrid[1][4], anchor='w')

        self.output_lbl.place(x=placeGrid[0][1], y=placeGrid[1][5], anchor='w')

        self.output_textbox.place(x=placeGrid[0][1], y=placeGrid[1][6], anchor='w')
        self.output_scrollbar.place(x=placeGrid[0][1], y=placeGrid[1][6], anchor='w')


    def command_flip_flop(self):

        self.pattern_var_chkbtn.toggle()
        self.setVarEntryState()
        # if self.custom_var.get == 1:
        #     self.custom_entry.config(state=DISABLED)
        #     self.pattern_entry.config(state=NORMAL)
        #     self.pattern_var_chkbtn.deselect()
        # else:
        #     self.custom_entry.config(state=NORMAL)
        #     self.pattern_entry.config(state=DISABLED)
        #     self.pattern_var_chkbtn.select()


    def pattern_flip_flop(self):

        self.custom_var_chkbtn.toggle()
        self.setVarEntryState()
        # if self.pattern_var.get == 1:
        #     self.custom_entry.config(state=DISABLED)
        #     self.pattern_entry.config(state=NORMAL)
        #     self.custom_var_chkbtn.deselect()
        # else:
        #     self.custom_entry.config(state=NORMAL)
        #     self.pattern_entry.config(state=DISABLED)
        #     self.custom_var_chkbtn.select()

    def setVarEntryState(self):

        # Sets the states of the variable entry boxes depending on which of the checkboxes is checked
        if self.custom_var.get() == 1:
            self.custom_entry.config(state=NORMAL)
            self.pattern_entry.config(state=DISABLED)
            self.pattern_repeat_spinbox.config(state=DISABLED)
        else:
            self.custom_entry.config(state=DISABLED)
            self.pattern_entry.config(state=NORMAL)
            self.pattern_repeat_spinbox.config(state=NORMAL)


    def makeVar(self):
        # Clearing the output text box
        self.output_textbox.delete('1.0', 'end')

        # Setting the output text box to the new variable!
        self.output_textbox.insert('1.0', gen(self))


if __name__ == '__main__':

    root = Tk()
    root.geometry("650x700")
    app = VariableGenerator(master=root)
    app.mainloop()