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
from main.interface import ChatbotGUI



def home(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

@csrf_exempt
def execute_prompt_vue(request):
    if request.method == 'POST':
        chatbot_gui = ChatbotGUI()
        # root.mainloop()
        empty_df = pd.DataFrame()  # DataFrame vide pour tester
        #result = chatbot_gui.query_response("Hi ! How are you today ?", empty_df)  # Utilisez le DataFrame vide
        #print("AI Response:", result)  # Ajoutez cette ligne pour imprimer la réponse de l'IA dans la console
        #return JsonResponse({'result': result})
        
        return JsonResponse({'result': 'Hello'})
    else:
        return render(request, loader.get_template('homepage.html'))


