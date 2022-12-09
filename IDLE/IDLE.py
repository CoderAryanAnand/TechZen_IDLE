import tkinter as tk

# TODO: create commands

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

        self.box1Text = tk.Text(self.root, width=1, height=1)
        self.box1Text.pack(fill=tk.BOTH,side=tk.TOP, expand=True)
        self.box2Text = tk.Text(self.root, width=1, height=1)
        self.box2Text.pack(fill=tk.BOTH,side=tk.BOTTOM, expand=True)
    
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