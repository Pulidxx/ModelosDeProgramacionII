from django.urls import path
from . import views
urlpatterns = [
    path('get_api/', views.ApiView.get_api , name="get_api"),
    path('post_api/', views.ApiView.post_api , name="post_api"),
    path('put_api/', views.ApiView.put_api , name="put_api"),
    path('delete_api/', views.ApiView.delete_api , name="delete_api"),
    ]