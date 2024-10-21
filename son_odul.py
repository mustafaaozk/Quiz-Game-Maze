import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("Ödül Ekranı")
window.geometry("600x600")

with open("kullanici.txt", "r") as file:
    kullanıcı_adı = file.read().strip()

icon_image = Image.open("Asset/icon/icono.png")  # Load the PNG image
icon_photo = ImageTk.PhotoImage(icon_image)
window.iconphoto(True, icon_photo)
# Create a label to display the video
video_label = Label(window)
video_label.pack(pady=100)

label_isim = tk.Label(window,text=f"Tebrikler {kullanıcı_adı}",font=("Times New Roman", 30, "bold"), fg="black")
label_isim.pack(side=TOP)

# Open the video file using OpenCV
video_path = "Asset/Video/video.mp4"
cap = cv2.VideoCapture(video_path)

# Set desired width and height for the video
desired_width = 600
desired_height = 600

# Update function to display video frames in Tkinter
def update_frame():
    ret, frame = cap.read()  # Read a frame from the video
    if ret:
        # Resize the frame while maintaining aspect ratio
        h, w = frame.shape[:2]  # Get the original height and width
        aspect_ratio = w / h
        if w > h:
            new_width = desired_width
            new_height = int(desired_width / aspect_ratio)
        else:
            new_height = desired_height
            new_width = int(desired_height * aspect_ratio)

        frame = cv2.resize(frame, (new_width, new_height))  # Resize the frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert color to RGB
        img = ImageTk.PhotoImage(Image.fromarray(frame))  # Convert to ImageTk format
        video_label.config(image=img)  # Update label with new image
        video_label.image = img

        # Schedule the next frame update
        window.after(10, update_frame)  # Call the function again after 10 ms
    else:
        # Release resources and close window when video ends
        cap.release()  # Release the video capture
        window.quit()  # Close the window

# Function to close the window after 5 seconds
def close_window():
    cap.release()  # Release the video capture
    window.quit()  # Close the window

# Start the update function
update_frame()

# Schedule the window to close after 5000 ms (5 seconds)
window.after(5000, close_window)

# Start the Tkinter main loop
window.mainloop()
