
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('home.urls')),

    path('admin/', admin.site.urls),
    ##path('grappelli/', include('grappelli.urls')),

]
