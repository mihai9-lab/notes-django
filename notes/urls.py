from django.urls import path
from . import views
app_name = 'notes'
urlpatterns = [
    path('', views.index, name="index"),
    path('register',views.register,name="register"),
    path('new-note',views.new,name="new_note")
]
