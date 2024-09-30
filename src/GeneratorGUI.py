from tkinter import *
import Menubar
from generatorFuncts import generateVarFromValue as gen
from GUI_Vars import placeGrid
from GUI_Vars import custom_entry_initial_value as ceiv
# from generatorFuncts import generateVarFromValue


class VariableGenerator(Frame):

    def __init__(self, master=None, root=None, lbl_anchor=NE, entry_anchor=NW):
        super().__init__(master)
 
        self.master = master # setting the root window so that it is accessable from this class
        self.root = root
        self.pack() # Packing the frame onto the Root window
        self.createMenu() # Creating the Menubar at the top of the screen
        self.createInput()
        self.createOutput()
        self.value = 0
        self.lbl_anchor = lbl_anchor
        self.entry_anchor = entry_anchor
        self.pbp_variable = self.output_textbox.get('1.0')
        self.gridWidgets()
        self.makeVar()
        # self.keybinds()


    def createMenu(self):
        # Using self.master because the menubar has to go on the top-level window. If you try to put the menu on a frame, you get errors
        self.root.menubar = Menu(self.root)

        # Creating the file dropdown menu
        self.root.filemenu = Menu(self.root.menubar, tearoff=0)
        self.root.filemenu.add_command(label="Save", command= lambda: Menubar.saveVariable(self.pbp_variable))
        self.root.filemenu.add_command(label="Write", command=lambda: Menubar.writeVar(self.pbp_variable))
        # self.root.filemenu.add_command(label="Open", command=lambda: Menubar.openVar(self.pbp_variable))

        self.root.openoptions = Menu(self.root.filemenu, tearoff=0)
        self.root.openoptions.add_command(label="Open Variable", command=Menubar.openVar())
        self.root.openoptions.add_command(label="Open Font", command=Menubar.openFont())

        self.root.filemenu.add_cascade(label="Open",menu=self.root.openoptions)

        # Creating the Edit Dropdown menu
        self.root.editmenu = Menu(self.root.menubar, tearoff=0)
        # editmenu.add_command(label="Cut", command=hello) # Decided not to use the CUT option
        self.root.editmenu.add_command(label="Copy", command=Menubar.copyVarToClipboard)
        self.root.editmenu.add_command(label="Paste", command=Menubar.pasteVarToVarbox)

        # Creating the Help Menu which will have an about tab and a help tab
        #   The help tab wil bring up a popUp that walks you through how to use the generator
        self.root.helpmenu = Menu(self.root.menubar, tearoff=0)
        self.root.helpmenu.add_command(label="About", command=Menubar.popUpHelp)

        # Adding the subMenus made above to the main menu (menubar)
        self.root.menubar.add_cascade(label="File", menu=self.root.filemenu)
        self.root.menubar.add_cascade(label="Edit", menu=self.root.editmenu)
        self.root.menubar.add_cascade(label="Help", menu=self.root.helpmenu)
        self.root.menubar.add_command(label="Quit", command=self.root.quit)

        # Assigning this menubar to self.root which is the root Tk window
        self.root.config(menu=self.root.menubar)


    def createInput(self):

        # Creating all of the input related widgets and variables

        self.name_lbl = Label(self, text="Var Name:")
        self.name_var = StringVar()
        self.name_entry = Entry(self, textvariable=self.name_var, width=60)
        self.name_var.set("MyVar1")

        self.type_lbl = Label(self, text="Var Type:")
        self.type_spinbox = Spinbox(self, values=('byte', 'word', 'long', 'double', 'bit'), wrap=True)

        self.var_value_lbl = Label(self, text='Variable Value:')

        self.custom_var = IntVar()
        self.custom_var_chkbtn = Checkbutton(self, text=" Custom:", variable=self.custom_var, command=self.command_flip_flop)
        self.custom_var_chkbtn.select()
        self.custom_lbl = Label(self, text="Custom:")
        self.custom_entry = Entry(self, width=60)
        self.custom_entry.insert(0, ceiv)

        self.pattern_var = IntVar()
        self.pattern_var_chkbtn = Checkbutton(self, text=" Pattern:", variable=self.pattern_var, command=self.pattern_flip_flop)
        self.pattern_lbl = Label(self, text="Pattern:")
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

        # Making all of the output related widgets

        self.output_lbl = Label(self, text="Output:")

        self.output_string = "MyVar1 var byte\nMyVar1 = $7f\n" # To have something to display in the output box of the window

            # self.output_string = StringVar()

        # Setting up the output textbox with a scrollbar for easier navigation.

        self.output_textbox = Text(self, height=40)
        self.output_scrollbar = Scrollbar(self, command=self.output_textbox.yview)
        self.output_textbox.insert(index='1.0', chars=self.output_string)
        self.output_textbox['yscrollcommand'] = self.output_scrollbar.set
            # self.output_textbox.configure(scrollregion=self.output_textbox.bbox(index=))
            # self.output_string.set("MyVar1 var byte\nMyVar1 = $7f")

        self.generate_var = Button(self, text='Make Var!', command=self.makeVar)


    def gridWidgets(self):

        # Placing all of the widgets in a grid that is convienently laid out for readability!

        self.name_lbl.grid(                 row=0, column=1, rowspan=1,  columnspan=1, padx=20,  pady=10, sticky=self.lbl_anchor)
        self.name_entry.grid(               row=0, column=2, rowspan=1,  columnspan=3, padx=10,  pady=10, sticky=self.entry_anchor)

        self.type_lbl.grid(                 row=1, column=1, rowspan=1,  columnspan=1, padx=20,  pady=10, sticky=self.lbl_anchor)
        self.type_spinbox.grid(             row=1, column=2, rowspan=1,  columnspan=3, padx=10,  pady=10, sticky=self.entry_anchor)

        self.var_value_lbl.grid(            row=2, column=1, rowspan=1,  columnspan=1, padx=0,   pady=10,  sticky=self.lbl_anchor)
        # self.custom_var_chkbtn.grid(        row=2, column=3, rowspan=1,  columnspan=1, padx=3,   pady=10)            
        # self.pattern_var_chkbtn.grid(       row=2, column=4, rowspan=1,  columnspan=1, padx=3,   pady=10)            

        self.custom_var_chkbtn.grid(        row=3, column=1, rowspan=1,  columnspan=2, padx=3,   pady=10, sticky=self.lbl_anchor)
        self.custom_entry.grid(             row=3, column=3, rowspan=1,  columnspan=2, padx=3,   pady=10, sticky=self.entry_anchor)

        self.pattern_var_chkbtn.grid(       row=4, column=1, rowspan=1,  columnspan=2, padx=3,   pady=10, sticky=self.lbl_anchor)
        self.pattern_entry.grid(            row=4, column=3, rowspan=1,  columnspan=1, padx=3,   pady=10, sticky=self.entry_anchor)
        self.pattern_repeat_spinbox.grid(   row=4, column=4, rowspan=1,  columnspan=1, padx=0,   pady=0 )

        self.generate_var.grid(             row=5, column=4, rowspan=1,  columnspan=1, padx=3,   pady=10)

        self.output_lbl.grid(               row=6, column=1, rowspan=1,  columnspan=1, padx=10,  pady=40, sticky=self.lbl_anchor)
        self.output_textbox.grid(           row=7, column=0, rowspan=5,  columnspan=6, padx=3,   pady=3,  sticky='nsew')
        self.output_scrollbar.grid(         row=7, column=6, rowspan=6,  columnspan=1, padx=2,   pady=3,  sticky='nsew')


    def placeWidgets(self):

        # To Try to use the place method for the widgets instead of the grid method... This did not work so well
 
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

        if self.custom_var.get() == 1:
            self.value = self.custom_entry.get()
        else:
            try:
                # Sets the value of the self.value to the user specified pattern and pattern repitition
                self.value = self.pattern_entry.get() * int(self.pattern_repeat_spinbox.get())
            except:
                # Defaults to 10 repetitions of the pattern if the value in the spinbox is invalid
                self.value = self.pattern_entry.get() * 10 

        # Clearing the output text box

        self.output_textbox.delete('1.0', 'end')

        # Setting the output text box to the new variable!
        self.pbp_variable = gen(self)
        self.output_textbox.insert('1.0', self.pbp_variable)


    def keybinds(self):
        self.master.bind('<Return>',lambda event:self.makeVar())
        # self.master.bind("<esc>", lambda event:self.master.quit)


    def openVar(self):

        with askopenfilename(filetypes = [("Variable Files", ".pyVar")]) as file:
            self.opened_variable = file.read 

    
    def openFont(self):

        with askopenfilename(filetypes = [("Font Files", ".font")]) as file:
            self.opened_font = file.read 

            

if __name__ == '__main__':

    root = Tk()
    root.geometry("650x800")
    app = VariableGenerator(master=root)
    app.mainloop()