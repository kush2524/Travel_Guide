
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
   path('search/', views.city_search, name='search_results'),
  path('input/', views.input, name='map'),
  path('route/', views.get_route, name='get_route'),
  path('city-info/', views.happening_places, name='city_info'),

  
]