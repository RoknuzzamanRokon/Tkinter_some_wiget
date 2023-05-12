import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("600x200")

# Create a frame and add it to the window
frame = tk.Frame(root, bg="blue", bd=10)
frame.place(relx=0.5, rely=0.5, anchor="center")


def my_button():

    label = tk.Label(text="Start playing", fg="red")
    label.winfo_geometry()
    label.pack()


# Add widgets to the frame
label = tk.Label(frame, text="This is a label in the frame", fg="Black", bg="Yellow")
label.pack(padx=10, pady=10)

button = tk.Button(frame, text="Play Game", bg="white", fg="blue", command=my_button)
button.pack(padx=10, pady=10)


# Start the main event loop
root.mainloop()
