#urls for mapping this app to the main project
from django.urls import path
from . import views

app_name = 'travello'
urlpatterns = [
    path("",views.index, name="index"),  #empty as the default homepage   
]