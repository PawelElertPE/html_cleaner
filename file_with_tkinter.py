import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Greetings willage people!!!!")
root.geometry("1000x600")
root.resizable(True, True)

photo = ImageTk.PhotoImage(Image.open("Halle.jpg"))
root.iconphoto(False, photo)

greetings = tk.Label(root,
                     text="Welcome to the Tkinter tutorial!",
                     font=("Arial", 25))

about_tkinter = tk.Label(foreground="black", 
                         background="cyan",
                         bd=14,
                         font=("Times New Roman", 20))

about_tkinter["text"] = "Standard Python interface to the Tk GUI toolkit shipped with Python!"

greetings.pack()
about_tkinter.pack()

root.mainloop()
