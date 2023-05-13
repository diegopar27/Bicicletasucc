from django.db import models

from productapp.models import Product
from storeapp.models import Store


class ProdcutxStore(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True,
                              verbose_name='Tienda')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
                                verbose_name='Producto')

    def __str__(self):
        return f"ProdcutxStore(store={self.store}, product={self.product})"
