import GUI as gui
from tkinter import Tk

root = Tk()
root.geometry("650x800")

app = VariableGenerator(master=root)
app.mainloop()

