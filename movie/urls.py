from django.contrib import admin
from django.urls import path
from .views import home,movie_view,movie_Add,movie_edit,movie_delete

app_name = 'movie' 

urlpatterns = [
    path('home/', home, name='home'),
    path('view/<int:id>', movie_view, name='movie_view'),
    path('edit/<int:pk>', movie_edit, name='movie_edit'),
    path('add', movie_Add, name='movie_Add'),
    path('delete/<int:id>', movie_delete, name='movie_delete'),
    

]