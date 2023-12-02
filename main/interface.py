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
        self.api_url = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
        self.headers = {"Authorization": "Bearer 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"}
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


    def query_openai(self, payload):
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        return response.json()
    def query_response(self, prompt):
        messag=[{"role": "Computer System Expert", "content": "You are a chatbot"}]
        messag=[{"role": "system", "content": "You are a chatbot"}]
        
        ## build a chat history: you can CONDITION the bot on the style of replies you want to see - also getting weird behaviors... such as KanyeGPT
        history_bot = ["Yes, I'm ready! Please provide the first paper abstract."]
    
        # ask ChatGPT to return STRUCTURED, parsable answers that you can extract easily - often better providing examples of desired behavior (1-2 example often enough)
        history_user = ["I am a user trying to understand my system and you are a computer systems professional who can help me explain my questions I have about it. I will send you my system logs in .json file and ask you some questions about them and you will respond to me with your best knowledge."]
        history_user = ["i'll give you some paper abstracts. for each abstract (i.e., for each of my messages), you will a) assign a topic from the following list:\nbiochemistry\nbiophysics\nproteomics\ncancer\ncell biology\nmolecular and synthetic biology\ncomputational biology\ngenetics and genomics\npathology\nimmunology\nmicrobiology\nneuroscience\ndevelopmental biology\nethology and behavior\nzoology\nplant biology\nindustrial biotechnology\npharmacology\nengineering\nvirology\nmachine learning\nchemical biology\nnanomedicine\naging\necology and evolution\nvaccinology\nepidemiology\nclinical trials,\nb) write a 2-sentences summary, focusing on the key innovation presented in that abstract.\n\nfor example:\nmy input = The spontaneous deamination of cytosine is a major source of transitions from C•G to T•A base pairs, which account for half of known pathogenic point mutations in humans. The ability to efficiently convert targeted A•T base pairs to G•C could therefore advance the study and treatment of genetic diseases. The deamination of adenine yields inosine, which is treated as guanine by polymerases, but no enzymes are known to deaminate adenine in DNA. Here we describe adenine base editors (ABEs) that mediate the conversion of A•T to G•C in genomic DNA. We evolved a transfer RNA adenosine deaminase to operate on DNA when fused to a catalytically impaired CRISPR–Cas9 mutant. Extensive directed evolution and protein engineering resulted in seventh-generation ABEs that convert targeted A•T base pairs efficiently to G•C (approximately 50% efficiency in human cells) with high product purity (typically at least 99.9%) and low rates of indels (typically no more than 0.1%). ABEs introduce point mutations more efficiently and cleanly, and with less off-target genome modification, than a current Cas9 nuclease-based method, and can install disease-correcting or disease-suppressing mutations in human cells. Together with previous base editors, ABEs enable the direct, programmable introduction of all four transition mutations without double-stranded DNA cleavage.\n\nyour output =\na. genetics and genomics\nb. A new base-editor that converts A-T to G-C, based on an RNA adenosine deaminase fused to catalitically-impaired CRISPR-Cas9. Base editors can install therapeutic mutations in genomic DNA in human cells with no double-strand break.\nready to start?"]
    
        for user_message, bot_message in zip(history_user, history_bot):
            messag.append({"role": "user", "content": str(user_message)})
def main():
    root = tk.Tk()
    chatbot_gui = ChatbotGUI(root)
    root.mainloop()
    #root.mainloop()
    print(chatbot_gui.query_response("The power of human language and thought arises from systematic compositionality"))

if __name__ == "__main__":
    main()
    main()