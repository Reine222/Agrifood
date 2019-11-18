from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce import HTMLField

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()
    def __str__(self):
        return self.nom


class Article(models.Model):
    image = models.ImageField(upload_to='blog_image')
    titre = models.CharField(max_length=250)
    date = models.DateField(auto_now=False, auto_now_add=False)
    categorie = models.ForeignKey("Categorie", on_delete=models.CASCADE, related_name = 'CategorieArticle')
    auteur = models.ForeignKey( User, on_delete=models.CASCADE, related_name = 'UserArticle')
    description = models.TextField()
    content = HTMLField('Content')
    tag = models.ManyToManyField("Tag",related_name ='TagArticle')
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()
    def __str__(self):
        return self.titre



class Commentaire(models.Model):
    image = models.ImageField(upload_to='blog_image')
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    nom =models.ForeignKey(User, on_delete=models.CASCADE, related_name = "UserCommentaire")
    message = models.TextField()
    article = models.ForeignKey("Article", on_delete=models.CASCADE, related_name = "ArticleCommentaire")
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()
    # def __str__(self):
    #     return self.nom


class Tag(models.Model):
    nom = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)
    statut = models.BooleanField()
    def __str__(self):
        return self.nom



class Comment(models.Model):
    nom = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    web = models.URLField(max_length=200)
    message = models.TextField()
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)

