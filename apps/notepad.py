# simple notepad with menubar
# Path: notepad.py
# Compare this snippet from frontend.py:
from tkinter import *
from tkinter.filedialog import askopenfile,asksaveasfile

#create an object to create a window
def notepad():
    notepadWindow = Tk()
    notepadWindow.title("Sales management system: Notepad")
    notepadWindow.geometry("800x500")
    # menubar
    menubar = Menu(notepadWindow)


    # file menu
    # open a file
    def open_file():
        global file
        file = askopenfile(mode='r', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
        if file is not None:
            contents = file.read()
            text.delete(1.0, END)
            text.insert(1.0, contents)
            file.close()
    # save text as file
    def save_file():
        files = [('All Files', '*.*'), 
                ('Python Files', '*.py'),
                ('Text Document', '*.txt')]
        global file
        file = asksaveasfile(mode='w', filetypes=files,defaultextension=files)
        if file is not None:
            data = text.get(1.0, END)
            file.write(data)
            file.close()

    # close file
    def close_file():
        text.delete(1.0, END)

    # new file add to new window
    def new_file():
        notepad()

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=new_file)
    filemenu.add_command(label="Open", command=open_file)
    filemenu.add_command(label="Save", command=save_file)
    filemenu.add_command(label="Close", command=close_file)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=notepadWindow.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # Edit menu
    # copy selected text
    def copy_to_clipboard():
        text_to_copy = text.get(SEL_FIRST, SEL_LAST)
        notepadWindow.clipboard_clear()
        notepadWindow.clipboard_append(text_to_copy)

    # cut selected text
    def cut_to_clipboard():
        text_to_copy = text.get(SEL_FIRST, SEL_LAST)
        notepadWindow.clipboard_clear()
        notepadWindow.clipboard_append(text_to_copy)
        text.delete(SEL_FIRST, SEL_LAST)

    # paste text from clipboard
    def paste_from_clipboard():
        text.insert(INSERT, notepadWindow.clipboard_get())

    # undo text
    def undo_text():
        text.edit_undo()

    # select all text
    def select_all_text():
        text.tag_add(SEL, "1.0", END)



    # edit menu
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=undo_text)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=cut_to_clipboard)
    editmenu.add_command(label="Copy", command=copy_to_clipboard)
    editmenu.add_command(label="Paste", command=paste_from_clipboard)
    editmenu.add_command(label="Select All", command=select_all_text)
    menubar.add_cascade(label="Edit", menu=editmenu)


    # display the menu
    notepadWindow.config(menu=menubar)

    # text widget
    text = Text(notepadWindow)
    text.configure(width=98, height=30)
    text.pack(expand=True, fill=BOTH)



    # display the window
    notepadWindow.mainloop()