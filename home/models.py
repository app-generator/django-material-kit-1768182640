# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Admin(models.Model):

    #__Admin_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)

    #__Admin_FIELDS__END

    class Meta:
        verbose_name        = _("Admin")
        verbose_name_plural = _("Admin")


class Usurio(models.Model):

    #__Usurio_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)

    #__Usurio_FIELDS__END

    class Meta:
        verbose_name        = _("Usurio")
        verbose_name_plural = _("Usurio")


class Pedidos(models.Model):

    #__Pedidos_FIELDS__
    user_id = models.ForeignKey(usurio, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    productos = models.TextField(max_length=255, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Pedidos_FIELDS__END

    class Meta:
        verbose_name        = _("Pedidos")
        verbose_name_plural = _("Pedidos")


class Productos(models.Model):

    #__Productos_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    provehedor = models.ForeignKey(provehedor, on_delete=models.CASCADE)

    #__Productos_FIELDS__END

    class Meta:
        verbose_name        = _("Productos")
        verbose_name_plural = _("Productos")


class Provehedor(models.Model):

    #__Provehedor_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    codigo = models.IntegerField(null=True, blank=True)

    #__Provehedor_FIELDS__END

    class Meta:
        verbose_name        = _("Provehedor")
        verbose_name_plural = _("Provehedor")



#__MODELS__END
