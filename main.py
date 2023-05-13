import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("This is my tkinter window")
window.minsize(width=500, height=300)


# Label
my_label = tkinter.Label()
my_label.config(text="Here config \n my label text", foreground="Green", font=("Arial", 24, "bold"))
# my_label.pack()
my_label.grid(row=0, column=0)


# Button Function
def button_fun():
    my_label["text"] = "Here config \n my label text"
    # my_label["bg"] = "Green"
    my_label["foreground"] = "black"


# Create Button
my_button = tkinter.Button()
# tkinter.Frame(master=my_button, background="Yellow")
my_button.config(text='Click me', command=button_fun, width=20, height=1)
my_button.grid(row=1, column=1)

# my_button = tkinter.Button(text='Play Game', font=("Arial", 24, "bold"))
# my_button.config(bg="red", font=("Arial", 20))
# my_button.pack()


# Create Entry.
input = tkinter.Entry(width=20)
input.config(width=30, borderwidth=2)
input.insert(index=END, string="Some text example.")
input.grid(row=2, column=2)


# Create another button.
my_button_2 = Button()
my_button_2.config(text="I am Second Button.", bg="Red")
my_button_2.place(x=250, y=250)

window.mainloop()

