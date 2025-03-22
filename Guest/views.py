from django.shortcuts import render,redirect
from Admin.models import *
# Create your views here.

def Login(request):
    if request.method == "POST":
        email = request.POST.get('txt_email')
        password = request.POST.get('txt_pass')
        admincount=tbl_Admin.objects.filter(admin_email=email,admin_password=password).count()
        hodcount=tbl_hod.objects.filter(hod_email=email,hod_password=password).count()
        staffcount=tbl_staff.objects.filter(staff_email=email,staff_password=password).count()
        if admincount>0:
            admindata=tbl_Admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect('Admin:AdminDashboard')
        elif hodcount>0:
            hoddata=tbl_hod.objects.get(hod_email=email,hod_password=password)
            request.session['hid']=hoddata.id
            return redirect('Hod:HodDashboard')
        elif staffcount>0:
            staffdata=tbl_staff.objects.get(staff_email=email,staff_password=password)
            request.session['sid']=staffdata.id
            return redirect('Staff:StaffDashboard')
        else:
            return render(request,'Guest/Login.html',{'msg':"Invalid Email or Password"})
    else:
        return render(request,'Guest/Login.html')
    
def index(request):
    return render(request,'Guest/index.html')