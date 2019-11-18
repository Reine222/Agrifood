from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewset import *

router = DefaultRouter()
router.register('categorie', CategorieViewset, base_name= 'categorie')
router.register('article', ArticleViewset, base_name= 'article')
router.register('commentaire', CommentaireViewset, base_name= 'commentaire')
router.register('tag', TagViewset, base_name= 'tag')
router.register('user', UserViewset, base_name= 'user')
router.register('comment', CommentViewset, base_name= 'comment')


router.register('categories', CategoriesViewset, base_name= 'categories')
router.register('produit', ProduitViewset, base_name= 'produit')
router.register('panier', PanierViewset, base_name= 'panier')
router.register('profile', ProfileViewset, base_name= 'profile')
router.register('temoignage', TemoignageViewset, base_name= 'temoignage')
router.register('caisse', CaisseViewset, base_name= 'caisse')
router.register('newsletter', NewsletterViewset, base_name= 'newsletter')
router.register('formCommande', FormCommandeViewset, base_name= 'formCommande')


urlpatterns = [
    #...
]

urlpatterns += router.urls
