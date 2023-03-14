import json
import requests

from django.views import generic
from django.http import JsonResponse
from django.urls import reverse_lazy
from apiapp.models import User, Rol, Permissions
from .forms import UserForm, RolForm, PermissionsForm


# URL de la API que se utilizo
URL_API = 'https://super-heroes-giweb-default-rtdb.firebaseio.com/heroes.json'
# URL de la API especifica por id
SPECIFIC_URL_API = 'https://super-heroes-giweb-default-rtdb.firebaseio.com/heroes/-MwlGkB5cL76_RxvO-2B.json'
DELETE_URL_API = 'https://super-heroes-giweb-default-rtdb.firebaseio.com/heroes/-NQNL_SkH2e5wdwci1jD.json'


class ApiView(generic.DetailView):

    # Solicitud Get
    def get_api(self):
        response = requests.get(URL_API)
        if response.status_code == 200:
            response_data = response.json()
        else:
            response_data = {'message':
                             'La solicitud no fue exitosa. Código de estado:',
                             'data': response.status_code}
        return JsonResponse(response_data, status=200)

# Solicitud Post
    def post_api(self):
        data = {'altura': '1.89', 'comics': 'Marvel', 'edad': '97', 'genero': 'Masculino', 'heroe': 'Capitan America',
                'imagen': 'imagencita', 'nombre': 'Steve Rogers', 'poderes': 'Fuerza, no envejece'}
        json_datos = json.dumps(data)
        response = requests.post(URL_API, data=json_datos)
        if response.status_code == 200:

            response_data = {
                'message': 'Datos recibidos', 'data': json_datos}
        else:
            response_data = {'message':
                             'La solicitud no fue exitosa. Código de estado:',
                             'data': response.status_code}
        return JsonResponse(response_data)

# Solicitud Put
    def put_api(self):
        data = {'altura': '1.89', 'comics': 'Marvel', 'edad': '97', 'genero': 'Masculino', 'heroe': 'Capitan America',
                'imagen': 'imagencita', 'nombre': 'Steve Rogers', 'poderes': 'Fuerza, no envejece'}
        datos_json = json.dumps(data)
        response = requests.put(SPECIFIC_URL_API, data=datos_json)
        if response.status_code == 200:
            response_data = {'message':
                             'Datos recibidos y actualizados correctamente  ',
                             'data': datos_json}
        else:
            response_data = {'message': 'La solicitud no fue exitosa. Código de estado:',
                             'data': response.status_code}
        return JsonResponse(response_data)

# Solicitud Delete
    def delete_api(self):
        response = requests.delete(DELETE_URL_API)
        if response.status_code == 200:
            response_data = {'message':
                             'Datos eliminados correctamente',
                             'data': response.status_code}
        else:
            response_data = {'message': 'La solicitud no fue exitosa. Código de estado:',
                             'data': response.status_code}
        return JsonResponse(response_data)

# CRUD delos usrios Rol Permisos


class UserList(generic.ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'


class UserDetail(generic.DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'


class UserCreate(generic.CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('user_list')


class UserUpdate(generic.UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('user_list')


class UserDelete(generic.DeleteView):
    model = User
    template_name = 'user/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

# CRUD Rol


class RolList(generic.ListView):
    model = Rol
    template_name = 'rol/rol_list.html'
    context_object_name = 'rols'


class RolDetail(generic.DetailView):
    model = Rol
    template_name = 'rol/rol_detail.html'
    context_object_name = 'rol'


class RolCreate(generic.CreateView):
    model = Rol
    form_class = RolForm
    template_name = 'rol/rol_create.html'
    success_url = reverse_lazy('rol_list')


class RolUpdate(generic.UpdateView):
    model = Rol
    form_class = RolForm
    template_name = 'rol/rol_create.html'
    success_url = reverse_lazy('rol_list')


class RolDelete(generic.DeleteView):
    model = Rol
    template_name = 'rol/rol_confirm_delete.html'
    success_url = reverse_lazy('rol_list')


# CRUD Permisssions

class PermissionsList(generic.ListView):
    model = Permissions
    template_name = 'permissions/permissions_list.html'
    context_object_name = 'permissionss'


class PermissionsDetail(generic.DetailView):
    model = Permissions
    template_name = 'permissions/permissions_detail.html'
    context_object_name = 'permissions'


class PermissionsCreate(generic.CreateView):
    model = Permissions
    form_class = PermissionsForm
    template_name = 'permissions/permissions_create.html'
    success_url = reverse_lazy('permissions_list')


class PermissionsUpdate(generic.UpdateView):
    model = Permissions
    form_class = PermissionsForm
    template_name = 'permissions/permissions_create.html'
    success_url = reverse_lazy('permissions_list')


class PermissionsDelete(generic.DeleteView):
    model = Permissions
    template_name = 'permissions/permissions_confirm_delete.html'
    success_url = reverse_lazy('permissions_list')
