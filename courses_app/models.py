from django.db import models


# Create your models here.

class Course(models.Model):
    courseseq = models.IntegerField(primary_key=True)
    coursename = models.TextField(blank=True)
    coursedescr = models.TextField(blank=True)
    coursetitle = models.CharField(max_length=14L, blank=True)
    createuser = models.CharField(max_length=8L, blank=True)
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    updateuser = models.CharField(max_length=5L, blank=True)
    updatedate = models.DateField(null=True, blank=True)
    updatetime = models.IntegerField(null=True, blank=True)
    shortname = models.TextField(blank=True)
    isonline = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'course'
        managed = 'false'


class Courseschooltype(models.Model):
    courseseq = models.IntegerField()
    schooltype = models.CharField(max_length=6L)

    class Meta:
        db_table = 'courseschooltype'
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


class Coursetype(models.Model):
    coursetypeseq = models.IntegerField(primary_key=True)
    coursetypedescr = models.CharField(max_length=18L, blank=True)
    isstudyhall = models.IntegerField(null=True, blank=True)
    islunch = models.IntegerField(null=True, blank=True)
    isepims = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'coursetype'
        managed = 'false'


class Department(models.Model):
    departmentseq = models.IntegerField(primary_key=True)
    deptcode = models.CharField(max_length=44L, blank=True)
    deptdescr = models.CharField(max_length=51L, blank=True)

    class Meta:
        db_table = 'department'
        managed = 'false'


class Scale(models.Model):
    scaleseq = models.IntegerField(primary_key=True)
    scalecode = models.CharField(max_length=10L, blank=True)
    scaledescr = models.CharField(max_length=36L, blank=True)

    class Meta:
        db_table = 'scale'
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


class Schoolcoursedept(models.Model):
    departmentseq = models.ForeignKey(Department, db_column='departmentseq')
    schoolcourseseq = models.ForeignKey(Schoolcourse, db_column='schoolcourseseq')
    credits = models.DecimalField(primary_key=True, max_digits=10, decimal_places=2, blank=True)

    class Meta:
        db_table = 'schoolcoursedept'
        managed = 'false'


class Schoolcourseprereq(models.Model):
    schoolcourseseq = models.ForeignKey(Schoolcourse, db_column='schoolcourseseq')
    prereqschoolcourseseq = models.IntegerField()

    class Meta:
        db_table = 'schoolcourseprereq'
        managed = 'false'


class Schoolcoursescale(models.Model):
    schoolcourseseq = models.IntegerField(primary_key=True)
    scaleseq = models.ForeignKey(Scale, db_column='scaleseq')
    includeincalc = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'schoolcoursescale'
        managed = 'false'

