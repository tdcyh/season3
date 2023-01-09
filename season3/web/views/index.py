from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from web import models

from web.models import dishes, displays1,displays2,historyOrder,cart

from  django.http import *
# Create your views here.

def index_unlog(request):
    ''' 项目前台大堂点餐首页 '''
    return render(request,"web/index_unlog.html")


def welcome(request):
    return render(request,"web/welcome.html")
def echarts(request):
    return render(request,"echarts/index.html")



def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username','')
        pass_word = request.POST.get('password','')
        user = models.User.objects.filter(username=user_name)  #查看数据库里是否有该用户名
        if user:#如果存在
            user = models.User.objects.get(username = user_name)#读取该用户信息
            if pass_word==user.password:#检查密码是否匹配
                request.session['IS_LOGIN'] = True
                request.session['nickname'] = user.nickname
                request.session['username'] = user_name
                return render(request,'web/logsuccess.html',{'user':user})
            else:
                return render(request,'web/login.html',{'error': '密码错误!'})
        else:
            return render(request, 'web/login.html', {'error': '用户名不存在!'})
    else:
        return render(request,'web/login.html')



def web_index(request):
    displaysobj1 = displays1.objects.all()
    displaysobj2 = displays2.objects.all()

    return render(request,'web/index.html',{'displays1':displaysobj1 , 'displays2':displaysobj2})


def get_dishes(request):
    dishes1 = dishes.objects.all()
    return render(request,'web/dishes.html',{'awards':dishes1})


def aboutus(request):
    return render(request,"web/about.html")


def vip(request):
    return render(request,"web/vip.html")







def makeremark(request):

    if request.method=="POST":
        u = request.POST.get("username", None)

        r = request.POST.get("remark", None)

        models.remarkTables.objects.create(
            username = u,

            remark = r,
        )
    user_list = models.remarkTables.objects.all()

    return render(request, "web/remark.html", {"user_list":user_list})



def showfood(request):
    dishes1 = dishes.objects.all()



    if request.method=="POST":
        d = request.POST.get("description", None)

        models.cart.objects.create(
            description = d,

        )
    cart_dishes = models.cart.objects.all()
    if request.method=="GET":
        models.cart.objects.all().delete()
    user_list = models.cart.objects.all()
    return render(request,"web/cart.html",{'awards':dishes1,'cart':user_list})


# def shoppingchart(request):
#     if request.method=="GET":
#         models.cart.objects.all().delete()
#     user_list = models.cart.objects.all()

#     return render(request,"web/shoppingchart.html",{'cart':user_list})
def shoppingchart(request):


    return render(request,"web/shoppingchart.html",{'order':cart_dishes})

from django.forms.models import model_to_dict

def pay(request):
    cart_dishes = models.cart.objects.all()
    
    

    return render(request,"web/pay.html",{'order':cart_dishes})

def pay_done(request):
    cart_dict = models.cart.objects.values('description')
    dishes = ""
    for item in cart_dict.values():
        dishes += item['description']        
    models.historyOrder.objects.create(
            his_dishes = dishes
        )
    history_Order = models.historyOrder.objects.all()
    models.cart.objects.all().delete()

    return render(request,"web/pay_done.html",{"hisorder":history_Order})

