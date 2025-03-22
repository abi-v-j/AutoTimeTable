from django.urls import path,include
from Admin import views

app_name="Admin"

urlpatterns = [
    path('Department/',views.Department,name='Department'),
    path('deletedepartment/<int:id>',views.deletedepartment,name='deletedepartment'),
    path('Semester/',views.Semester,name='Semester'),
    path('deletesemester/<int:id>',views.deletesemester,name='deletesemester'),
    path('Academic_year/',views.Academic_year,name='Academic_year'),
    path('deleteacyear/<int:id>',views.deleteacyear,name='deleteacyear'),
    path('AdminRegistration/',views.AdminRegistration,name='AdminRegistration'),
    path('deleteadmr/<int:id>',views.deleteadmr,name='deleteadmr'),
    path('editadmr/<int:id>',views.editadmr,name='editadmr'),
    path('editdep/<int:id>',views.editdep,name='editdep'),
    path('Dashboard/',views.Dashboard,name='Dashboard'),
    path('Subject/',views.Subject,name='Subject'),
    path('HOD/',views.HOD,name='HOD'),
    path('deletehod/<int:id>',views.deletehod,name='deletehod'),
    path('edithod/<int:id>',views.edithod,name='edithod'),
    path('generate_timetable/', views.generate_timetable, name='generate_timetable'),
    path('view_timetable/', views.view_timetable, name='view_timetable'),
]