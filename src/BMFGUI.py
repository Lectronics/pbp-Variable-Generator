from tkinter import *
from tkinter import ttk
from BMFFuncts import *
from tkinter.filedialog import asksaveasfile

class BMF(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.pack()

        self.invisible_image = PhotoImage(width=1, height=1)

        self.startGUI()
        


    def startGUI(self):

        self.start_lbl = Label(self, text="Select Your Font Size: ")
        self.rows_lbl = Label(self, text='Rows:')
        self.columns_lbl = Label(self, text='Columns:')

        self.rows_entry = Entry(self, width=2)
        self.columns_entry = Entry(self, width=2)
        self.rows_entry.insert(0, "8")
        self.columns_entry.insert(0, "5")

        self.name_lbl = Label(self, text='Font Name: ')
        self.name_entry = Entry(self, width=12)
        self.name_entry.insert(0, "Font")

        self.start_btn = Button(self, text='Start!', command=self.userSetup)

        self.start_lbl.grid(row=1, column=1, columnspan=2)

        self.rows_lbl.grid(row=2, column=3)
        self.rows_entry.grid(row=2, column=4, padx=20)

        self.columns_lbl.grid(row=2, column=5)
        self.columns_entry.grid(row=2, column=6, padx=20)

        self.name_lbl.grid(row=2, column=7)
        self.name_entry.grid(row=2, column=8)

        self.start_btn.grid(row=3, column=7, padx=20)


    def userSetup(self):

        # self.fontOptions() # These have been commented out because they are at this moment useless and use the pack manager
        try:
            self.btn_frame.destroy()
        except:
            print('')

        self.start_btn.config(text='Re-Start!')

        self.btn_frame = Frame(self)
        self.btn_frame.grid(row=4, column=1, columnspan=6, padx=40, sticky='nsew')

        self.btn_array = []
        # self.btn_lookup = []

        self.rows = int(self.rows_entry.get())
        self.columns = int(self.columns_entry.get())


        self.char_index = []
        for i in 'abcdefghijklmnopqrstuvwxyz':
            self.char_index.append(i)

        self.font = [[1, 0, self.rows, self.columns]] # Making the font array that as the zero index keeps metadata in the form: []

        self.makeBtns(self.rows, self.columns)
        self.assignCommands()
        self.gridButtons()
        self.navigationButtons()
        self.operationButtons()
        self.indexLabel()


    
    def makeBtns(self, rows, columns):

        # Setting the max size in pixels for the button frame
        btn_size = self.btnSize(rows, columns)
        self.font.append([]) # making a blank array to hold the whole character map that is created in the next for loops

        for x in range(rows):
            # Adding the enpty array for the buttons the next row
            self.btn_array.append([])
            self.font[1].append([])

            for y in range(columns):
                self.font[1][x].append(0)
                self.btn_array[x].append(Button(self.btn_frame, bg='white', image=self.invisible_image, width=btn_size, height=btn_size))


    def btnSize(self, rows, columns):
        #  Based on whatever there are more of (rows or columns), the button width/height is calculated to be within 375 pixels 
        if rows >= columns:
            return round(375 / rows) 
        else:
            return round(375 / columns)


    def assignCommands(self):
        for arr in self.btn_array:
            for btn in arr:
                btn.bind('<Button-1>', self.btnColor)
                # Trying to implement drag the mouse pointer over buttons to change their color too
                # btn.bind('<B1-Motion>', self.btnColor) # Doesn't Work...


    def gridButtons(self):
        for y, arr in enumerate(self.btn_array):
            for x, btn in enumerate(arr):
                btn.grid(row=y, column=x, padx=0, pady=0)


    def getButtonIndexes(self, number):

        rowcount = 0
        if number:
            while number > self.columns: # Deciding what row the button is on. (the buttons are place horizontally across the screen)
                number -= self.columns
                rowcount += 1
        else:
            return 0, 0 # if there is no number passed, that means it was the first button placed (which happens to be at 0, 0)

        if rowcount < self.rows: # This returns the index (starting at zero) so the row count number should always be less than the amount of rows.
            return rowcount, number-1

        else:
            return self.rows-1, self.columns-1


    def btnColor(self, event):
        try:
            index = self.getButtonIndexes(int(str(event.widget)[30:]))
        except ValueError:
            index = [0, 0]

        if self.font[self.font[0][0]][index[0]][index[1]] == 0:
            event.widget.config(bg='black', fg='white', highlightcolor='black', activeforeground='black', highlightbackground='black')
            # event.widget.config(theme='alt')
            self.font[self.font[0][0]][index[0]][index[1]] = 1
        else: 
            event.widget.config(bg='white', fg='black', highlightcolor='white', activeforeground='white', highlightbackground='white')
            # event.widget.config(theme='classic')
            self.font[self.font[0][0]][index[0]][index[1]] = 0

        # print(self.font[self.font[0][0]])



    def allWhite(self):
        for arr in self.btn_array:
            for btn in arr:
                btn.config(bg='white', fg='black', highlightcolor='white', activeforeground='white', highlightbackground='white')
        
        for row in self.font[self.font[0][0]]:
            for i, j in enumerate(row):
                row[i] = 0



    def allBlack(self):
        for arr in self.btn_array:
            for btn in arr:
                btn.config(bg='black', fg='white', highlightcolor='black', activeforeground='black', highlightbackground='black')

        for row in self.font[self.font[0][0]]:
            for i in enumerate(row):
                row[i] = 1


    def getBitmap(self):
        return self.font[self.font[0][0]]


    def loadBitmap(self, index):
        for y, row in enumerate(self.font[index]):
            for x, i in enumerate(row):
                if i == 0:
                    self.btn_array[y][x].config(bg='white', fg='black', highlightcolor='white', activeforeground='white', highlightbackground='white')
                else:
                    self.btn_array[y][x].config(bg='black', fg='white', highlightcolor='black', activeforeground='black', highlightbackground='black')


    def navigationButtons(self):

        self.back_btn = Button(self, text='Back', command=self.goBack)
        self.master.bind('<Left>', self.goBack)
        self.back_btn.grid(row=5, column=1)

        self.next_btn = Button(self, text='Next', command=self.goNext)
        self.master.bind('<Right>', self.goNext)
        self.next_btn.grid(row=5, column=6)

    
    def operationButtons(self):

        self.clear_btn = Button(self, text='Clear', command=self.allWhite)
        self.master.bind("<Control-c>", self.allWhite)
        self.clear_btn.grid(row=5, column=3)

        self.save_btn = Button(self, text='Save', command=self.saveCharacters)
        self.master.bind("Control-s", self.saveCharacters)
        self.save_btn.grid(row=5, column=4)


    def fontOptions(self):

        self.options_lbl = Label(self, text="Number of Sizes:").pack(side='left')
        self.options_entry = Entry(self, width=3).pack(side='left')

        self.scale_lbl = Label(self, text="Font Scale").pack(side='left')
        self.scale_entry = Entry(self, width=3).pack(side='left')
    
    def indexLabel(self):

        self.index_lbl = Label(self, text=f"Character {self.font[0][0]} of {len(self.font) - 1}")
        self.index_lbl.grid(row=7, column=7, pady=10)

        self.char_lbl = Label(self, text="Character Name: ")
        self.char_lbl.grid(row=6, column=6)

        self.char_entry = Entry(self, width=12)
        self.char_entry.insert(0, self.char_index[self.font[0][0] - 1])
        self.char_entry.grid(row=6, column=7)

    
    def updateLabel(self):
        self.index_lbl.config(text=f"Character {self.font[0][0]} of {len(self.font) - 1}")

        self.char_entry.delete(0, END)
        self.char_entry.insert(0, f'{self.char_index[self.font[0][0] - 1]}')


    def goNext(self):

        self.char_index[self.font[0][0] - 1] = self.char_entry.get() 

        if self.font[0][0] + 2 > len(self.font):
           
            self.makeNewChar()
            # self.font.append([])
            # self.font[-1] = self.btn_lookup # Appending the 2D array of the black and white pixels that is currently on the screen.
            self.allWhite() # Making all the buttons in the child class BMF_GUI White.
            self.updateLabel()
            # print(self.font)
        else:
            if self.font[0][0] <= 0:
                pass

            self.font[0][0] += 1

            self.loadBitmap(self.font[0][0])
            self.updateLabel()


    def goBack(self):

        self.char_index[self.font[0][0] - 1] = self.char_entry.get() 

        if self.font[0][0] <= 1:
            pass

        else:
            self.font[0][0] -= 1

            self.loadBitmap(self.font[0][0])
            self.updateLabel()


    def makeNewChar(self):
        # Makes a new character map of zeros in the font variable
        # This along with the goNext function will allow creation of multiple characters
        # and editing of them before saving the font or bitmap to anything.
        # We will make the arrays with the .append feature and multiplication!

        self.font.append([]) # Making the new empty array to store the new character

        self.font[0][0] = len(self.font) - 1 # Setting the character index to the new character
        self.font[0][1] = len(self.font) - 1# Adding 1 to the font length

        for i in range(self.rows):
            self.font[self.font[0][0]].append([])
            for c in range(self.columns):
                self.font[self.font[0][0]][i].append(0)


    def saveCharacters(self):

        self.font[0].append(self.name_entry.get())

        with asksaveasfile(filetypes = [("Font Files", ".font")]) as f:
            f.write("Font as List: \n" + str(self.font) + "\n")
            f.write("Font as Hex: \n" + str(fontToHex(self.font))+ '\n')
            f.write("Char Index: \n" + str(self.char_index[:self.font[0][1]]))

    

if __name__ == '__main__':
    root = Tk()

    app = BMF(root)
    app.mainloop()



