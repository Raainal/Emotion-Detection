import customtkinter as ctk
import cv2
from PIL import Image, ImageTk


def ensure_camera_opened():
    global cap
    if cap is None or not cap.isOpened():
        cap = cv2.VideoCapture(0)  # Use 0 for the default camera
        if not cap.isOpened():
            print("Error: Could not open camera.")
            return False
    return True


def start_camera():
    global cap, frame, label

    if not ensure_camera_opened():
        return

    # Create a label to display the video stream
    label = ctk.CTkLabel(master=window,text=None)
    label.pack(expand=True, fill="both")

    update_frame()


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
        window.after(10, update_frame)
    else:
        # If no frame is read, try reopening the camera
        cap.release()
        cap = None
        print("Error reading frame from camera. Trying to reopen...")
        window.after(500, update_frame)  # Retry after a delay


# Initialize variables
cap = None
frame = None
label = None
face_cascade = cv2.CascadeClassifier("D:\Studies\Mini Project 2\python\haarcascade_frontalface_default.xml")  # Load face detector

# Create the main window
window = ctk.CTk()
window.geometry("400x300")
window.title("Camera App with Face Tracking Box")

# Create a button to start the camera
button = ctk.CTkButton(master=window, text="Start Camera", command=start_camera)
button.pack(pady=20)


# Function to handle window closing (optional)
def on_closing():
    global cap
    if cap is not None:
        cap.release()
    window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)  # Bind window closing event (optional)

# Run the Tkinter main loop
window.mainloop()
