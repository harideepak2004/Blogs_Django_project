from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('del/<int:id>/', views.delete_blog, name="delete_blog"),

]
