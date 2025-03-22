from django.shortcuts import render,redirect
from Admin.models import *
from Hod.models import *
from datetime import datetime, timedelta
from random import choice, shuffle



def Dashboard(request):
    return render(request,'Admin/Dashboard.html')

def Department(request):
    dep=tbl_Department.objects.all()
    if request.method == "POST":
        depname = request.POST.get('txt_department')
        tbl_Department.objects.create(department_name=depname)
        return render(request,'Admin/Department.html',{'department':dep})
    else:
        return render(request,'Admin/Department.html',{'department':dep})

def deletedepartment(request,id):
    tbl_Department.objects.get(id=id).delete()
    return redirect('Admin:Department')
  
def Semester(request):
    sem=tbl_Semester.objects.all()
    if request.method == "POST":
        semnum = request.POST.get('txt_semester')
        tbl_Semester.objects.create(semester_name=semnum)
        return render(request,'Admin/Semester.html',{'semester':sem})
    else:
        return render(request,'Admin/Semester.html',{'semester':sem})

def deletesemester(request,id):
    tbl_Semester.objects.get(id=id).delete()
    return redirect('Admin:Semester')

def Academic_year(request):
    acy=tbl_Academic_year.objects.all()
    if request.method == "POST":
        acyear = request.POST.get('txt_year')
        tbl_Academic_year.objects.create(Academic_year=acyear)
        return render(request,'Admin/Academic_year.html',{'year':acy})
    else:
        return render(request,'Admin/Academic_year.html',{'year':acy})

def deleteacyear(request,id):
    tbl_Academic_year.objects.get(id=id).delete()
    return redirect('Admin:Academic_year')

def AdminRegistration(request):
    ar=tbl_Admin.objects.all()
    if request.method == "POST":
        adname = request.POST.get('txt_name')
        adcontact = request.POST.get('txt_cont')
        ademail = request.POST.get('txt_email')
        adpass = request.POST.get('txt_pass')
        tbl_Admin.objects.create(admin_name=adname,admin_contact=adcontact,admin_email=ademail,admin_password=adpass)
        return render(request,'Admin/AdminRegistration.html',{'admin':ar})
    else:
        return render(request,'Admin/AdminRegistration.html',{'admin':ar})

def deleteadmr(request,id):
    tbl_Admin.objects.get(id=id).delete()
    return redirect('Admin:AdminRegistration')

def editadmr(request,id):
    ab=tbl_Admin.objects.all()
    data=tbl_Admin.objects.get(id=id)
    if request.method == "POST":
        temp_name = request.POST.get('txt_name')
        temp_contact = request.POST.get('txt_cont')
        temp_email = request.POST.get('txt_email')
        temp_password = request.POST.get('txt_pass')
        data.admin_name = temp_name
        data.admin_contact = temp_contact
        data.admin_email = temp_email
        data.admin_password = temp_password
        data.save()
        return redirect('Admin:AdminRegistration')
    else:
        return render(request,'Admin/AdminRegistration.html',{'data':data,'admin':ab})
    
def editdep(request,id):
    dep=tbl_Department.objects.all()
    data=tbl_Department.objects.get(id=id)
    if request.method == "POST":
        temp_dep = request.POST.get('txt_department')
        data.department_name = temp_dep
        data.save()
        return redirect('Admin:Department')
    else:
        return render(request,'Admin/Department.html',{'data':data,'department':dep})

def Subject(request):
    dep=tbl_Department.objects.all()
    sem=tbl_Semester.objects.all()
    if request.method == "POST":
        dept = tbl_Department.objects.get(id=request.POST.get('sel_dept'))
        sem = tbl_Semester.objects.get(id=request.POST.get('sel_sem'))
        sub = request.POST.get('txt_subject')
        tbl_subject.objects.create(subject_name=sub,department=dept,semester=sem)
        return redirect('Admin:Subject')
    else:
        return render(request,'Admin/Subject.html',{'dep':dep,"sem":sem})

    
def HOD(request):
    dep=tbl_Department.objects.all()
    data = tbl_hod.objects.all()
    if request.method == "POST":
        dept = tbl_Department.objects.get(id=request.POST.get('sel_dept'))
        name=request.POST.get('txt_name')
        photo=request.FILES.get('txt_photo')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        password=request.POST.get('txt_password')
        tbl_hod.objects.create(hod_name=name,hod_email=email,hod_contact=contact,hod_photo=photo,hod_password=password,department=dept)
        return redirect('Admin:HOD')
    else:
        return render(request,'Admin/HOD.html',{'dep':dep,'data': data})
    
def deletehod(request,id):
    tbl_hod.objects.get(id=id).delete()
    return redirect('Admin:HOD')

