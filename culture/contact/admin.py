from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'message', 'date_add', 'date_upd',)
    list_filter = ('date_add', 'date_upd',)
    list_serach = ('email')
    list_per_page = 5
    ordering = ('nom',)
    