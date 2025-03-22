from django.db import models
from Admin.models import *
from Hod.models import *
# Create your models here.

class tbl_leave(models.Model):
    leave_date=models.DateField(auto_now_add=True)
    to_date=models.DateField()
    staff=models.ForeignKey(tbl_staff,on_delete=models.CASCADE)
    leave_reason=models.CharField(max_length=150)
    status=models.IntegerField(default=0)
