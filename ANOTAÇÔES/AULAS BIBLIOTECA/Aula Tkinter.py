#Apresentação#

from tkinter import*
from tkinter.ttk import*

master = Tk()

pane = Frame(master)
pane.pack(fiil = BOTH, expand = True)

b1 = Button(pane, text = "Click Me!")
b1.pack(fiil = BOTH, expand = True)

b2 = Button(pane, text = "Click Me!")
b2.pack(fiil = BOTH, expand = True)

master.mainloop()