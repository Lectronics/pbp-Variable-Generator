from tkinter.filedialog import askopenfilename, SaveFileDialog, asksaveasfile
from tkinter.simpledialog import askstring

def saveVariable(variable_text):
    # Needs a popup prompting for a filename
    # filename = askstring("Filename", "Please enter a filename.")
    # print(filename)

    # with open(f"{filename}.txt", "x") as file:
        

    with asksaveasfile() as file:
        file.write(variable_text)


def writeVar(variable_text, filename=None):

    if filename == None:
        filename = askopenfilename()

    with open(f"{filename}", "a") as file:
        file.write(variable_text)


def copyVarToClipboard():
    pass


def pasteVarToVarbox():
    pass


def popUpHelp():
    askstring("About", "This is version 0.0.2.3.16 of\npbp Variable Generator. Are you liking it?")