from unicodedata import name
from django.urls import path,include
from predition import views

urlpatterns = [
    path("",views.pred),
    path("result/",views.show,name='show')
]