from django.contrib import admin
from trending.models import trending_anime

class trending_admin(admin.ModelAdmin):
    list_display = ('name', 'dis' , 'img' ,'trend_slug')
admin.site.register(trending_anime,trending_admin)    
