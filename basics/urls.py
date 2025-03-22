from django.urls import path,include
from basics import views

urlpatterns = [
    path('add/',views.add,name='add'),
    path('largest/',views.largest,name='largest'),
]
