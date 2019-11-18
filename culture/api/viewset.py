from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from blog.models import *
from  .serializers import *


###################################################### BLOG #######################################################

class CategorieViewset(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TagViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentaireViewset(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


###################################################### AGRI #######################################################


class CategoriesViewset(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class ProduitViewset(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class PanierViewset(viewsets.ModelViewSet):
    queryset = Panier.objects.all()
    serializer_class = PanierSerializer


class TemoignageViewset(viewsets.ModelViewSet):
    queryset = Temoignage.objects.all()
    serializer_class = TemoignageSerializer

class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CaisseViewset(viewsets.ModelViewSet):
    queryset = Caisse.objects.all()
    serializer_class = CaisseSerializer

class FormCommandeViewset(viewsets.ModelViewSet):
    queryset = FormCommande.objects.all()
    serializer_class = FormCommandeSerializer

class NewsletterViewset(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
