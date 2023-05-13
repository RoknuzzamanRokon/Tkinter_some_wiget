import tkinter

window = tkinter.Tk()
window.title("This is my tkinter window")
window.minsize(width=500, height=300)


# Label
my_label = tkinter.Label()
my_label.config(text="Here config my label text", foreground="Green", font=("Arial", 24, "bold"))


# Button

def button_fun():
    my_label["text"] = "Here config my label text"
    # my_label["bg"] = "Green"
    my_label["foreground"] = "black"


my_button = tkinter.Button(text='Click me', command=button_fun, width=20, height=1)
# tkinter.Frame(master=my_button, background="Yellow")
my_button.config(text="start Game")
my_button.pack()

# my_button = tkinter.Button(text='Play Game', font=("Arial", 24, "bold"))
# my_button.config(bg="red", font=("Arial", 20))
# my_button.pack()


input = tkinter.Entry(width=20)
input.pack()

window.mainloop()

