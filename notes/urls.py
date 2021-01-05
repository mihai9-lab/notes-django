from django.urls import path
from . import views
app_name = 'notes'
urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('home', views.home, name="home"),
    path('completed', views.completed, name="completed"),
    path('new-note', views.new, name="new_note"),
    path('edit/<int:id>/', views.edit, name="edit_note"),
    path('complete/<int:id>/', views.complete, name="complete_note"),
    path('delete/<int:id>/', views.delete, name="delete_note")
]
