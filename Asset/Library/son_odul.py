import tkinter as tk
from PIL import Image, ImageTk
import os

# Create the main window
window = tk.Tk()
window.title("Ödül Ekranı")

# Get screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")

# Load the icon image and set it as the window icon
icon_image = Image.open("Asset/icon/game.jpg")
icon_photo = ImageTk.PhotoImage(icon_image)
window.iconphoto(True, icon_photo)

# Load the reward image without resizing
son_odul = Image.open("Asset/Images/son_odul.jpg")
son_odul_photo = ImageTk.PhotoImage(son_odul)

# Set the desired background color
arka_plan = "#fdfff2"

# Create a canvas to display the image with the specified background color
canvas = tk.Canvas(window, width=screen_width, height=screen_height, bg=arka_plan)
canvas.pack()

# Calculate image coordinates to center it
img_x = (screen_width // 2) - (son_odul_photo.width() // 2)
img_y = (screen_height // 2) - (son_odul_photo.height() // 2)

# Display the image on the canvas
canvas.create_image(img_x, img_y, image=son_odul_photo, anchor=tk.NW)
with open("Asset/Database/kullanici.txt", "r") as file:
    kullanıcı_adı = file.read().strip()

os.remove("Asset/Database/kullanici.txt")

window.mainloop()
