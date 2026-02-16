from . import views
from django.urls import path

urlpatterns = [
    path('', views.getData, name='get-data'),
    path('add/', views.addItem, name='add-item'),
]