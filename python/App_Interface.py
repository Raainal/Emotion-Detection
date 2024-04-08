import customtkinter as ctk
import tkinter as tk  # Needed for messagebox
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk

# Initialize variables for camera and image display
cap = None
frame = None
label = None

def start_camera():
    global cap, frame, label

    # Release any existing camera resource
    if cap is not None:
        cap.release()

    # Create a new video capture object
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera

    # Create a label to display the video stream
    label = ctk.CTkLabel(master=window , text=None)
    label.pack(expand=True, fill="both")

    # Start a loop to continuously read and display frames
    update_frame()

def update_frame():
    global cap, frame, label

    # Read a frame from the camera
    ret, frame = cap.read()
    if ret:
        # Convert frame to RGB format and then to a PIL image
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)

        # Update the label with the new image
        label.configure(image=photo)
        label.image = photo  # Keep a reference to prevent garbage collection

        # Schedule the next frame update
        window.after(10, update_frame)  # Update every 10 milliseconds
    else:
        # If no frame is read, release the camera and stop the loop
        cap.release()
        cap = None
        frame = None
        print("Error reading frame from camera")


def analyze_emotion():
    # Replace this with your actual emotion detection logic
    detected_emotion = "Happy"  # Temporary happy
    messagebox.showinfo(
        "Emotion Detection", f"This feature is not yet implemented. Emotion detected: {detected_emotion}"
    )


def capture_image():
    global cap, frame, messagebox

    # Capture image if camera is active
    if cap is not None:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("captured_image.png", frame)
            messagebox.showinfo("Capture Image", "Image captured successfully!")
        else:
            messagebox.showerror("Error", "Failed to capture image. Camera might be unavailable")
    else:
        messagebox.showwarning("Warning", "Camera is not started. Please start the camera first.")


# Create the main window
window = ctk.CTk()
window.geometry("600x400")  # Adjust window size as needed
window.title("Emotion Detection App (Camera Integration)")

# Create a label for displaying captured image (optional, comment out if not needed)
# captured_image_label = tk.Label(window)
# captured_image_label.pack()

# Create a button to start the camera
button_start_camera = ctk.CTkButton(master=window, text="Start Camera", command=start_camera)
button_start_camera.pack(pady=10)

# Create a button to capture image
button_capture_image = ctk.CTkButton(master=window, text="Capture Image", command=capture_image)
button_capture_image.pack(pady=10)

# Create a button to analyze emotion (placeholder for future implementation)
button_analyze_emotion = ctk.CTkButton(
    master=window, text="Analyze Emotion", command=analyze_emotion
)
button_analyze_emotion.pack(pady=10)

# Text entry field for user name (optional, comment out if not needed)
# name_label = tk.Label(window, text="Enter Your Name:")
# name_label.pack()
# name_entry = tk.Entry(window)
# name_entry.pack()

# Run the Tkinter main loop
window.mainloop()
