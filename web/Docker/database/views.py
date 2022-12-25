from django.shortcuts import render
from database.models import coins
import requests
# Create your views here.
api = "192.168.1.152:5000"

def home(request):
    context = {
        'coins': coins.current_coins()
    }
    return render(request, 'index.html', context)


def coin(request, id):
    context = {
        'coin': coins.objects.get(id=id),
        'api': api
    }
    return render(request, 'coin.html', context)



def history(request, id):
    context = {
        'coin': coins.objects.get(id=id),
        'api': api
    }
    return render(request, 'history.html', context)
