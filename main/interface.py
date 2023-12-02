import tkinter as tk
from tkinter import ttk, messagebox
import json

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
        self.show_logs_button = ttk.Button(master, text="Show All Logs", command=self.show_logs_window)
        self.show_logs_button.pack(pady=10)

    def show_logs_window(self):
        # Create a new window to display logs
        logs_window = tk.Toplevel(self.master)
        logs_window.title("Logs Window")

        # Style configuration for themed widgets in the new window
        style = ttk.Style(logs_window)
        style.theme_use('clam')  # You can experiment with different themes

        # Frame to hold the table
        frame = ttk.Frame(logs_window)
        frame.pack(padx=10, pady=10)

        # Create a Treeview widget
        tree = ttk.Treeview(frame, columns=("TimeGenerated", "EntryType", "Source", "Message"), show="headings")

        # Define column headings
        tree.heading("TimeGenerated", text="Time Generated")
        tree.heading("EntryType", text="Entry Type")
        tree.heading("Source", text="Source")
        tree.heading("Message", text="Message")

        # Add Treeview to the frame
        tree.pack(expand=True, fill="both")

        try:
            # Charger les logs à partir d'un fichier JSON préparé avec UTF-16 encoding
            with open("system_logs_last_7_days.json", "r", encoding="utf-16") as file:
                logs_data = json.load(file)

            # Insert logs into the Treeview
            for log_entry in logs_data:
                tree.insert("", "end", values=(log_entry["TimeGenerated"], log_entry["EntryType"], log_entry["Source"], log_entry["Message"]))

        except Exception as e:
            error_message = f"Error loading and displaying logs: {e}"
            messagebox.showerror("Error", error_message)
            print(error_message)

# Fonction principale
def main():
    root = tk.Tk()
    chatbot_gui = ChatbotGUI(root)
    root.mainloop()

# Appeler la fonction principale si le script est exécuté en tant que programme principal
if __name__ == "__main__":
    main()
