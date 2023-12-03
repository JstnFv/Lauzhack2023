# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from main.interface import ChatbotGUI

def home(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())


def execute_prompt_vue(request):
    if request.method == 'POST':
        result = ChatbotGUI.query_response("Hi ! How are you today ?")
        return JsonResponse({'result': result})
    else:
        return render(request, loader.get_template('homepage.html'))
