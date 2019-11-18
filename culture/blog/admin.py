from django.contrib import admin
from . import models
from tinymce import HTMLField
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add', 'date_upd', 'statut',)
    list_filter = ('date_add', 'date_upd', 'statut',)
    list_search = ('nom')
    ordering = ('nom',)
    list_per_page = 5
    actions = ('active', 'desactive',) 
    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'Activer une categorie')
    active.short_description = 'active categorie'
    
    def desactive(self, request, queryset):
        queryset.update(statut = False)
        self.message_user(request, 'Desactiver une categorie')
    desactive.short_description = 'desactive categorie'
    


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date', 'description', 'content', 'date_add', 'date_upd', 'statut', 'categorie', 'auteur','view_image',)
    list_filter = ('date_add', 'date', 'date_upd', 'statut',)
    list_search = ('titre')
    ordering = ('titre',)
    list_per_page = 5
    readonly_fields = ['detail_image']
    filter_horizontal = ('tag',)
    actions = ('active', 'desactive',)
    
    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'Activer une Article')
    active.short_description = 'active Article'
    
    def desactive(self, queryset, request):
        queryset.update(statut = False)
        self.message_user(request, 'Desactiver une Article')
    desactive.short_description = 'desactive Article'
    
    def view_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))
    
    def detail_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))



@admin.register(models.Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('date', 'message', 'date_add', 'date_upd', 'statut', 'article', 'nom', 'view_image',)
    list_filter = ('date_add', 'date', 'date_upd', 'statut',)
    list_search = ('nom',)
    ordering = ('nom',)
    list_per_page = 5
    
    readonly_fields = ['detail_image']
    actions = ('active', 'desactive',) 
    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'Activer une Commentaire')
    active.short_description = 'active Commentaire'
    
    def desactive(self, request, queryset):
        queryset.update(statut = False)
        self.message_user(request, 'Desactiver une Commentaire')
    desactive.short_description = 'desactive Commentaire'
    def view_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))
    
    def detail_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))






@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add', 'date_upd', 'statut',)
    list_filter = ('date_add', 'date_upd', 'statut',)
    list_serach = ('nom')
    list_per_page = 5
    ordering = ('nom',)
    