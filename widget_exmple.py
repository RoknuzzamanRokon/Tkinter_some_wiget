import tkinter
from tkinter import *

# Create a window.
window = tkinter.Tk()
window.title("Widget Example")
window.minsize(width=700, height=600)


# Create Label
my_label = tkinter.Label(text="This is new text", font=("Arial", 24, "bold"))
my_label.pack()


def button_function():
    print("Do something")


# Create Button
my_button = tkinter.Button()
my_button.config(text="Click Here", command=button_function)
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
my_textbox.insert(END, "Something")
my_textbox.pack()


# Create Spinbox function.
def spinbox_function():
    print(my_spinbox.get())


# Create Spinbox.
my_spinbox = tkinter.Spinbox()
my_spinbox.config(from_=0, to=10, width=5, command=spinbox_function)
my_spinbox.pack()


# Scale Functon.
def scale_function(value):
    print(value)


# Create Scale.
my_scale = tkinter.Scale()
my_scale.config(from_=0, to=10, command=scale_function)
my_scale.pack()


#  Create Function for checkbutton.
def checkbutton_function():
    print(check_status.get())


# Create checkbutton.
my_checkbutton = tkinter.Checkbutton()
check_status = IntVar()
my_checkbutton.config(text="Is On", variable=check_status, command=checkbutton_function)
my_checkbutton.pack()


# Create rediobutton function.
def radiobutton_function():
    print(check_radiobutton.get())


# create Radiobutton
my_radiobutton = tkinter.Radiobutton()
check_radiobutton = IntVar()
my_radiobutton.config(text="Option", value=2, variable=check_radiobutton, command=radiobutton_function)
my_radiobutton.pack()


# Create Listbox
my_listbox = tkinter.Listbox()
my_listbox.config()
my_listbox.pack()









window.mainloop()


