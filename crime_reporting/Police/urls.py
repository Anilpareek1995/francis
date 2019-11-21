from django.urls import path
from . import views

urlpatterns = [

 path("pmissing/",views.pmissing, name='pmissing'),
 path(" policehome/",views.policehome, name='policehome'),
 path("mostwanted/",views.mostwanted, name='mostwanted'),
 
 ]