from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rezume', views.rezume, name='rezume'),
    path('contact', views.contact, name='contact'),
    path('create', views.create, name='create'),
]
