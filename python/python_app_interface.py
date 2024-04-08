import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk

def analyze_emotion():
    # Placeholder function for analyzing emotion
    detected_emotion = "Happy"  # Replace with actual emotion detection logic
    emotion_label.config(text=f"Detected Emotion: {detected_emotion}")

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_image.png", frame)
        messagebox.showinfo("Capture Image", "Image captured successfully!")
    cap.release()

# Create the main window
root = tk.Tk()
root.title("Emotion Detection App")

# Create a label for displaying detected emotion
emotion_label = tk.Label(root, text="Detected Emotion: ")
emotion_label.pack()

# Create a button to capture image
capture_button = tk.Button(root, text="Capture Image", command=capture_image)
capture_button.pack()

# Create a button to analyze emotion
analyze_button = tk.Button(root, text="Analyze Emotion", command=analyze_emotion)
analyze_button.pack()

# Create a text entry field for user's name
name_label = tk.Label(root, text="Enter Your Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Run the Tkinter event loop
root.mainloop()
