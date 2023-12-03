from tkinter import ttk, messagebox, END
import json
import pandas as pd
import requests
import key
import openai
class ChatbotGUI:
    def __init__(self):
        # OpenAI API configuration
        openai.api_key = key.OPENAI_KEY

    def jsonToArray(self, jsonFile):
        with open(jsonFile, "r", encoding="utf-16") as file:
                logs_data = json.load(file)
        
        #map the time to the message
        df = pd.DataFrame({'Message': []}) #'TimeGenerated': [], 
        for eachField in logs_data:
            new_row = {'Message': eachField["Message"]}
            df.loc[len(df)] = new_row
        return df

    def start_query_session(self, dataFrame):
        messag=[{"role": "system", "content": "You are a chatbot."}]
        
        ## build a chat history: you can CONDITION the bot on the style of replies you want to see - also getting weird behaviors... such as KanyeGPT
        history_bot = ["I'm ready! Ask me any question about your system"]
        # ask ChatGPT to return STRUCTURED, parsable answers that you can extract easily - often better providing examples of desired behavior (1-2 example often enough)
        history_user = ["I am a user trying to understand my system and you are a computer systems professional who can help me explain my questions I have about it. For each answer you give, you need to show proof for the answer directly copied from the (Message) column in the database. For example, if someone asks, what installations have happened in the system? You can reply with, there have been _ number of installations that have happened in the system. Examples of things you have installed include: 1. An antivirus shown from the log: Installation réussie : Windows a installé la mise à jour suivante : Mise à jour de la sélection disjointe pour Microsoft Defender Antivirus – 2267602 Ko (version 1.401.1546.0) – Canal actuel (large). Please use the dataset given here:"]
        history_user.append("This is the database you should analyse from: " + dataFrame)
        history_bot.append("Okay! I will use the database you have given me and give you my best answer!")
        #chatgpt should remember previous prompts!
        for user_message, bot_message in zip(history_user, history_bot):
            messag.append({"role": "user", "content": str(user_message)})
            messag.append({"role": "system", "content": str(bot_message)})
        
        #store the chat and update it each time
        print("Hello, I am your Personal Virtual Technician, ask me questions about your system! Enter 'exit' if you'd like to stop chatting with me.")
        while True:
            user_input = input("Your input: ")
            messag.append({"role": "user", "content": str(user_input)})
            response = openai.ChatCompletion.create(
             model="gpt-3.5-turbo",
             messages=messag
            )
            result = ''
            for choice in response.choices:
                result += choice.message.content
            history_bot.append(result)
            if user_input.lower() == 'exit':
                print("Exiting the chat!")
                break
            else:
                print("AI Response:")
                print(result)

def main():
    chatbot_gui = ChatbotGUI()
    df = chatbot_gui.jsonToArray("system_logs_last_30_days.json")
    chatbot_gui.start_query_session(df)
if __name__ == "__main__":
    main()
