from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "destinations"
urlpatterns = [
    path('', views.all_destinations.as_view(), name='all_destinations'), 
    path('<str:city_name>/', views.details.as_view(), name='details'),

    # the above line was originally: path("A City", views.A_City, name="A_City"),
    # then it was: path('<str:city_name>/', views.details, name='details'), 
    # ... but now we don't have to explicitely write the path for every new destination object

    path("accounts/", include("accounts.urls")),

]