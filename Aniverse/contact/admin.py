from django.contrib import admin
from .models import Contact

class admin_contact(admin.ModelAdmin):
    list_display = ('name', 'email' , 'created_at')
admin.site.register(Contact , admin_contact) 
