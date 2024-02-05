from django.contrib import admin
from recent.models import recently_updated

class recent_admin(admin.ModelAdmin):
    list_display = ('name', 'dis' , 'img' , 'recent_slug')
admin.site.register(recently_updated, recent_admin)    