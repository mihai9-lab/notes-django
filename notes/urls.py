from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="notes_index"),
    path('page', views.page, name="notes_page")
]
