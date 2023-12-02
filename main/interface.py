import tkinter as tk
from tkinter import ttk, messagebox, END
import json
import requests
import key
import openai
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
        openai.api_key = key.OPENAI_KEY

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


    def query_response(self, prompt):
        messag=[{"role": "Computer System Expert", "content": "You are a chatbot"}]
        
        ## build a chat history: you can CONDITION the bot on the style of replies you want to see - also getting weird behaviors... such as KanyeGPT
        history_bot = ["Yes, I'm ready! Please provide the first paper abstract."]
    
        # ask ChatGPT to return STRUCTURED, parsable answers that you can extract easily - often better providing examples of desired behavior (1-2 example often enough)
        history_user = ["I am a user trying to understand my system and you are a computer systems professional who can help me explain my questions I have about it. I will send you my system logs in .json file and ask you some questions about them and you will respond to me with your best knowledge."]
    
        for user_message, bot_message in zip(history_user, history_bot):
            messag.append({"role": "user", "content": str(user_message)})
            messag.append({"role": "system", "content": str(bot_message)})
        messag.append({"role": "user", "content": str(prompt)})

        response = openai.ChatCompletion.create(
        
        # please use gtp3.5 although gpt4 is much better for $$
        model="gpt-3.5-turbo",
            messages=messag
        )
        result = ''
        for choice in response.choices:
            result += choice.message.content
        history_bot.append(result)
        history_user.append(str(prompt))
        return result

def main():
    root = tk.Tk()
    chatbot_gui = ChatbotGUI(root)
    #root.mainloop()
    print(chatbot_gui.query_response("The power of human language and thought arises from systematic compositionality"))

if __name__ == "__main__":
    main()
