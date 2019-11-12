from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.



class Categorie(models.Model):
    nom = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()
    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    prix = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    descripPanier = models.TextField()
    categorie = models.ForeignKey("Categorie",on_delete=models.CASCADE, related_name = "CategorieProduit")
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()
    def __str__(self):
        return self.nom

class Panier(models.Model):
    forme = models.CharField(max_length=250)
    quantité = models.IntegerField()
    total = models.IntegerField()
    image = models.ImageField(upload_to='images')
    produit = models.ManyToManyField("Produit")
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()
    def __str__(self):
        return self.forme

class FormCommande(models.Model):
    ville = models.CharField(max_length=250)
    code_postal = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)


class Newsletter(models.Model):
    email = models.EmailField(max_length=254)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)


class Caisse(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    addrress = models.CharField(max_length=250)
    ville = models.CharField(max_length=250)
    code_postal = models.CharField(max_length=250)
    telephone = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    mode_de_paiement = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)


class Temoignage(models.Model):
    image = models.ImageField(upload_to="images")
    nom = models.CharField(max_length=250)
    description = models.TextField()
    fonction = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()
    def __str__(self):
        return self.nom


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "profileUser")
    # Initialisation a la creation
    image = models.ImageField(upload_to="profile")
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=250)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        
        instance.profile.save()