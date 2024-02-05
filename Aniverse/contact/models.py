from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100 , blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
