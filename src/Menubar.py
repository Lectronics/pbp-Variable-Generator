from tkinter.filedialog import askopenfilename, SaveFileDialog, asksaveasfile
from tkinter.simpledialog import askstring

def saveVariable(variable_text):
    # Needs a popup prompting for a filename
    # filename = askstring("Filename", "Please enter a filename.")
    # print(filename)

    # with open(f"{filename}.txt", "x") as file:
        
    with asksaveasfile(filetypes = [("Font Files", ".font")]) as file:
        file.write(variable_text)


def writeVar(variable_text, filename=None):

    if filename == None:
        with askopenfilename(filetypes = [("Font Files", ".font")]) as file:
            file.write(variable_text)


    with open(f"{filename}", "a") as file:
        file.write(variable_text)


def copyVarToClipboard():
    pass


def pasteVarToVarbox():
    pass


def popUpHelp():
    askstring("About", "This is version 0.0.2.3.16 of\npbp Variable Generator. Are you liking it?")


def openVar():
    pass

def openFont():
    pass

# def createMenu(master):
#         # Using master because the menubar has to go on the top-level window. If you try to put the menu on a frame, you get errors
#         master.menubar = Menu(master)

#         # Creating the file dropdown menu
#         master.filemenu = Menu(master.menubar, tearoff=0)
#         master.filemenu.add_command(label="Save", command= lambda: saveVariable(pbp_variable))
#         master.filemenu.add_command(label="Write", command=lambda: writeVar(pbp_variable))

#         # Creating the Edit Dropdown menu
#         master.editmenu = Menu(master.menubar, tearoff=0)
#         # editmenu.add_command(label="Cut", command=hello) # Decided not to use the CUT option
#         master.editmenu.add_command(label="Copy", command=copyVarToClipboard)
#         master.editmenu.add_command(label="Paste", command=pasteVarToVarbox)

#         # Creating the Help Menu which will have an about tab and a help tab
#         #   The help tab wil bring up a popUp that walks you through how to use the generator
#         master.helpmenu = Menu(master.menubar, tearoff=0)
#         master.helpmenu.add_command(label="About", command=popUpHelp)

#         # Adding the subMenus made above to the main menu (menubar)
#         master.menubar.add_cascade(label="File", menu=master.filemenu)
#         master.menubar.add_cascade(label="Edit", menu=master.editmenu)
#         master.menubar.add_cascade(label="Help", menu=master.helpmenu)
#         master.menubar.add_command(label="Quit", command=master.quit)

#         # Assigning this menubar to master which is the root Tk window
#         master.config(menu=master.menubar)
