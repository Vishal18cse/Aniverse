from django.contrib import admin
from  .models import Comment

class admin_comment(admin.ModelAdmin):
    list_display = ('user' , 'message', 'anime' , 'created_at')
admin.site.register(Comment , admin_comment)    