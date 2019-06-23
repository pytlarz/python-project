from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('place_model', views.place_model, name='place_model'),
    path('listy', views.listy, name='listy'),
    path('slowniki', views.slowniki, name='slowniki'),
    path('time', views.current_datetime, name='current_datetime'),
]
