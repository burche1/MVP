from django.shortcuts import render
from django.http import HttpResponse
from bestbud.watchdog import Watchdog
from bestbud.models import Product,Purchase
from django.utils import timezone
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
class Produto(object):
    name = ''
    price = ''
    logo = ''
    def __init__(self, name, price, logo):
        self.name = name
        self.logo = logo
        self.price = price
class Compra(object):
    name = ''
    price = ''
    qtd = ''
    ptotal = ''
    def __init__(self, name, price, qtd, ptotal):
        self.name = name
        self.qtd = qtd
        self.price = price
        self.ptotal = ptotal

def produtos(request):
    produtos = []
    for produto in Product.objects.all():
        produtos.append(Produto(name = (produto.name),price=(produto.price),logo=('/' + (produto.logo.url.split('/', 1)[1]))))
    context = {'produtos': produtos}
    return render(request, 'bestbud/products.html', context)

def buy(request):
    produtos_comprados = request.POST.getlist('prod')
    produtos = []
    for produto in Product.objects.all():
        produtos.append(Produto(name = (produto.name),price=(produto.price),logo=('/' + (produto.logo.url.split('/', 1)[1]))))
    compras = []
    total = 0
    for i in range(len(Product.objects.all())):
        if int(produtos_comprados[i])>0:
            total = total + (float(produtos[i].price) * float(produtos_comprados[i]))
            compras.append(Compra(name=(produtos[i].name),price=(produtos[i].price),qtd=(produtos_comprados[i]),ptotal=('%.2f' % (float(produtos[i].price)*float(produtos_comprados[i])))))
    return render(request, 'bestbud/buy.html', {'compras': compras, 'total': ('%.2f' % total)})

def thanks(request):
    names = request.POST.getlist('nome')
    qtds = request.POST.getlist('qtde')
    prices = request.POST.getlist('preco')
    totalprices = request.POST.getlist('precototal')
    if (len(Purchase.objects.all())==0):
        purchase_ident = 0
    else:
        purchase_ident = int(Purchase.objects.latest('id').purchase_id) + 1
    for i in range(len(names)):
        q = Purchase(name=(names[i]),price=(prices[i]),total_price=totalprices[i],qtd=qtds[i],purchase_id=purchase_ident,date=timezone.now())
        q.save()
    return render(request, 'bestbud/thanks.html')
