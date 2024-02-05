from django.contrib import admin
from Anime.models import a_anime , b_anime , c_anime

class a_admin(admin.ModelAdmin):
    list_display = ('name', 'dis' , 'img')
admin.site.register(a_anime ,a_admin)    

class b_admin(admin.ModelAdmin):
    list_display = ('name', 'dis' , 'img')
admin.site.register(b_anime ,b_admin)    

class c_admin(admin.ModelAdmin):
    list_display = ('name', 'dis' , 'img')
admin.site.register(c_anime ,c_admin)    


