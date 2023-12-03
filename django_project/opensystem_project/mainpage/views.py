# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import sys
import tkinter as tk
import pandas as pd

sys.path.append('C:\\Users\\noafl\\Documents\\GitHub\\Lauzhack2023')
sys.path.append('C:\\Users\\noafl\\Documents\\GitHub\\Lauzhack2023\\main')
sys.path.append('C:\\Users\\noafl\\Documents\\GitHub\\Lauzhack2023\\dataBases')
from main.interface import ChatbotGUI



def home(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

@csrf_exempt
def execute_prompt_vue(request):
    chatbot_gui = ChatbotGUI()
    # root.mainloop()
    empty_df = pd.DataFrame()  # DataFrame vide pour tester
    file_name = request.POST.get('file_name', 'system_logs_last_30_days.json')
    
    # Construct the file path dynamically
    file_path = f"C:\\Users\\noafl\\Documents\\GitHub\\Lauzhack2023\\dataBases\\{file_name}"
    
    # Load the JSON file into a DataFrame
    #df = chatbot_gui.jsonToArray(file_path)
    
    # Utilisez request.POST pour récupérer les données du formulaire
    user_message = request.POST.get('message', '')  
    
    # Utilisez le message récupéré dans query_response
    result = chatbot_gui.start_query_session(user_message, empty_df)
    
    # Renvoie la réponse en tant que JSON
    return JsonResponse({'result': result})


