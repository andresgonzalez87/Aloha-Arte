from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.index, name='inicio_app'),
    path('getproperties/', views.get_properties, name='getproperties_app'),
    path('createpropertie/', views.create_propertie, name='getproperties_app'),
    path('propertie/<int:id>/', views.detail_propertie, name='gtpropertie_app'),
    path('deletepropertie/<int:id>/', views.delete_propertie, name='deletepropertie_app'),
    path('updatepropertie/<int:id>/', views.update_propertie, name='updatepropertie_app'),
    
]