from django.db import models


class User(models.Model):
    password = models.CharField(max_length=50)


class Rol(models.Model):
    name_rol = models.CharField(max_length=200)
    user = models.ManyToManyField(User)


class Permissions(models.Model):
    name_permissions = models.CharField(max_length=200)
    function = models.CharField(max_length=200)
    rol = models.ManyToManyField(Rol)
