from django.db import models

# Create your models here.
from stu_app.models import Student

class Calendaryear(models.Model):
    calendaryearseq = models.IntegerField(primary_key=True)
    academicyear = models.CharField(max_length=16L)
    displayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'calendaryear'
        managed = 'false'


class Coursesection(models.Model):
    coursesectionseq = models.IntegerField(primary_key=True)
    schoolcourseseq = models.IntegerField(null=True, blank=True)
    coursesecdesc = models.CharField(max_length=19L, blank=True)
    maxseats = models.IntegerField(null=True, blank=True)
    filledcount = models.IntegerField(null=True, blank=True)
    techedweekseq = models.IntegerField(null=True, blank=True)
    linkedcoursesectionseq = models.IntegerField(null=True, blank=True)
    horzavgruleseq = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'coursesection'
        managed = 'false'


class Stutermcourse(models.Model):
    studentid = models.ForeignKey(Student, db_column='studentid')
    calendaryearseq = models.ForeignKey(Calendaryear, db_column='calendaryearseq')
    schooltermseq = models.ForeignKey(Schoolterm, db_column='schooltermseq')
    schoolcourseseq = models.ForeignKey(Schoolcourse, db_column='schoolcourseseq')
    coursesectionseq = models.ForeignKey(Coursesection, db_column='coursesectionseq')

    class Meta:
        db_table = 'stutermcourse'
        managed = 'false'


class Schoolcourse(models.Model):
    schoolcourseseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)
    courseseq = models.IntegerField(null=True, blank=True)
    honortypeseq = models.IntegerField(null=True, blank=True)
    coursetypeseq = models.IntegerField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    printclasslist = models.IntegerField(null=True, blank=True)
    horizontalavg = models.IntegerField(null=True, blank=True)
    verticalavg = models.IntegerField(null=True, blank=True)
    gparank = models.IntegerField(null=True, blank=True)
    failure = models.IntegerField(null=True, blank=True)
    verticalweight = models.IntegerField(null=True, blank=True)
    curriculumlevel = models.IntegerField(null=True, blank=True)
    majorminor = models.IntegerField(null=True, blank=True)
    acadtechedcycle = models.CharField(max_length=5L, blank=True)
    numberofrequests = models.IntegerField(null=True, blank=True)
    hasmeetingtime = models.IntegerField(null=True, blank=True)
    linkedschoolcourseseq = models.IntegerField(null=True, blank=True)
    printontranscript = models.IntegerField(null=True, blank=True)
    fromgradelevelseq = models.IntegerField(null=True, blank=True)
    togradelevelseq = models.IntegerField(null=True, blank=True)
    numofsections = models.IntegerField(null=True, blank=True)
    createuser = models.CharField(max_length=19L, blank=True)
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    updateuser = models.CharField(max_length=19L, blank=True)
    updatedate = models.DateField(null=True, blank=True)
    updatetime = models.IntegerField(null=True, blank=True)
    numofterms = models.IntegerField(null=True, blank=True)
    numberofrequestsalt = models.IntegerField(null=True, blank=True)
    maxseats = models.IntegerField(null=True, blank=True)
    canshare = models.IntegerField(null=True, blank=True)
    passfail = models.IntegerField(null=True, blank=True)
    numperiodspercycle = models.IntegerField(null=True, blank=True)
    usedbymsb = models.IntegerField(null=True, blank=True)
    sameperiod = models.IntegerField(null=True, blank=True)
    allowmultiplerooms = models.IntegerField(null=True, blank=True)
    additionalperiods = models.CharField(max_length=19L, blank=True)
    blockedperiods = models.CharField(max_length=5L, blank=True)
    msbrank = models.IntegerField(null=True, blank=True)
    consecutivetermsonly = models.IntegerField(null=True, blank=True)
    useextended = models.IntegerField(null=True, blank=True)
    ineligibilitytypeseq = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'schoolcourse'
        managed = 'false'


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


class Pwrschid(models.Model):
    pwrschoolid =models.IntegerField(null=True, blank=True)
    ipassid = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'pwrschid'
        managed = 'false'
