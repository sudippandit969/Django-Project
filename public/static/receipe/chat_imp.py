# import following :
# 1.  pip install -q -U google-generativeai
# 2. pip install rich

# to get API KEY go to this link  (https://aistudio.google.com/app/apikey)


import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext
from rich.console import Console
from rich.text import Text

# Configure the API key
gemini_key = 'YPUR API KEY '
genai.configure(api_key=gemini_key)

# Initialize the Generative Model
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

# Function to get chatbot response
def get_chatbot_response(user_input):
    response = chat.send_message(user_input)
    return response.text

# Function to handle sending messages
def send_message():
    user_input = user_input_box.get("1.0", "end-1c").strip()
    user_input_box.delete("1.0", "end")

    if user_input.lower() in ['exit', 'quit']:
        chat_log.insert(tk.END, "Chatbot: Goodbye!\n")
        return

    chat_log.insert(tk.END, "You: " + user_input + "\n")
    bot_response = get_chatbot_response(user_input)
    chat_log.insert(tk.END, "Chatbot: " + bot_response + "\n")

# Create the main application window
root = tk.Tk()
root.title("Chatbot Interface")

# Create a chat log area
chat_log = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD)
chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create a user input box
user_input_box = scrolledtext.ScrolledText(root, width=40, height=4, wrap=tk.WORD)
user_input_box.grid(row=1, column=0, padx=10, pady=10)
# Example of setting a background color and font
root.configure(bg='lightblue')
chat_log.configure(bg='white', font=('Arial', 12))
user_input_box.configure(bg='white', font=('Arial', 12))

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)
# Example of making the chat log and input box responsive
chat_log.grid(row=0, column=0, columnspan=2, sticky='nsew')
user_input_box.grid(row=1, column=0, sticky='ew')
send_button.grid(row=1, column=1, sticky='nse')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start the GUI event loop
root.mainloop()