def edithod(request, id):
    dep = tbl_Department.objects.all()
    data=tbl_hod.objects.all()
    edit_data = tbl_hod.objects.get(id=id)
    if request.method == "POST":
        dept = tbl_Department.objects.get(id=request.POST.get('sel_dept'))
        name = request.POST.get('txt_name')
        photo = request.FILES.get('file_photo')
        email = request.POST.get('txt_email')
        contact = request.POST.get('txt_contact')
        password = request.POST.get('txt_password')
        edit_data.hod_name = name
        edit_data.hod_email = email
        edit_data.hod_contact = contact
        if photo: 
            edit_data.hod_photo = photo
        edit_data.hod_password = password
        edit_data.department = dept
        edit_data.save()
        return redirect('Admin:HOD')
    else:
        return render(request, 'Admin/HOD.html', {'edit_data': edit_data, 'dep': dep,'data': data})
    

def generate_timetable(request):
    if request.method == "POST":
        # Clear existing timetable and timeslots
        tbl_timetable.objects.all().delete()
        tbl_timeslot.objects.all().delete()

        # Define days and time slots
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        time_slots = [
            ("9:00", "10:00"),
            ("10:00", "11:00"),
            ("11:00", "12:00"),
            ("12:00", "1:00"),
        ]

        # Create time slots with the correct format
        for day in days:
            for start, end in time_slots:
                tbl_timeslot.objects.create(day=day, start_time=start, end_time=end)
        timeslots = tbl_timeslot.objects.all()
        print(f"Timeslots created: {timeslots.count()}")
        for timeslot in timeslots:
            print(f"Timeslot: {timeslot.day}, {timeslot.start_time}-{timeslot.end_time}")

        # Rest of the function remains the same
        departments = tbl_Department.objects.all()
        semesters = tbl_Semester.objects.all()
        print(f"Departments: {departments.count()}, Semesters: {semesters.count()}")

        today = datetime.now().date()
        week_end = today + timedelta(days=6)
        leaves = tbl_leave.objects.filter(leave_date__lte=week_end, to_date__gte=today, status=1)
        print(f"Leaves: {leaves.count()}")

        for department in departments:
            for semester in semesters:
                subjects = tbl_subject.objects.filter(department=department, semester=semester)
                print(f"Department: {department.department_name} (ID: {department.id}), Semester: {semester.semester_name} (ID: {semester.id}), Subjects: {subjects.count()}")

                if not subjects.exists():
                    print(f"No subjects found for {department.department_name} - {semester.semester_name}, skipping...")
                    continue

                for timeslot in timeslots:
                    if tbl_timetable.objects.filter(department=department, semester=semester, timeslot=timeslot).exists():
                        print(f"Slot {timeslot} already assigned for {department.department_name} - {semester.semester_name}, skipping...")
                        continue

                    subject = choice(list(subjects))
                    teachers = tbl_teachersubject.objects.filter(subject=subject).select_related('staff')
                    print(f"Timeslot: {timeslot}, Subject: {subject.subject_name} (ID: {subject.id}), Teachers: {teachers.count()}")

                    available_teachers = []
                    for teacher in teachers:
                        if not tbl_timetable.objects.filter(staff=teacher.staff, timeslot=timeslot, department=department).exists():
                            available_teachers.append(teacher.staff)
                        else:
                            print(f"Teacher {teacher.staff.staff_name} already assigned in {timeslot} for {department.department_name}")

                    print(f"Available Teachers: {len(available_teachers)}")

                    if not available_teachers:
                        print(f"No available teachers for {subject.subject_name} in {timeslot}, skipping...")
                        continue

                    absent_teachers = leaves.filter(staff__in=available_teachers)
                    selected_teacher = None
                    for teacher in available_teachers:
                        if teacher not in [leave.staff for leave in absent_teachers]:
                            selected_teacher = teacher
                            break

                    if not selected_teacher:
                        free_teachers = tbl_staff.objects.exclude(
                            id__in=tbl_timetable.objects.filter(timeslot=timeslot).values_list('staff', flat=True)
                        ).filter(department=department)
                        print(f"Free Teachers: {free_teachers.count()}")
                        if free_teachers.exists():
                            selected_teacher = choice(list(free_teachers))

                    if selected_teacher:
                        tbl_timetable.objects.create(
                            department=department,
                            semester=semester,
                            timeslot=timeslot,
                            subject=subject,
                            staff=selected_teacher
                        )
                        print(f"Assigned: {subject.subject_name} to {selected_teacher.staff_name} in {timeslot} for {department.department_name} - {semester.semester_name}")
                    else:
                        print(f"No teacher selected for {subject.subject_name} in {timeslot}, skipping...")

        return redirect('Admin:view_timetable')
    return render(request, 'Admin/GenerateTimetable.html')





# def generate_timetable(request):
#     if request.method == "POST":
#         # Clear existing timetable and timeslots
#         tbl_timetable.objects.all().delete()
#         tbl_timeslot.objects.all().delete()

