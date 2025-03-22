from django.urls import path,include
from Guest import views
app_name="Guest"
urlpatterns = [
    path('Login/', views.Login,name="Login"),
    path('index/', views.index,name="index"),
]
