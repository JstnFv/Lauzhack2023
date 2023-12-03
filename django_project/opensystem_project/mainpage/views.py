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

df = pd.DataFrame()  # DataFrame vide pour tester
chatbot_gui = ChatbotGUI()
chatbot_gui.initialize_chatbot(df)

def home(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

@csrf_exempt
def execute_prompt_vue(request):
    # Utilisez request.POST pour récupérer les données du formulaire
    user_message = request.POST.get('message', '')

    # Utilisez le message récupéré dans query_response
    result = chatbot_gui.add_prompt(user_message)

    # Renvoie la réponse en tant que JSON
    return JsonResponse({'result': result})


