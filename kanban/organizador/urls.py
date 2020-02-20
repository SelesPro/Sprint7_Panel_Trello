from django.urls import path, include

from . import views 

urlpatterns = [ 
    path("index", views.index, name='index'),
    path('creartarea', views.creartarea, name='creartarea'),
    path('consultartablero', views.consultartablero, name='consultartablero'),
    path('infotablero/<int:id>', views.infotablero, name='infotablero'),
]