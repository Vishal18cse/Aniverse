from django.contrib import admin
from top.models import top_airing

class top_admin(admin.ModelAdmin):
    list_display = ('name', 'dis' , 'img' , 'top_slug' )
admin.site.register(top_airing , top_admin)    
