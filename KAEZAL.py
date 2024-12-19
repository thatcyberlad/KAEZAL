import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import os
import platform
import subprocess

# Version
version = "1.2"

# Helper functions to launch each tool in a separate terminal
def open_how_to_use():
    webbrowser.open("https://pastecode.io/s/t98k2t94")

def launch_tool(tool_name, script_name, script_type="bash"):
    # Define the path to the tool's folder and script
    tool_path = os.path.join("Tools", tool_name, script_name)
    if os.path.exists(tool_path):
        # Open the tool in a new terminal window
        try:
            # Try x-terminal-emulator first (common default on many Linux distributions)
            if script_type == "bash":
                subprocess.Popen(["x-terminal-emulator", "-e", f"bash {tool_path}"])
            elif script_type == "python":
                subprocess.Popen(["x-terminal-emulator", "-e", f"python3 {tool_path}"])
        except FileNotFoundError:
            # If x-terminal-emulator is not available, try xfce4-terminal
            try:
                if script_type == "bash":
                    subprocess.Popen(["xfce4-terminal", "--hold", "-e", f"bash {tool_path}"])
                elif script_type == "python":
                    subprocess.Popen(["xfce4-terminal", "--hold", "-e", f"python3 {tool_path}"])
            except FileNotFoundError:
                # If xfce4-terminal is not available, try gnome-terminal
                try:
                    if script_type == "bash":
                        subprocess.Popen(["gnome-terminal", "--", "bash", tool_path])
                    elif script_type == "python":
                        subprocess.Popen(["gnome-terminal", "--", "python3", tool_path])
                except FileNotFoundError:
                    messagebox.showerror("Error", "No compatible terminal found. Please install x-terminal-emulator, xfce4-terminal, or gnome-terminal.")
    else:
        messagebox.showerror("Error", f"{tool_name} directory or script not found!")

# Individual functions for each tool button
def open_phishing_tool():
    launch_tool("phisher", "phisher.sh")

def open_webcam_phishing():
    launch_tool("camphisher", "camphisher.sh")

def open_qr_phishing():
    launch_tool("QR_Attack", "QR_Attack.py", "python")

def open_user_find():
    launch_tool("finduser", "finduser.sh")

def open_url_mask():
    launch_tool("URL_Mask", "URL_Mask.sh")  

def open_KAEZAL_X():
    # Show "Coming Soon!" message box
    messagebox.showinfo("Coming Soon!", "KAEZAL_X will be available soon!")

# GUI setup
root = tk.Tk()
root.title(f"KAEZAL v{version}")

# Set window to open maximized (cross-platform solution)
if platform.system() == "Windows":
    root.state('zoomed')
else:
    root.attributes('-zoomed', True)
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")

# Load background image (JPG) and set it as the background
background_image = Image.open("background.jpg")  # Use your JPG file here
background_photo = ImageTk.PhotoImage(background_image)

# Create a background label to hold the image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# ASCII Art Header (Figlet-style)
ascii_art = """
    _/    _/    _/_/    _/_/_/_/  _/_/_/_/_/    _/_/    _/     
   _/  _/    _/    _/  _/              _/    _/    _/  _/      
  _/_/      _/_/_/_/  _/_/_/        _/      _/_/_/_/  _/       
 _/  _/    _/    _/  _/          _/        _/    _/  _/        
_/    _/  _/    _/  _/_/_/_/  _/_/_/_/_/  _/    _/  _/_/_/_/  
"""

# Display ASCII art with enlarged font in GUI
ascii_label = tk.Label(root, text=ascii_art, font=("Courier", 18, "bold"), fg="lime", bg="black")
ascii_label.pack(pady=30)

# Subheader display with larger font size
subheader = tk.Label(root, text='"All your social engineering needs at one stop"', font=("Courier", 16, "bold"), fg="cyan", bg="black")
subheader.pack(pady=15)

# Buttons for each tool with larger font size
button_texts = [
    ("How to Use?", open_how_to_use),
    ("Phishing Tool", open_phishing_tool),
    ("WebCam Phishing", open_webcam_phishing),
    ("QR Phishing", open_qr_phishing),
    ("User Find", open_user_find),
    ("URL Mask", open_url_mask),
    ("KAEZAL_X", open_KAEZAL_X)
]

# Adding Buttons to GUI with increased font size and padding
for text, command in button_texts:
    button = tk.Button(root, text=text, font=("Courier", 16), command=command, width=25, fg="white", bg="black", relief="raised")
    button.pack(pady=10)

# Display version and credits with larger font size
version_label = tk.Label(root, text=f"Version: {version}", font=("Courier", 14), fg="gray", bg="black")
version_label.pack(side="left", padx=20, pady=20)

credits = tk.Label(root, text="Coded by: Zeeshan Karim, Umair Fazal", font=("Courier", 14), fg="gray", bg="black")
credits.pack(side="right", padx=20, pady=20)

# Run the GUI loop
root.mainloop()
