from django.contrib import admin
from movies.models import anime_movies

class movies_admin(admin.ModelAdmin):
    list_display = ('name' , 'dis' , 'img' ,'movie_slug')
admin.site.register(anime_movies , movies_admin)   
