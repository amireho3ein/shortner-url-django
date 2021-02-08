from django.urls import path
from backend.shortner import views

urlpatterns = [
   path('', views.base, name='base'),
   path('carete/', views.create, name='create'),
   path('<str:pk>', views.get_url, name='get_url') 
]