from django.db import models

# Create your models here.
from stu_app.models import Student

class Schoolterm(models.Model):
    schooltermseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    termorder = models.IntegerField(null=True, blank=True)
    termstartdate = models.DateField(null=True, blank=True)
    termenddate = models.DateField(null=True, blank=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)
    termseq = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'schoolterm'
        managed ='false'


class Stuschedule(models.Model):
    schoolcycleseq = models.IntegerField(null=True, blank=True)
    schoolperiodsseq = models.IntegerField(null=True, blank=True)
    schooltermseq = models.ForeignKey(Schoolterm, null=True, db_column='schooltermseq', blank=True)
    studentid = models.ForeignKey(Student, db_column='studentid')
    scheduleseq = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'stuschedule'
        managed = 'false'
