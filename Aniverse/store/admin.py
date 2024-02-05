from django.contrib import admin
from store.models import storage

class admin_store(admin.ModelAdmin):
    list_display = ('name' , 'dis' , 'img' ,'slug' , 'i_img')
admin.site.register(storage , admin_store)

