from tkinter import *
from tkinter import ttk
k=0
def clicker(event):
    global k
    k += 1
    lbl.configure(text=k)

def clicker1(event):
    global k
    if k > 0:
        k-=1
    lbl.configure(text=k)

def entry_to_label(event):
    text = ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)

def choosed():
    text = var.get()
    ent.insert(END, text)

def new_window(ind:int):
    def tab_name(ind:int):
        newwindow.title(texts[ind])
    newwindow = Toplevel()
    tabs = ttk.Notebook(newwindow)
    texts = ["First","Second","Third","Fourth"]
    tab = []
    for i in range(len(texts)):
        tab.append("tab"+str(i)) #tab0 , tab1, tab2
        tab[i] = Frame(tabs)
        tabs.add(tab[i],text = texts[i])    
        tab[i].bind("<Button-1>", tab_name(i))
    tabs.grid(column = 0, row = 0)
    tabs.select(ind)
    newwindow.title(texts[ind])
    newwindow.mainloop()

root = Tk()
root.title("My first window.")
root.geometry("800x320")
frm = ttk.Frame(root, padding=10)
menu = Menu(root)
root.config(menu=menu)
m1 = Menu(menu)
menu.add_cascade(label="Tabs",menu = m1)
m1.add_command(label="Card1", accelerator = "Command+A", command = lambda:new_window(0))
m1.add_command(label="Card2", accelerator = "Command+B", command = lambda:new_window(1))
m1.add_command(label="Card3", accelerator = "Command+C", command = lambda:new_window(2))
m1.add_command(label="Card4", accelerator = "Command+D", command = lambda:new_window(3))
var = IntVar() #IntVar() or StringVar()

ttk.Label(frm, text="Hello World!").pack()
ttk.Button(frm, text="Quit", command=root.destroy).pack()
ttk.Button(frm, text="Start", command = root.destroy).pack()
lbl = Label(root,
            text = ". . .",
            font = "Comic_Sans_MS 15")
btn = Button(frm, 
             text = "Vajuta siia",
             font = "Comic_Sans_MS 15",
             fg = "Blue", 
             bg = "#148038",
             relief = GROOVE,
             width = 15,
             height = 2,)
ent = Entry(root, 
            fg = "Blue",
            bg = "#148038",
            width = 15,
            justify = CENTER)



r1 = Radiobutton(root,
                text = "First",
                fg = "Blue",
                font = "Comic_Sans_MS 15",
                bg = "#148038",
                width = 15,
                variable=var,
                value = 1,
                command = choosed)
r2 = Radiobutton(root,
                text = "Second",
                fg = "Blue",
                bg = "#148038",
                font = "Comic_Sans_MS 15",
                width = 15,
                variable=var,
                value = 2,
                command = choosed)

btn.bind("<Button-1>",clicker)#LKM
btn.bind("<Button-3>",clicker1)#PKM
ent.bind("<Return>",entry_to_label)#Enter

frm.pack()
btn.pack()
lbl.pack()
ent.pack()
r1.pack(side=LEFT)
r2.pack(side = LEFT)

root.mainloop()
