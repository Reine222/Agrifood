from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add', 'date_upd', 'statut','view_image',)
    list_filter = ('date_add', 'date_upd', 'statut',)
    list_search = ('nom')
    ordering = ('nom',)
    list_per_page = 5
    readonly_fields = ['detail_image']
    actions = ('active', 'desactive') 
    
    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'Activer une categorie')
    active.short_description = 'active categorie'
    
    def desactive(self, request, queryset):
        queryset.update(statut = False)
        self.message_user(request, 'Desactiver une categorie')
    desactive.short_description = 'desactive categorie'
    
    def view_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))
    
    def detail_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))






@admin.register(models.Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'description', 'stock', 'descripPanier', 'categorie', 'date_add', 'date_upd', 'statut','view_image',)
    list_filter = ('date_add', 'date_upd', 'statut',)
    list_search = ('nom')
    ordering = ('nom',)
    list_per_page = 5
    readonly_fields = ['detail_image']
    actions = ('active', 'desactive',) 
    def active(self, queryset, request):
        queryset.update(statut = True)
        self.message_user(request, 'Activer un produit')
    active.short_description = 'active produit'
    
    def desactive(self, queryset, request):
        queryset.update(statut = False)
        self.message_user(request, 'Desactiver un produit')
    desactive.short_description = 'desactive produit'
    def view_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))
    
    def detail_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))





@admin.register(models.Panier)
class PanierAdmin(admin.ModelAdmin):
    list_display = ('forme', 'quantité', 'total', 'date_add', 'date_upd', 'statut','view_image',)
    list_filter = ('date_add', 'date_upd', 'statut',)
    list_search = ('forme')
    ordering = ('quantité',)
    list_per_page = 5
    filter_horizontal = ('produit',)
    readonly_fields = ['detail_image']
    actions = ('active', 'desactive',) 
    def active(self, queryset, request):
        queryset.update(statut = True)
        self.message_user(request, 'Activer un panier')
    active.short_description = 'active panier'
    
    def desactive(self, queryset, request):
        queryset.update(statut = False)
        self.message_user(request, 'Desactiver un panier')
    desactive.short_description = 'desactive panier'
    def view_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))
    
    def detail_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))





@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'contact', 'image',)
    list_search = ('user')
    ordering = ('user',)
    list_per_page = 5
    #readonly_fields = ['detail_image']
    actions = ('active', 'desactive',) 
    def active(self, queryset, request):
        queryset.update(statut = True)
        self.message_user(request, 'Activer un profile')
    active.short_description = 'active profile'
    
    def desactive(self, queryset, request):
        queryset.update(statut = False)
        self.message_user(request, 'Desactiver un profile')
    desactive.short_description = 'desactive profile'
    # def view_image(self, obj):
    #     return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))
    
    # def detail_image(self, obj):
    #     return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))



@admin.register(models.FormCommande)
class FormCommandeAdmin(admin.ModelAdmin):
    list_display = ('ville', 'code_postal', 'date_add', 'date_upd',)
    list_filter = ('date_add', 'date_upd',)
    list_search = ('ville')
    ordering = ('date_add',)
    list_per_page = 5
    

@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_add', 'date_upd',)
    list_filter = ('date_add', 'date_upd',)
    list_search = ('email')
    ordering = ('date_add',)
    list_per_page = 5


@admin.register(models.Caisse)
class CaisseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'addrress', 'ville', 'code_postal', 'telephone', 'email', 'mode_de_paiement', 'date_add', 'date_upd',)
    list_filter = ('date_add', 'date_upd',)
    list_search = ('nom')
    ordering = ('date_add',)
    list_per_page = 5
    actions = ('active', 'desactive',) 
    def active(self, queryset, request):
        queryset.update(statut = True)
        self.message_user(request, 'Activer un temoignage')
    active.short_description = 'active temoignage'
    
    def desactive(self, queryset, request):
        queryset.update(statut = False)
        self.message_user(request, 'Desactiver un temoignage')
    desactive.short_description = 'desactive temoignage'



@admin.register(models.Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'fonction', 'date_add', 'date_upd', 'statut', 'view_image',)
    list_filter = ('date_add', 'date_upd', 'statut',)
    list_search = ('nom')
    ordering = ('nom',)
    list_per_page = 5
    readonly_fields = ['detail_image']
    actions = ('active', 'desactive',) 
    def active(self, queryset, request):
        queryset.update(statut = True)
        self.message_user(request, 'Activer un temoignage')
    active.short_description = 'active temoignage'
    
    def desactive(self, queryset, request):
        queryset.update(statut = False)
        self.message_user(request, 'Desactiver un temoignage')
    desactive.short_description = 'desactive temoignage'
    def view_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))
    
    def detail_image(self, obj):
        return mark_safe('<img src = "{url}" width ="100px" height ="100px" />'.format(url = obj.image.url))



