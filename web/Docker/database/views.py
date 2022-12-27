from django.shortcuts import render

# Create your views here.
from database.models import coins
import requests
api = "127.0.0.1:5000"

def home(request):
    context = {
        'coins': coins.current_coins()
    }
    return render(request, 'index.html', context)


def coin(request, id):
    context = {
        'coin': coins.objects.get(id=id),
        'api': request.get_host().split(':')[0]+':5000'
    }
    return render(request, 'coin.html', context)



def history(request, id):
    context = {
        'coin': coins.objects.get(id=id),
        'api': request.get_host().split(':')[0]+':5000'
    }
    return render(request, 'history.html', context)