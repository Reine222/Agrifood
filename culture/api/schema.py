import graphene
from blog.models import *
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategorieNode(DjangoObjectType):
    class Meta:
        model = Categorie
        filter_fields = ['nom', 'CategorieArticle', 'date_add', 'date_upd', 'statut']
        interfaces = (relay.Node, )


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        filter_fields = ['nom', 'TagArticle', 'date_add', 'date_upd', 'statut']
        interfaces = (relay.Node, )
    
class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        # Allow for some more advanced filtering here
        filter_fields = {
            'image': [],
            'titre': ['exact', 'icontains', 'istartswith'],
            'date': ['exact', 'icontains'],
            'categorie': ['exact'],
            'categorie__id': ['exact'],
            'auteur':  ['exact'],
            'auteur__id': ['exact'],
            'tag': ['exact'],
            'tag__id': ['exact'],
            'description': ['exact', 'icontains', 'istartswith'],
            'content': ['exact', 'icontains', 'istartswith'],
            'date_add': ['exact', 'icontains', 'istartswith'],
            'date_upd': ['exact', 'icontains', 'istartswith'],
            'statut': ['exact', 'icontains', 'istartswith'],
            
        }
        interfaces = (relay.Node, )

class CommentaireNode(DjangoObjectType):
    class Meta:
        model = Commentaire
        # Allow for some more advanced filtering here
        filter_fields = {
            'image': [],
            'nom': ['exact'],
            'nom__id': ['exact'],
            'date': ['exact', 'icontains'],
            'article': ['exact'],
            'article__id': ['exact'],
            'message': ['exact', 'icontains', 'istartswith'],
            'date_add': ['exact', 'icontains', 'istartswith'],
            'date_upd': ['exact', 'icontains', 'istartswith'],
            'statut': ['exact', 'icontains', 'istartswith'],
            
        }
        interfaces = (relay.Node, )


class CommentNode(DjangoObjectType):
    class Meta:
        model = Comment
        # Allow for some more advanced filtering here
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'email': ['exact', 'icontains', 'istartswith'],
            'web': ['exact', 'icontains', 'istartswith'],
            'message': ['exact', 'icontains', 'istartswith'],
            'date_add': ['exact', 'icontains', 'istartswith'],
            
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    categorie = relay.Node.Field(CategorieNode)
    all_categories = DjangoFilterConnectionField(CategorieNode)

    tag = relay.Node.Field(TagNode)
    all_tags = DjangoFilterConnectionField(TagNode)
    
    article = relay.Node.Field(ArticleNode)
    all_articles = DjangoFilterConnectionField(ArticleNode)

    commentaire = relay.Node.Field(CommentaireNode)
    all_commentaires = DjangoFilterConnectionField(CommentaireNode)

    comment = relay.Node.Field(CommentNode)
    all_comments = DjangoFilterConnectionField(CommentNode)