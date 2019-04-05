from django.urls import path
from . import views

# using path() we will map url to view function

# /product/new

urlpatterns = [
    path('', views.index),
    path('new', views.new),

]

# in this List we mapp various uls to view function
