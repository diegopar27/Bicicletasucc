from django.db import models


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255,
                            blank=True,
                            null=True,
                            verbose_name='Categoria')

    def __str__(self):
        return self.name
