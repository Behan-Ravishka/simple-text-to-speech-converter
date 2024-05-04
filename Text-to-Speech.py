import tkinter as tk
from gtts import gTTS
from tkinter import ttk
import os
import pygame
import tempfile

# Initialize pygame
pygame.init()

# Function to convert text to speech
def convert_text_to_speech():
    text = text_entry.get("1.0", "end-1c")  # Get text from the text entry
    language = languages[language_dropdown.get()]  # Get selected language from dropdown
    
    # Create the gTTS object with the selected language
    tts = gTTS(text, lang=language)
    
    # Create a temporary file in a secure manner
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_filename = temp_file.name
        # Save the speech to the temporary file
        tts.save(temp_filename)
    
    # Play the speech
    pygame.mixer.music.load(temp_filename)
    pygame.mixer.music.play()
    
    # Wait for the playback to finish
    while pygame.mixer.music.get_busy():
        continue
        
    # Delete the temporary file after playback
    os.unlink(temp_filename)

# Create the main tkinter window
root = tk.Tk()
root.title("Text-to-Speech Application")

# Create a text entry for user input
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

# Create a dropdown menu for language selection
languages = {'English': 'en', 'Sinhala': 'si', 'Tamil': 'ta'}
language_dropdown = ttk.Combobox(root, values=list(languages.keys()))
language_dropdown.pack()

# Default language selection
language_dropdown.set('English')

# Create a button to convert text to speech
convert_button = tk.Button(root, text="Convert to Speech", command=convert_text_to_speech)
convert_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
