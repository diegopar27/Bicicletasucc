from django.db import models

# Create your models here.


class Store(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255,
                            blank=True,
                            null=True,
                            verbose_name='Nombre de la tienda')
    address = models.CharField(max_length=255,
                               blank=True,
                               null=True,
                               verbose_name='Direccion de la tienda')
    contact_number = models.CharField(max_length=10,
                                      blank=True,
                                      null=True,
                                      verbose_name='Numero de contacto')
    phone = models.CharField(max_length=14,
                             blank=True,
                             null=True,
                             verbose_name='Telefono')
    email = models.EmailField(max_length=50,
                             null=True,
                             blank=True,
                             verbose_name='Correo electronico')
    website = models.URLField(max_length=255,
                              blank=True,
                              null=True,
                              verbose_name='Sitio web')

    def __str__(self):
        return self.name