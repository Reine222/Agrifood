from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import *
from agri.models import *



###################################################### BLOG #######################################################

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 1

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'
        depth = 1


class ArticleSerializer(serializers.ModelSerializer):
    blog_image = CategorieSerializer(many=True, required=False)
    UserArticle = UserSerializer(many=True, required=False)
    class Meta:
        model = Article
        fields = '__all__'
        depth = 1



class CommentaireSerializer(serializers.ModelSerializer):
    ArticleCommentaire = ArticleSerializer(many=True, required=False)
    UserCommentaire = UserSerializer(many=True, required=False)
    class Meta:
        model = Commentaire
        fields = '__all__'
        depth = 2

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

###################################################### AGRI #######################################################


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        depth = 1

class ProduitSerializer(serializers.ModelSerializer):
    CategorieProduit = CategoriesSerializer(many=True, required=False)
    class Meta:
        model = Produit
        fields = '__all__'


class PanierSerializer(serializers.ModelSerializer):
    produitPanier = ProduitSerializer(many=True,)
    UserPanier = UserSerializer(many=True, required=False)
    class Meta:
        model = Panier
        fields = '__all__'
        depth = 1

class ProfileSerializer(serializers.ModelSerializer):
    profileUser = UserSerializer(many=True, required=False)
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1


class TemoignageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temoignage
        fields = '__all__'
        depth = 1

class FormCommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormCommande
        fields = '__all__'

class CaisseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caisse
        fields = '__all__'

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'
