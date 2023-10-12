from EatingUsApp import views
from django.urls import path


urlpatterns = [
    path('', views.inicio),
    path('inicio/', views.inicio, name="Inicio"),
    path('brunch/', views.brunch, name="Brunch"),
    path('almuerzo/', views.almuerzo, name="Almuerzo"),
    path('merienda/', views.merienda, name="Merienda"),
    path('cena/', views.cena, name="Cena"),
    path('nueva_review/', views.nuevaReview, name="Nueva Review"),
    path('mostrar/', views.mostrar, name="Mostrar"),
    path('buscar/', views.buscar, name="Buscar Review")
]
