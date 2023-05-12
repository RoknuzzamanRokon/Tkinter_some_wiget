import tkinter


# Create a window.
window = tkinter.Tk()
window.title("Widget Example")
window.minsize(width=700, height=600)


# Create Label
my_label = tkinter.Label(text="This is new text", font=("Arial", 24, "bold"))
my_label.pack()


# Create Button
my_button = tkinter.Button()
my_button.config(text="Click Here")
my_button.pack()


# Create Entry
my_entry = tkinter.Entry()
my_entry.config(borderwidth=5, width=30)
my_entry.insert(index=1, string="Insert some text")
# print(my_entry.get())
my_entry.pack()


# Create Text Box
my_textbox = tkinter.Text()
my_textbox.config(height=10, width=30)
# Put cursor in text box.
my_textbox.focus()
my_textbox.pack()


# Create Spinbox
my_spinbox = tkinter.Spinbox()
my_spinbox.pack()


# Create Scale
my_scale = tkinter.Scale()
my_scale.pack()


# Create checkbutton
my_checkbutton = tkinter.Checkbutton()
my_checkbutton.config(text="Is On")
my_checkbutton.pack()

#

# create Radiobutton
my_radiobutton = tkinter.Radiobutton()
my_radiobutton.config(text="Option")
my_radiobutton.pack()


# Create Listbox
my_listbox = tkinter.Listbox()
my_listbox.config()
my_listbox.pack()









window.mainloop()


