from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_service_category, name='add_category'),

    path('mechanics/', views.mechanic_list, name='mechanic_list'),
    path('mechanics/add/', views.add_mechanic, name='add_mechanic'),

    path('services/', views.service_list, name='service_list'),
    path('services/add/', views.add_service, name='add_service'),
]