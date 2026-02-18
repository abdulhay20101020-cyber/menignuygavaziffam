from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('service/category/<str:name>/', views.services_by_category),
    path('service/<int:id>/', views.service_detail),
    path('service/mechanic/<int:id>/', views.services_by_mechanic),
]
