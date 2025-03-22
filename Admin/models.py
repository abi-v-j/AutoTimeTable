from django.db import models

class tbl_Department(models.Model):
    department_name = models.CharField(max_length=50)

class tbl_Semester(models.Model):
    semester_name = models.CharField(max_length=50)

class tbl_Academic_year(models.Model):
    Academic_year = models.CharField(max_length=50)

class tbl_Admin(models.Model):
    admin_name = models.CharField(max_length=50)
    admin_contact = models.CharField(max_length=50)
    admin_email = models.EmailField(max_length=50)
    admin_password = models.CharField(max_length=50)

class tbl_subject(models.Model):
    subject_name=models.CharField(max_length=50)
    department=models.ForeignKey(tbl_Department,on_delete=models.CASCADE)
    semester=models.ForeignKey(tbl_Semester,on_delete=models.CASCADE)

class tbl_staff(models.Model):
    staff_name=models.CharField(max_length=50)
    staff_email=models.EmailField(max_length=50)
    staff_contact=models.CharField(max_length=50)
    staff_password=models.CharField(max_length=50)
    department=models.ForeignKey(tbl_Department,on_delete=models.CASCADE)

class tbl_hod(models.Model):
    hod_name=models.CharField(max_length=50)
    hod_email=models.EmailField(max_length=50)
    hod_contact=models.CharField(max_length=50)
    hod_photo=models.FileField(upload_to='Assets/Hod/')
    hod_password=models.CharField(max_length=50)
    department=models.ForeignKey(tbl_Department,on_delete=models.CASCADE)







# In Admin/models.py
class tbl_timeslot(models.Model):
    day = models.CharField(max_length=10)  # e.g., "Monday"
    start_time = models.CharField(max_length=10)  # e.g., "09:00:00"
    end_time = models.CharField(max_length=10)    # e.g., "10:00:00"

class tbl_timetable(models.Model):
    department = models.ForeignKey(tbl_Department, on_delete=models.CASCADE)
    semester = models.ForeignKey(tbl_Semester, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(tbl_timeslot, on_delete=models.CASCADE)
    subject = models.ForeignKey(tbl_subject, on_delete=models.CASCADE)
    staff = models.ForeignKey(tbl_staff, on_delete=models.CASCADE)