import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk 

# Create the main window
window = tk.Tk()
window.title="Ödül Ekrannı"
window.geometry("600x600")

# Load and resize the reward image
son_odul_resmi = Image.open("Asset/Images/son_odul.jpg")  # Load the reward image
son_odul_img = ImageTk.PhotoImage(son_odul_resmi)  # Create a PhotoImage from the image

# Create a label to display the image
label = Label(window, image=son_odul_img)  # Create a label with the image
label.pack(pady=20)  # Pack the label into the window with some padding

# Start the Tkinter main loop
window.mainloop()
