#前台大堂点餐端子路由文件
from django.urls import path

from web.views import index

app_name = "web"
urlpatterns = [
    path('',index.web_index,name = "web_index"),
    path('dishes/',index.get_dishes,name = "dishes"),
    path('aboutus/',index.aboutus,name = "aboutus"),
    path('index_unlog/',index.index_unlog,name = "index_unlog"),
    path('remark/',index.makeremark,name = "remark"),
    path('login/',index.login,name='login'),
    path('cart/',index.showfood,name='cart'),
    path('pay/',index.pay,name='pay'),
    path('pay_done/',index.pay_done,name='pay_done'),
    path('echarts/',index.echarts,name='echarts'),

    
]
