from django.shortcuts import render
from api import api
from database.models import coins
import requests
# Create your views here.


coin = api('8807a578d9a3dd4ad7f132d2f3934d6da75cf68eaf267be1fea2572ef70f92bd')

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
