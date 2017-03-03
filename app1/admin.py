from django.contrib import admin

# Register your models here.

from models import *

class UsertDesc(admin.ModelAdmin):
    list_display = ('id','name','password')

class BlogDesc(admin.ModelAdmin):
    list_display = ('id','title','author','create')

admin.site.register(User,UsertDesc)
admin.site.register(Blog,BlogDesc)