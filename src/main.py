import GeneratorGUI as gui
# import BMF_Tab

import BMFGUI

from tkinter import Tk, ttk

root = Tk()
root.geometry("650x800")

tabbed_pages = ttk.Notebook(root)

variable_tab = gui.VariableGenerator(master=tabbed_pages, root=root)

# bmf_tab = BMF_Tab.BMFTab(master=tabbed_pages)
bmf_gui = BMFGUI.BMF(master=tabbed_pages)
# bmf_tab.child = bmf_gui

tabbed_pages.add(variable_tab, text="Variable Generator")
tabbed_pages.add(bmf_gui, text="Bit Map Font")

tabbed_pages.pack(expand=1, fill="both")

# KeyBinds!!

tabbed_pages.mainloop()

