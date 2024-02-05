from django.urls import path
from .views import add_to_wishlist

app_name = 'store'

urlpatterns = [
    # Other URL patterns...
    path('wishlist/', add_to_wishlist, name='add_to_wishlist'),
]
