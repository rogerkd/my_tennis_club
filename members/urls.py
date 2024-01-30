from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.Name, name='Name'),
    path('members/details/<int:id>', views.details, name='details'),
    path('', views.main, name='main'),
    path('members/table/', views.table, name='table'),
]
 