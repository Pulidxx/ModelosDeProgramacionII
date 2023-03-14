from django import forms
from .models import User, Rol, Permissions


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']


class RolForm(forms.ModelForm):
    user = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Rol
        fields = ['name_rol', 'user']


class PermissionsForm(forms.ModelForm):
    rol = forms.ModelMultipleChoiceField(
        queryset=Rol.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Permissions
        fields = ['name_permissions', 'function', 'rol']
