# Importing Modules
from django.urls import path
from . import views

# URL pattern/URL routes
urlpatterns = [
    path("", views.main,name='index'),
    path("success/", views.createList, name='success'),
    path("<id>/delete",views.deleteRecord,name='delete'),
]
