import json
import requests

from django.views import generic
from django.http import JsonResponse

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
