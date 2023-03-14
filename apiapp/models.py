from django.db import models


class User(models.Model):
    password = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Rol(models.Model):
    name_rol = models.CharField(max_length=200, null=True)
    user = models.ManyToManyField(User, null=True)

    def __str__(self):
        return self.name_rol


class Permissions(models.Model):
    name_permissions = models.CharField(max_length=200, null=True)
    function = models.CharField(max_length=200, null=True)
    rol = models.ManyToManyField(Rol, null=True)
