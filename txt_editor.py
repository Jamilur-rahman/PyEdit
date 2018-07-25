from tkinter import Tk, filedialog, END, Menu, scrolledtext, messagebox
import os
# Making the interface

scene = Tk(className=" PyEdit")
text = scrolledtext.ScrolledText(scene, width=100, height=40)

# Adding open, save, exit function


def open_file():
    f = filedialog.askopenfile(parent=scene, title="Select a file", filetypes=(("HTML file", "*.html"), ("Text file","*.txt")))
    scene.title(os.path.basename(f.name) + " - PyEdit")
    if f != None:
        content = f.read()
        text.insert('1.0', content)
        f.close()


def save_file():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt", filetypes=(("HTML file", "*.html"), ("Text file","*.txt")))

    if f != None:
        data = text.get('1.0', END+'-1c')
        f.write(data)
        f.close()


def new_file():
    if len(text.get('1.0', END+'-1c')) > 0:
        if messagebox.askyesno("Create new File", "Do you wish to create a new file?"):
            save_file()
            text.delete('0.0', END)
        else:
            text.delete('0.0', END)

def quit_e():
    data = text.get('0.0', END+'-1c')
    if messagebox.askyesno("Exit", "Do you wish to exit?"):
        if len(data) > 0:
            save_file()
            scene.quit()
        else:
            scene.quit()
# Creating menu bar


m_bar = Menu(scene)
scene.config(menu=m_bar)
f_menu = Menu(m_bar)
m_bar.add_cascade(label="File", menu=f_menu)

# Adding menu option

f_menu.add_command(label=" New File", command=new_file)
f_menu.add_command(label=" Open File", command=open_file)
f_menu.add_command(label=" Save file", command=save_file)
f_menu.add_separator()
f_menu.add_command(label="Exit", command=quit_e)

# Adding text area and starting interface
text.pack()
scene.mainloop()
