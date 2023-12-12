from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('details/<slug:prop_slug>/', views.propert, name='details'),
]