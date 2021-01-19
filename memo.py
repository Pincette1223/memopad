from tkinter import *
from tkinter import filedialog

class tkGUi :
    def __init__(self):
        
        self.root = Tk()
        
        menubar = Menu(self.root)
        
        self.text = Text(self.root)
        
        self.text.pack()
        
        filemenu = Menu(menubar, tearoff=0)
        
        menubar.add_cascade(label="File", menu=filemenu)
        
        filemenu.add_command(label="New", command=self.domenu)
        
        filemenu.add_command(label="Open", command=self.Load)
        
        filemenu.add_command(label="Save", command=self.Save)
        
        filemenu.add_command(label="Save as...", command=self.Save)
        
        filemenu.add_separator()
        
        filemenu.add_command(label="Exit", command=self.root.quit)
        
        editmenu = Menu(menubar, tearoff=0)
        
        menubar.add_cascade(label="Edit", menu=editmenu)
        
        editmenu.add_command(label="Copy", command=self.domenu)
        
        editmenu.add_command(label="Paste", command=self.domenu)
        
        editmenu.add_separator()
        
        editmenu.add_command(label="Delete", command=self.domenu)
        
        helpmenu = Menu(menubar, tearoff=0)
        
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        helpmenu.add_command(label="About...", command=self.domenu)
 
        self.root.config(menu=menubar)
        
        self.root.mainloop()


    def Load(self):

        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("text files", "*.txt"),
                                              ("all files", "*.*")))

        print(filename)
        
        data=open(filename,'rt',encoding="utf-8")
        
        self.text.delete('1.0', END)
        
        self.text.insert(END,data.read())

    def Save(self):
        filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                              filetypes=(("text files", "*.txt"),
                                              ("all files", "*.*")))
        
        print(filename)
 
 
    def domenu(self):
    
        print("OK")

if __name__ == '__main__':
 
    Example = tkGUi()
