from django.shortcuts import render,redirect
from Staff.models import *
# Create your views here.

def Staff(request):
    return render(request,'Staff/StaffDashboard.html')

def leave(request):
    lv=tbl_leave.objects.all()
    if request.method=="POST":
        st=tbl_staff.objects.get(id=request.session['sid'])
        reason=request.POST.get('txt_reason')
        date=request.POST.get('txt_date')
        stat=0
        ldate=request.POST.get('txt_leave_date')
        tbl_leave.objects.create(staff=st,leave_date=ldate,to_date=date,leave_reason=reason,status=stat)
        return redirect('Staff:leave')
    else:
        return render(request,'Staff/leave.html',{'leave':lv})

def deleterq(request,id):
    tbl_leave.objects.get(id=id).delete()
    return redirect('Staff:leave')