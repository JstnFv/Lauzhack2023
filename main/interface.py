import tkinter as tk
from tkinter import ttk, messagebox, END
import json
import requests

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot Interface")

        # Style configuration for themed widgets
        style = ttk.Style()
        style.theme_use('clam')  # You can experiment with different themes

        # Entry widget for user input
        self.user_input = ttk.Entry(master, width=40)
        self.user_input.pack(padx=10, pady=10)

        # Button to show all logs
        self.show_logs_button = ttk.Button(master, text="Send Message", command=self.send_message)
        self.show_logs_button.pack(pady=10)

        # Text widget to display conversation history
        self.conversation_history = tk.Text(master, wrap="word", width=60, height=20)
        self.conversation_history.pack(padx=10, pady=10)

        # Initialize conversation history
        self.conversation_history.insert(tk.END, "Chatbot: Hello! How can I help you?\n")

        # OpenAI API configuration
        self.api_url = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
        self.headers = {"Authorization": "Bearer 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"}

    def send_message(self):
        # Get user input
        user_message = self.user_input.get()

        # Display user's message in the conversation history
        self.conversation_history.insert(tk.END, f"User: {user_message}\n")

        # Call OpenAI API
        response = self.query_openai({"text": user_message})

        # Print the response for debugging
        print("OpenAI Response:", response)

        # Display OpenAI's response in the conversation history
        self.conversation_history.insert(tk.END, f"Chatbot: {response}\n")  # Adjust this line accordingly


    def query_openai(self, payload):
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        return response.json()

def main():
    root = tk.Tk()
    chatbot_gui = ChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
