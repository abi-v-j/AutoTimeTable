from django.shortcuts import render,redirect
from Admin.models import *
from Staff.models import *
from Hod.models import *

# Create your views here.

def staff(request):
    st=tbl_staff.objects.all()
    dep=tbl_Department.objects.all()
    if request.method == "POST":
        dept = tbl_Department.objects.get(id=request.POST.get('sel_dept'))
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        password=request.POST.get('txt_password')
        tbl_staff.objects.create(department=dept,staff_name=name,staff_email=email,staff_contact=contact,staff_password=password)
        return render(request,'Hod/staff.html',{'st':st,'dep':dep})
    else:
        return render(request,'Hod/staff.html',{'st':st,'dep':dep})
    
def view_leave_application(request):
    lv=tbl_leave.objects.all()
    st=tbl_staff.objects.get(id=request.session['sid'])
    return render(request,'Hod/view_leave_application.html',{'leave':lv,'staff':st})

def rejectrq(request,id):
    data=tbl_leave.objects.get(id=id)
    data.status=2
    data.save()
    return redirect('Hod:view_leave_application')
    

def approverq(request,id):
    data=tbl_leave.objects.get(id=id)
    data.status=1
    data.save()
    return redirect('Hod:view_leave_application')

def assign(request,id):
    sm=tbl_Semester.objects.all()
    dep=tbl_Department.objects.all()
    if request.method == "POST":
        sub = tbl_subject.objects.get(id=request.POST.get('sel_sub'))
        st_id=tbl_staff.objects.get(id=id)
        tbl_teachersubject.objects.create(staff=st_id,subject=sub)
        return redirect('Hod:staff')
    else:
        return render(request,'Hod/assign.html',{'sm':sm,'dep':dep})
    
def ajaxsubject(request):
    sem=tbl_Semester.objects.get(id=request.GET.get('sid'))
    dept=tbl_Department.objects.get(id=request.GET.get('did'))
    sub=tbl_subject.objects.filter(semester=sem,department=dept)
    return render(request,'Hod/ajaxsubject.html',{'sub':sub})