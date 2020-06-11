from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

#main window
win=Tk()
win.title("Untitled - Notepad")
win.geometry("600x300")

#variables
file=None

class functions():
    def clear():
        txtPad.delete(1.0, END)
    
    def new():
        global file
        file=None
        win.title("Untitled - Notepad")
        txtPad.delete(1.0, END)

    def exit():
        win.destroy()

    def save_file():
        global file
        if file==None:
            file=filedialog.asksaveasfilename(title="Save As", initialfile="Untitled", defaultextension="*.txt", filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py")])
            if file=="":
                file=None
            else:
                contents=open(file, "w")
                contents.write(txtPad.get(1.0, END))
                contents.close()
                win.title(file+" - Notepad")
        else:
            contents=open(file, "w")
            contents.write(txtPad.get(1.0, END))
            contents.close()
            
    def open_file():
        global file
        file=filedialog.askopenfilename(title="Open a File", filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py")])
        if file==None or file=="":
            win.title("Untitled - Notepad")
        else:
            win.title(file+" - Notepad")
            contents=open(file, "r")
            txtPad.delete(1.0, END)
            txtPad.insert(1.0, contents.read())
            contents.close()

    def help():
        messagebox.showinfo("Notepad", "This Notepad is created by Atharva")


#text area

txtPad=Text(font=("cambria 12"))
txtPad.pack(expand=1, fill=BOTH)
txtPad.focus()

# Scrollbar Y

scrolly=Scrollbar(txtPad)
scrolly.pack(side=RIGHT, fill=Y)
scrolly.config(command=txtPad.yview)
txtPad.config(yscrollcommand=scrolly.set)

# Scrollbar X

scrollx=Scrollbar(txtPad, orient=HORIZONTAL, command=txtPad.xview)
scrollx.pack(side=BOTTOM, fill=X, anchor="w")
scrollx.config(command=txtPad.xview)
txtPad.config(xscrollcommand=scrollx.set)

# THIS IS THE AREA OF MENUS

# File Menu
file_menu=Menu(tearoff=0)
file_menu.add_command(label="New", command=functions.new)
file_menu.add_command(label="Open", command=functions.open_file)
file_menu.add_command(label="Save", command=functions.save_file)
file_menu.add_separator()
file_menu.add_command(label="Clear", command=functions.clear)
file_menu.add_command(label="Exit", command=functions.exit)


# Help Menu
help_menu=Menu(tearoff=0)
help_menu.add_command(label="About", command=functions.help)

# Main Menu
main_menu=Menu()
win.configure(menu=main_menu)
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Help", menu=help_menu)

# Shortcut Keys

win.bind("<Control-s>", lambda pressed_key : functions.save_file())
win.bind("<Control-o>", lambda pressed_key : functions.open_file())

win.mainloop()
