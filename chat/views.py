from django.shortcuts import render

def index(request, room_name):
    return render(request, 'chatapp/index.html', {'room_name': room_name})
