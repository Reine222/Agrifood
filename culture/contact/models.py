from django.db import models

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    sujet = models.CharField(max_length=250)
    message = models.TextField()
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
