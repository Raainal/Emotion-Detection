import customtkinter as ct
import cv2
from PIL import Image, ImageTk

# (Optional) Set custom themes
ct.set_appearance_mode("Dark")  # Or "Dark" for dark mode

# Create the main application window
root = ct.CTk()
root.geometry("1920x1080")
root.title("Emotion Detection")

# Load the background image
bg_image = Image.open("D:/Studies/Mini Project 2/python/Front End/bg img4.jpg")
bg_image = bg_image.resize((1920, 1080))  # Resize the image to fit the window size
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Canvas to place the background image
canvas = ct.CTkCanvas(root, width=1920, height=1080)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=bg_photo)

# Create a title label with appealing formatting
title_label = ct.CTkLabel(
    root,
    text="Emotion Detection",
    font=("Arial", 30, "bold"),
    text_color="white",
    justify="center"  # Use justify for text alignment
)
title_label.place(relx=0.5, rely=0.1, anchor="center")

# Informational label (placeholder)
info_label = ct.CTkLabel(
    root,
    text="This is an application used to detect the Emotions of a person using the input from Camera",
    font=("Arial", 20),
    text_color="white",
    justify="center"  # Center-align informational text as well
)
info_label.place(relx=0.5, rely=0.2, anchor="center")

# Global variables
cap = None
frame = None
label = None
face_cascade = cv2.CascadeClassifier("D:/Studies/Mini Project 2/python/haarcascade_frontalface_default.xml")

def ensure_camera_opened():
    global cap
    if cap is None or not cap.isOpened():
        cap = cv2.VideoCapture(0)  # Use 0 for the default camera
        if not cap.isOpened():
            print("Error: Could not open camera.")
            return False
    return True

def update_frame():
    global cap, frame, label

    if not ensure_camera_opened():
        return

    # Read a frame from the camera
    ret, frame = cap.read()
    if ret:
        # Detect faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw boxes around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Green box for faces

        # Convert frame to RGB format and then to a PIL image
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)

        # Update the label with the new image
        label.configure(image=photo)
        label.image = photo  # Keep a reference to prevent garbage collection

        # Schedule the next frame update
        root.after(10, update_frame)
    else:
        # If no frame is read, try reopening the camera
        cap.release()
        cap = None
        print("Error reading frame from camera. Trying to reopen...")
        root.after(500, update_frame)  # Retry after a delay

def start_camera_button_pressed():
    print("Start Camera button clicked ")
    global cap, frame, label

    # Create label for displaying video feed
    label = ct.CTkLabel(root, text=None)
    label.place(relx=0.5, rely=0.5, anchor="center")

    update_frame()

def detect_emotions_button_pressed():
    print("Detect Emotions button clicked (functionality not yet implemented)")

start_camera_button = ct.CTkButton(
    root, text="Start Camera", command=start_camera_button_pressed
)
start_camera_button.place(relx=0.5, rely=0.8, anchor="center")

detect_emotions_button = ct.CTkButton(
    root, text="Detect Emotions ", command=detect_emotions_button_pressed
)
detect_emotions_button.place(relx=0.5, rely=0.9, anchor="center")

# Run the main application loop
root.mainloop()
