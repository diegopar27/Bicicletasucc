from django.db import models
from categoryapp.models import Category
# Create your models here.


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255,
                            blank=True,
                            null=True,
                            verbose_name="Nombre")
    price = models.CharField(max_length=10,
                             blank=True,
                             null=True,
                             verbose_name="Precio")
    model = models.CharField(max_length=255,
                             blank=True,
                             null=True,
                             verbose_name="Modelo")
    types = models.CharField(max_length=255,
                             blank=True,
                             null=True,
                             verbose_name="Tipo")
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True,
                                 verbose_name='Categoria')

    def __str__(self):
        return self.name
