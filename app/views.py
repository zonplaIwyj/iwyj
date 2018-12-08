from django.shortcuts import render
from app.models import Wheel, Nav, Mustbuy, Shop, MainShow


def home(request):
    wheels=Wheel.objects.all()
    navs=Nav.objects.all()
    mustbuys=Mustbuy.objects.all()
    shops=Shop.objects.all()
    shophead=shops[0]
    shoptabs=shops[1:3]
    shopclass=shops[3:7]
    shopcommends=shops[7:11]
    mainShows=MainShow.objects.all()
    data={
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead':shophead,
        'shoptabs':shoptabs,
        'shopclass':shopclass,
        'shopcommends':shopcommends,
        'mainShows':mainShows,

    }
    return render(request,'home/home.html',context=data)


def market(request):
    return render(request, 'market/market.html')


def cart(request):
    return render(request, 'cart/cart.html')


def mine(request):
    return render(request, 'mine/mine.html')