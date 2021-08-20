from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.contact),
    path("<str:value>/", views.resume),
    path("", views.home)
]
