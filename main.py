import tkinter

window = tkinter.Tk()
window.title("This is my tkinter window")
window.minsize(width=500, height=300)

# my_button = tkinter.Button(text='Play Game', font=("Arial", 24, "bold"))
# my_button.config(bg="red", font=("Arial", 20))
# my_button.pack()

my_label = tkinter.Label(text='I am label', font=("Arial", 24, "bold"), )
# my_label.config() # Create a custom size for label.
my_label.pack(side='top')


my_label02 = tkinter.Label(text='label', font=("Arial", 20,), )
# my_label.config() # Create a custom size for label.
my_label02.pack(side='left')

window.mainloop()