#         # Define days and time slots
#         days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#         time_slots = [
#             ("9:00", "10:00"),
#             ("10:00", "11:00"),
#             ("11:00", "12:00"),
#             ("12:00", "1:00"),
#         ]

#         # Create time slots
#         for day in days:
#             for start, end in time_slots:
#                 tbl_timeslot.objects.create(day=day, start_time=start, end_time=end)
#         timeslots = tbl_timeslot.objects.all()
#         print(f"Timeslots created: {timeslots.count()}")

#         departments = tbl_Department.objects.all()
#         semesters = tbl_Semester.objects.all()
#         today = datetime.now().date()
#         week_end = today + timedelta(days=6)
#         leaves = tbl_leave.objects.filter(leave_date__lte=week_end, to_date__gte=today, status=1)

#         for department in departments:
#             for semester in semesters:
#                 subjects = list(tbl_subject.objects.filter(department=department, semester=semester))
#                 print(f"Department: {department.department_name} (ID: {department.id}), Semester: {semester.semester_name} (ID: {semester.id}), Subjects: {len(subjects)}")
#                 if not subjects:
#                     print(f"No subjects found for {department.department_name} - {semester.semester_name}, skipping...")
#                     continue

#                 for timeslot in timeslots:
#                     if tbl_timetable.objects.filter(department=department, semester=semester, timeslot=timeslot).exists():
#                         print(f"Slot {timeslot} already assigned for {department.department_name} - {semester.semester_name}, skipping...")
#                         continue

#                     # Shuffle subjects to try different ones
#                     shuffle(subjects)
#                     selected_subject = None
#                     selected_teacher = None

#                     for subject in subjects:
#                         teachers = tbl_teachersubject.objects.filter(subject=subject).select_related('staff')
#                         available_teachers = []
#                         for teacher in teachers:
#                             if not tbl_timetable.objects.filter(staff=teacher.staff, timeslot=timeslot).exists():
#                                 available_teachers.append(teacher.staff)
#                             else:
#                                 print(f"Teacher {teacher.staff.staff_name} already assigned in {timeslot} for {department.department_name}")

#                         if not available_teachers:
#                             print(f"No available teachers for {subject.subject_name} in {timeslot}, trying another subject...")
#                             continue

#                         absent_teachers = leaves.filter(staff__in=available_teachers)
#                         for teacher in available_teachers:
#                             if teacher not in [leave.staff for leave in absent_teachers]:
#                                 selected_teacher = teacher
#                                 selected_subject = subject
#                                 break

#                         if selected_teacher:
#                             break

#                     if not selected_teacher:
#                         free_teachers = tbl_staff.objects.exclude(
#                             id__in=tbl_timetable.objects.filter(timeslot=timeslot).values_list('staff', flat=True)
#                         ).filter(department=department)
#                         if free_teachers.exists():
#                             selected_teacher = choice(list(free_teachers))
#                             selected_subject = choice(subjects)

#                     if selected_teacher and selected_subject:
#                         tbl_timetable.objects.create(
#                             department=department,
#                             semester=semester,
#                             timeslot=timeslot,
#                             subject=selected_subject,
#                             staff=selected_teacher
#                         )
#                         print(f"Assigned: {selected_subject.subject_name} to {selected_teacher.staff_name} in {timeslot} for {department.department_name} - {semester.semester_name}")
#                     else:
#                         print(f"No teacher or subject selected for {timeslot} in {department.department_name} - {semester.semester_name}, leaving slot empty...")

#         return redirect('Admin:view_timetable')
#     return render(request, 'Admin/GenerateTimetable.html')


def view_timetable(request):
    timetable = tbl_timetable.objects.all()
    departments = tbl_Department.objects.all()
    semesters = tbl_Semester.objects.all().order_by('id')
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    time_slots = [
        {"start": "9:00", "end": "10:00"},
        {"start": "10:00", "end": "11:00"},
        {"start": "11:00", "end": "12:00"},
        {"start": "12:00", "end": "1:00"},
    ]
    print(f"Timetable Entries: {timetable.count()}")
    for entry in timetable:
        print(f"Entry: Dept {entry.department.department_name} (ID: {entry.department.id}), Sem {entry.semester.semester_name} (ID: {entry.semester.id}), Day {entry.timeslot.day}, Time {entry.timeslot.start_time}-{entry.timeslot.end_time}, Subject {entry.subject.subject_name}, Staff {entry.staff.staff_name}")
    print("Semesters passed to template:")
    for semester in semesters:
        print(f" - {semester.semester_name} (ID: {semester.id})")
    return render(request, 'Admin/ViewTimetable.html', {
        'timetable': timetable,
        'departments': departments,
        'semesters': semesters,
        'days': days,
        'time_slots': time_slots
    })