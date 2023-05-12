import tkinter

window = tkinter.Tk()
window.title("This is my tkinter window")
window.minsize(width=500, height=300)

# my_button = tkinter.Button(text='Play Game', font=("Arial", 24, "bold"))
# my_button.config(bg="red", font=("Arial", 20))
# my_button.pack()

my_label = tkinter.Label(text='click', font=("Arial", 24, "bold"))
# my_label.config() # Create a custom size for label.
my_label.pack(side='top')


def button_fun():
    my_label["text"] = "This is edited text"

    print("I Got click ")




my_button = tkinter.Button(text='Click me', command=button_fun)
my_button.pack()

window.mainloop()

