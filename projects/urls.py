from django.urls import path
from . import views



urlpatterns = [
    path('', views.projects, name="projects"),
    path('projectjhgf/<str:pk>/', views.projct, name="project"),
]