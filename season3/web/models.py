from distutils.command.upload import upload
from django.db import models
from django.contrib import  admin
from django.urls import reverse
from django.utils.timezone import now


from django import forms
# Create your models here.
TOPIC_CHOICES=(
    ('level1','Bad'),
    ('level2','Soso'),
    ('level3','Good'),
)

class Remark(models.Model):
    subject = models.CharField(max_length=100)
    mail = models.EmailField()
    topic = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    cc_myself = models.BooleanField()

    def __str__(self):
        return self.subject

    class Meta:
        ordering=['subject']

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 200)
    nickname = models.CharField(max_length = 50,default='匿名')
    email = models.EmailField()
    created_time = models.CharField(max_length=50,default=now)
    comment_num = models.PositiveIntegerField(verbose_name='评论数', default=0)
    avatar = models.ImageField(upload_to = 'media', default="media/default.png")

    def __str__(self):
        return self.username

    def comment(self):
        self.comment_num += 1
        self.save(update_fields=['comment_num'])

    def comment_del(self):
        self.comment_num -= 1
        self.save(update_fields=['comment_num'])

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email')
#修饰器



#菜品
class dishes(models.Model):
    description = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                 )
    photo = models.ImageField(upload_to='media/dishies/',
                              blank=True,
                              )


class displays1(models.Model):
    photo = models.ImageField(upload_to='media/displays1/',
                            )

class displays2(models.Model):
    photo = models.ImageField(upload_to='media/displays2/',
                                )



from django.db import models

# Create your models here.

class remarkTables(models.Model):
    username = models.CharField(max_length=64)
    #sex = models.CharField(max_length=64)
    #email = models.CharField(max_length=64)
    remark = models.CharField(max_length=10000)




class cart(models.Model):
    description = models.TextField(max_length=500,
                                    blank=True,
                                    null=True,
                                    )

 


class historyOrder(models.Model):
    his_dishes = models.TextField(max_length=1000,
                                    blank=True,
                                    null=True,
                                    )
