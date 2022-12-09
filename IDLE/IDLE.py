import tkinter as tk
from tkinter.constants import VERTICAL

# TODO: create commands
# https://stackoverflow.com/questions/68956736/how-to-change-the-height-or-width-of-tkinter-widget-with-mouse-drag-after-ini

VERSION = "0.0.1"

class MyApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title(f"TechZen IDLE v.{VERSION}")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.update()

        self.menubar = tk.Menu(self.root, tearoff=0)
        self.root.config(menu=self.menubar)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.newfile)
        self.filemenu.add_command(label="Open", command=self.openfile)
        self.filemenu.add_command(label="Save", command=self.savefile)
        self.filemenu.add_command(label="Save as", command=self.saveas)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exitwindow)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.runmenu = tk.Menu(self.menubar, tearoff=0)
        self.runmenu.add_command(label="Run", command=self.run)
        self.menubar.add_cascade(label="Run", menu=self.runmenu)

        self.frame_navigator = tk.PanedWindow(self.root, orient=VERTICAL)

        self.frame_navigator.configure(background="white", width=300, height=300)
        self.frame_navigator.pack_propagate(0)

        self.box1 = tk.Text(self.frame_navigator)
        self.frame_navigator.add(self.box1)

        self.box2 = tk.Text(self.frame_navigator, exportselection=False, state=tk.DISABLED)
        self.frame_navigator.add(self.box2)

        self.frame_navigator.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
    
    def newfile():
        pass

    def openfile():
        pass

    def savefile():
        pass

    def saveas():
        pass

    def exitwindow():
        pass

    def run():
        pass


App = MyApp()
App.root.mainloop()