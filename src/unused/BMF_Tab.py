from tkinter import *
def goBack():
    pass

def goNext():
    pass

class BMFTab(Frame):
    def __init__(self, master=None, child=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.child = child # I need to access the child frame of this one so that I can get its variables and have access to its functions
        self.font = []
        self.navigationButtons()
        
    
    def navigationButtons(self):

        back_btn = Button(self, text='Back', command=goBack).pack()
        next_btn = Button(self, text='Next', command=self.goNext).pack()

    def goNext(self):
        self.font.append(self.child.btn_lookup) # Appending the 2D array of the black and white pixels that is currently on the screen.
        self.child.allBlack() # Making all the buttons in the child class BMF_GUI White.
        print(self.font)