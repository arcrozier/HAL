from django.shortcuts import render


def home(request):
    return render(request, 'chatbot/HAL.html')
