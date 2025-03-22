from django.urls import path,include
from Hod import views

app_name="Hod"

urlpatterns = [
    path('staff/',views.staff,name='staff'),
    path('view_leave_application/',views.view_leave_application,name='view_leave_application'),
    path('approverq/<int:id>',views.approverq,name='approverq'),
    path('rejectrq/<int:id>',views.rejectrq,name='rejectrq'),
    path('assign/<int:id>',views.assign,name='assign'),
    path('ajaxsubject/',views.ajaxsubject,name='ajaxsubject'),
]