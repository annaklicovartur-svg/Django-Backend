from django.urls import path
from . import views

urlpatterns = [ 
    path ('', views.bitch ),
    path('render', views.bitch),
    path('boodstrap', views.boodstrap),
    path('work', views.workshowing),
    path('create', views.create),
    path('creatework', views.creatework),
    ]