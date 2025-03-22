from django.urls import path,include
from Staff import views

app_name="Staff"

urlpatterns = [
    path('StaffDashboard/', views.Staff,name="StaffDashboard"),
    path('leave/', views.leave,name="leave"),
    path('deleterq/<int:id>',views.deleterq,name='deleterq'),

]