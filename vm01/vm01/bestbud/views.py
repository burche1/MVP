from django.shortcuts import render
from django.http import HttpResponse
from bestbud.watchdog import Watchdog
import time
import numpy as np
# Create your views here.

def index(request):
    return render(request, 'bestbud/index.html')

def check_age(request):
    #flag = 0
    #return render(request, 'bestbud/check_age.html')
    #anterior = render(request, 'bestbud/index.html')
    #timer.sleep(5)
    return render(request, 'bestbud/check_age.html')

    #while not time.sleep(5) == True:
        #return render(request, 'bestbud/check_age.html')

    """
    try:
        Watchdog(5)
            #while(flag == 0):
                #if flag == 1:
                    #wd.stop()
        return render(request, 'bestbud/index')
    except Exception as e:
        return render(request, 'bestbud/index')
    """

#def check_age(request):
#    return render(request, 'bestbud/check_age.html')

def produtos(request):
    return render(request, 'bestbud/products.html')

def buy(request):
    produtos = request.POST.getlist('prod')
    lista = ['CocaCola', 'Pepsi', 'Soda', 'Guarana',
    'CocaCola', 'Pepsi', 'Soda', 'Guarana',
    'CocaCola', 'Pepsi', 'Soda', 'Guarana',
    'CocaCola', 'Pepsi', 'Soda', 'Guarana',
    'CocaCola', 'Pepsi', 'Soda', 'Guarana',
    'CocaCola', 'Pepsi', 'Soda', 'Guarana',
    'CocaCola', 'Pepsi', 'Soda', 'Guarana',
    'CocaCola', 'Pepsi', 'Soda', 'Guarana']
    compras = []
    for i in range(32):
        if int(produtos[i])>0:
            compras.append('Produto %s: %d' % (lista[i],int(produtos[i])))
    return render(request, 'bestbud/buy.html', {'compras': compras})
