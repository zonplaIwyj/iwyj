from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtype, Goods


def home(request):

    # 获取轮播图数据
    wheels = Wheel.objects.all()

    # 获取导航数据
    navs = Nav.objects.all()

    # 获取每日必购数据
    mustbuys = Mustbuy.objects.all()

    # 商品部分数据
    shops = Shop.objects.all()  # 所有
    shophead = shops[0]
    shoptabs = shops[1:3]
    shopclass = shops[3:7]
    shopcommends = shops[7:11]

    # 商品列表
    mainShows = MainShow.objects.all()

    data = {
        'wheels':wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shophead': shophead,
        'shoptabs': shoptabs,
        'shopclass': shopclass,
        'shopcommends': shopcommends,
        'mainShows': mainShows
    }

    return render(request, 'home/home.html', context=data)

def marketbase(request):
    # 默认是热销榜， 全部分类， 综合排序
    return redirect('axf:market', 104749, 0, 0)

# 参数1: categoryid 分类
# 参数2: childid 子类
# 参数3: sortid 排序方式
def market(request, categoryid, childid, sortid):
    # 分类信息
    foodtypes = Foodtype.objects.all()

    # 获取 分类下标  >>> typeIndex
    # 没有时，默认为0  >>> 默认热销数据
    typeIndex = int(request.COOKIES.get('typeIndex', 0))
    # 根据下标   获取  分类id
    categoryid = foodtypes[typeIndex].typeid

    # 子类信息
    childtypenames = foodtypes[typeIndex].childtypenames
    childtypelist = []
    for item in childtypenames.split('#'):
        # 子类名称: 子类ID
        # print(item)
        temp = item.split(':')
        dir = {
            'childname': temp[0],
            'childid': temp[1]
        }
        childtypelist.append(dir)

    # 商品信息
    # goodslist = Goods.objects.all()[0:10]
    # 商品信息 -- 分类
    # goodslist = Goods.objects.filter(categoryid=categoryid)
    if childid == '0':  # 全部分类
        goodslist = Goods.objects.filter(categoryid=categoryid)
    else:
        goodslist = Goods.objects.filter(categoryid=categoryid).filter(childcid=childid)

    # 0 综合排序
    if sortid == '1':   # 销量排序
        goodslist = goodslist.order_by('-productnum')
    elif sortid == '2': # 价格最低
        goodslist = goodslist.order_by('price')
    elif sortid == '3': # 价格最高
        goodslist = goodslist.order_by('-price')

    data = {
        'foodtypes': foodtypes,
        'goodslist': goodslist,
        'childtypelist': childtypelist,
        'categoryid': categoryid,
        'childid': childid
    }

    return render(request, 'market/market.html', context=data)


def cart(request):
    return render(request, 'cart/cart.html')


def mine(request):
    return render(request, 'mine/mine.html')


def register(request):
    return render(request, 'mine/register.html')