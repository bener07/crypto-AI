from django.shortcuts import render
from database.models import coins
import requests
# Create your views here.


def home(request):
    context = {
        'coins': coins.current_coins()
    }
    return render(request, 'index.html', context)


def coin(request, id):
    context = {
        'coin': coins.objects.get(id=id)
    }
    return render(request, 'coin.html', context)



def history(request, id):
    context = {
        'coin': coins.objects.get(id=id)
    }
    return render(request, 'history.html', context)
