from django.contrib import admin
from web.models import dishes,displays1,displays2,historyOrder
class dishesAdmin(admin.ModelAdmin):
    list_display = ['description', 'photo']
admin.site.register(dishes,dishesAdmin)


class displays1Admin(admin.ModelAdmin):
    list_display = ['photo']
admin.site.register(displays1,displays1Admin)

class displays2Admin(admin.ModelAdmin):
    list_display = ['photo']
admin.site.register(displays2,displays2Admin)

class historyOrderAdmin(admin.ModelAdmin):
    list_display = ['his_dishes']
admin.site.register(historyOrder,historyOrderAdmin)