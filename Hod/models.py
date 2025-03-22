from django.db import models
from Admin.models import *
from Staff.models import *

class tbl_teachersubject(models.Model):
    staff=models.ForeignKey(tbl_staff,on_delete=models.CASCADE)
    subject=models.ForeignKey(tbl_subject,on_delete=models.CASCADE)