from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('Eleve-list/', views.EleveList, name="Eleve-list"),
    path('Eleve-create/', views.EleveCreate, name="Eleve-create"),
    path('Eleve-delete/<str:pk>/', views.EleveDelete, name="Eleve-delete"),
    path('Eleve-update/<str:pk>/', views.EleveUpdate, name="Eleve-update"),
]