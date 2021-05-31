#main project urls

from django.contrib import admin
from django.urls import path, include

#the below is for line 16
from django.conf import settings
from django.conf.urls.static import static

#with namespacing and app/template/app setup...
# 1) to access a view do appName:viewName 
# 2) to access a template do appName/templateName
# 3) to access a url do appName/pathRoute where pathRoute is the first argument in path()

urlpatterns = [  #when ading an entry in urlpatterns, they tend to go both ways (the app to the project) and should also add it in app views
    
    path('', include('travello.urls')), #empty, effectively our default
    path('accounts/', include('accounts.urls')),
    path('destinations/', include('destinations.urls')),
    path('admin/', admin.site.urls),
    

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#this specifies the media url so it knows where to look to show the media options (like in the admin panel for creating destination objects)

