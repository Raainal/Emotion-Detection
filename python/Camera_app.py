import customtkinter as ctk
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
   label = ctk.CTkLabel(master=window)
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

# Create the main window
window = ctk.CTk()
window.geometry("400x300")
window.title("Camera App")

# Create a button to start the camera
button = ctk.CTkButton(master=window, text="Start Camera", command=start_camera)
button.pack(pady=20)

# Run the Tkinter main loop
window.mainloop()
