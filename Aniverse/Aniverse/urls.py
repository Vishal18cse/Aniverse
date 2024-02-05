"""
URL configuration for Aniplex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Aniverse import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index , name = 'index'),
    path('signup/' , views.signup , name = 'signup'),
    path('login/' , views.main_login , name = 'login'),
    path('search/' ,views.search , name = 'search'),
    path('logout/' ,views.logout_view),
    path('anime/' , views.anime),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('favourite/', views.favourite, name='favourite'),
    path('contact/' , views.contact), 
    path('comment/' , views.comment , name = 'comment'),
    path('<slug>/' , views.slug , name = 'slug'),
    path('trending/<slug>/' , views.t_slug),
    path('recent/<slug>/' , views.r_slug),
    path('top/<slug>/' , views.top_slug),
    path('movies/<slug>/' , views.m_slug),
    path('delete-from-watchlist/<int:product_id>/', views.delete_from_watchlist, name='delete_from_watchlist'),
    path('delete-from-favourite/<int:product_id>/', views.delete_from_favourite, name='delete_from_favourite'),
   
]   
   

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)