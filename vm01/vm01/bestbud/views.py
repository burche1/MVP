from django.shortcuts import render
from django.http import HttpResponse
from bestbud.watchdog import Watchdog
import time

# Create your views here.

def index(request):
    return render(request, 'bestbud/index.html')

def check_age(request):
    #flag = 0
    #return render(request, 'bestbud/check_age.html')
    #anterior = render(request, 'bestbud/index.html')
    #timer.sleep(5)
    return render(request, 'bestbud/index.html')

    #while not time.sleep(5) == True:
        #return render(request, 'bestbud/check_age.html')

    """
    try:
        Watchdog(5)
            #while(flag == 0):
                #if flag == 1:
                    #wd.stop()
        return render(request, 'bestbud/index.html')
    except Exception as e:
        return render(request, 'bestbud/index.html')
    """

#def check_age(request):
#    return render(request, 'bestbud/check_age.html')

def produtos(request):
    return render(request, 'bestbud/products.html')
