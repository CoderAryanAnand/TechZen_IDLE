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

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command("New", command=newfile)
        self.filemenu.add_command("Open", command=openfile)
        self.filemenu.add_command("Save", command=savefile)
        self.filemenu.add_command("Save as", command=saveas)
        self.filemenu.add_separator()
        self.filemenu.add_command("Exit", command=exit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.runmenu = tk.Menu(self.menubar, tearoff=0)
        self.runmenu.add_command("Run", command=run)
        self.menubar.add_cascade(label="Run", menu=self.runmenu)

        self.box1Text = tk.Text(self.root, width=1, height=1)
        self.box1Text.pack(fill=tk.BOTH,side=tk.TOP, expand=True)
        self.box2Text = tk.Text(self.root, width=1, height=1)
        self.box2Text.pack(fill=tk.BOTH,side=tk.BOTTOM, expand=True)

App = MyApp()
App.root.mainloop()