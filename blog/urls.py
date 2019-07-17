from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blogpost/<int:id>', views.blogpost, name='blogpost'),
    path('blogview/', views.blogview, name='blogview'),
    path('blogviewall/', views.blogviewall, name='blogviewall'),
    path('blogedit/<int:id>', views.blogedit, name='blogedit'),
    path('blogupdate/<int:id>', views.blogupdate, name='blogupdate'),

]