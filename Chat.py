import tkinter as tk
from tkinter import font 
import docs.assets.scripts.python.create_database as create_database
import os
import docs.assets.scripts.python.query_data as query_data

CHROMA_PATH = "chroma"

if not os.path.exists(CHROMA_PATH):
  create_database.main()
  

def send_message(event=None):
    # Get the message text from the entry field
    message_text = message_entry.get()

    # Clear the message entry field
    message_entry.delete(0, tk.END)

    # Insert user question into chat window
    chat_window.insert(tk.END, "You: \n" + message_text + "\n")

    response=query_data.main(message_text)
    print(response)
    if response == None:
        response="Sorry, I do not have that knowledge."

    # Insert the response into the chat window
    chat_window.insert(tk.END, "Bot: \n" + response + "\n")


def on_resize(event):
    # Get the new window width and height
    new_width = event.width
    new_height = event.height

    # Adjust chat window size (adjust these values as needed)
    chat_window.config(width=int(new_width * 0.8), height=int(new_height * 0.8))

    # Adjust message entry size (adjust this value as needed)
    message_entry.config(width=int(new_width * 0.8))


window = tk.Tk()
window.title("VIS DRACONIS - Chatbot")

# Prevent full screen (optional, adjust as needed)
window.geometry("1200x800")  # Set initial window size

# Enable resizing
window.resizable(True, True)  # Allow both horizontal and vertical resizing

# Set font size
font_size = 20

# Logo image path (replace with your logo image path)
logo_path = "docs/assets/scripts/python/logo.png"  # Adjust the path to your logo file

# Ensure the logo image exists
if not os.path.exists(logo_path):
    print("Error: Logo image not found at", logo_path)
    exit(1)

# Load the logo image using PIL (assuming PNG format)
from PIL import Image, ImageTk
logo_image = Image.open(logo_path)

# Calculate desired resize dimensions based on a factor (adjust factor as needed)
resize_factor = 0.4  # Adjust this value to control logo size (e.g., 0.5 for half size)
logo_width, logo_height = logo_image.size  # Get original width and height

desired_width = int(logo_width * resize_factor)
desired_height = int(logo_height * resize_factor)

# Resize the logo image
logo_image = logo_image.resize((desired_width, desired_height), Image.BICUBIC)


logo_photo = ImageTk.PhotoImage(logo_image)

# Create a frame to hold logo and main content
container = tk.Frame(window)
container.pack(fill=tk.BOTH, expand=True)

# Logo label at top left (adjust padding as needed)
logo_label = tk.Label(container, image=logo_photo, padx=10, pady=10)
logo_label.pack(side=tk.LEFT)

# Chat window (adjust height as needed)
chat_window = tk.Text(container, height=20, width=50, font=(font.Font(size=font_size)))
chat_window.pack(fill=tk.BOTH, expand=True)  # Allow chat window to fill most space

# Send button below the message entry
send_button = tk.Button(container, text="Send", command=send_message)
send_button.pack(side=tk.BOTTOM)

# Message entry at the bottom
message_entry = tk.Entry(container, width=50, font=(font.Font(size=font_size)))
message_entry.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)  # Pack at bottom

# Bind Enter key press to send_message function
message_entry.bind("<Return>", send_message)

def send_message():
  # Get the message text from the entry box
  message = message_entry.get()
  
  # Clear the entry box for the next message
  message_entry.delete(0, tk.END)

  # Handle sending the message (logic depends on your app)
  # This could involve appending to chat_window or sending to a server
  chat_window.insert(tk.END, f"You: {message}\n")  # Example: append to chat window
  
  # (Optional) Additional actions after sending, like scrolling chat window
  chat_window.see(tk.END)  # Scroll to the end (optional)


window.mainloop()