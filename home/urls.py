
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.index),
    path('projects/', views.index),
    path('contact/', views.index),

    #path('id<int:video_id>/', views.detail, name = 'detail'),

]
