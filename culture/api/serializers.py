from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import *
from agri.models import *



###################################################### BLOG #######################################################

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        deph = 1

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'
        deph = 1


class ArticleSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializer(many=True, required=False)
    class Meta:
        model = Article
        fields = '__all__'
        deph = 1



class CommentaireSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(many=True, required=False)
    class Meta:
        model = Commentaire
        fields = '__all__'
        deph = 1

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

###################################################### AGRI #######################################################


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        deph = 1

class ProduitSerializer(serializers.ModelSerializer):
    categorie = CategoriesSerializer(many=True, required=False)
    class Meta:
        model = Produit
        fields = '__all__'


class PanierSerializer(serializers.ModelSerializer):
    produit = ProduitSerializer(many=True, required=False)
    class Meta:
        model = Panier
        fields = '__all__'
        deph = 1

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, required=False)
    class Meta:
        model = Profile
        fields = '__all__'


class TemoignageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temoignage
        fields = '__all__'
        deph = 1

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
