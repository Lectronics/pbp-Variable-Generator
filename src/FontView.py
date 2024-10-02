from tkinter import *
from tkinter import filedialog

class view(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()

        self.buttons()
        self.viewWindow()


    def buttons(self):

        self.next_btn = Button(self, text="Next", command=self.nextLetter)
        self.load_btn = Button(self, text="Load Font", command=self.loadFont)
        self.back_btn = Button(self, text="Back", command=self.backLetter)

        self.next_btn.pack(side=RIGHT)
        self.load_btn.pack(side=TOP)
        self.back_btn.pack(side=LEFT)


    def viewWindow(self):

        self.text_window = Text(self, height=20, width=40)
        self.text_window.pack()


    def loadFont(self):
        with filedialog.askopenfile() as file:
            self.font = eval(file.read().split('\n')[1])
            self.index = 1
            self.displayChar()


    def displayChar(self):

        self.text_window.delete("1.0", "end")

        self.charString = ''

        for i in self.font[self.index]:
            self.charString += str(i) + '\n'

        self.text_window.insert('1.0', self.charString)


    def nextLetter(self):

        if self.index + 1 < self.font[0][1]:
            self.index += 1
            self.displayChar()

        else:
             pass



    def backLetter(self):

        if self.index - 1 > 0:
            self.index -= 1
            self.displayChar()

        else:
             pass
