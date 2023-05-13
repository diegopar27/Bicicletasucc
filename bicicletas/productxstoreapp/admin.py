from django.contrib import admin
from .models import ProdcutxStore


@admin.register(ProdcutxStore)
class ProductxStoreAdmin(admin.ModelAdmin):
    list_display = ('store', 'product')
    list_filter = ('store', 'product')

