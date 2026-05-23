#import tkinter for creating GUI apps
import tkinter as tk
from tkinter import filedialog,messagebox
#main window code
root=tk.Tk()
root.title("Text Editor App")
root.geometry("800x600")
#creating text area
text=tk.Text(
    root,
    wrap=tk.WORD,
    font=("Ariel",12)
)

text.pack(expand=True,fill=tk.BOTH)
#main logic
#function 1- to create a new file
def new_file():
    text.delete(1.0,tk.END)

#function 2-to open a new file
def open_file():
    file_path=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )

    if file_path:
        with open(file_path,"r") as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END,file.read())

#function 3- Saving the file
def save_file():
    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

    messagebox.showinfo("info","File Saved Successfully")

#menu
menu=tk.Menu(root)
root.config(menu=menu)

file_menu=tk.Menu(menu)

menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

# it starts and keep the window open
root.mainloop()
