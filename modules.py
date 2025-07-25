import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My First Tkinter App")
window.geometry("300x200")  # Width x Height

# Add a label widget
label = tk.Label(window, text="Hello, AK! Welcome to Tkinter.")
label.pack(pady=10)  # pack adds it to the window with padding

# Add a button widget
def on_button_click():
    label.config(text="You clicked the button!")

button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Start the event loop
window.mainloop()
