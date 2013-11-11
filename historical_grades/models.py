from django.db import models

# Create your models here.

class Grade(models.Model):
    gradeseq = models.IntegerField(primary_key=True)
    gradecode = models.CharField(max_length=8L, blank=True)
    nummin = models.IntegerField(null=True, blank=True)
    nummax = models.IntegerField(null=True, blank=True)
    passfail = models.IntegerField(null=True, blank=True)
    credit = models.IntegerField(null=True, blank=True)
    calculationtypeseqhorizont = models.IntegerField(null=True, blank=True)
    calculationtypeseqvertical = models.IntegerField(null=True, blank=True)
    calculationtypeseqgpa = models.IntegerField(null=True, blank=True)
    unweighted = models.DecimalField(null=True, max_digits=10, decimal_places=1, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    show = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)
    calculationtypeseqhonorrol = models.IntegerField(null=True, blank=True)
    ineligibilitytypeseq = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'grade'
        managed = 'false'


class Gradeheading(models.Model):
    gradeheadingseq = models.IntegerField(primary_key=True)
    gradeheadingabbr = models.CharField(max_length=21L, blank=True)
    gradeheadingdescr = models.CharField(max_length=33L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    printonprogress = models.IntegerField(null=True, blank=True)
    printonreport = models.IntegerField(null=True, blank=True)
    isfinalgrade = models.IntegerField(null=True, blank=True)
    gradeparameterseq = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    istermgrade = models.IntegerField(null=True, blank=True)
    showgrade = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'gradeheading'
        managed = 'false'


class Gradeheadingterm(models.Model):
    gradeheadingtermseq = models.IntegerField(primary_key=True)
    schooltermseq = models.IntegerField(null=True, blank=True)
    gradeheadingseq = models.IntegerField(null=True, blank=True)
    openclosed = models.IntegerField(null=True, blank=True)
    gradeparameterseq = models.IntegerField(null=True, blank=True)
    displaygrades = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'gradeheadingterm'
        managed = 'false'


class Gradeparameter(models.Model):
    gradeparameterseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    numeffortcodes = models.IntegerField(null=True, blank=True)
    numconductcodes = models.IntegerField(null=True, blank=True)
    numcomments = models.IntegerField(null=True, blank=True)
    reportmessage = models.CharField(max_length=5L, blank=True)
    gradeparameterdescr = models.CharField(max_length=21L, blank=True)
    usecourseabsences = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'gradeparameter'
        managed = 'false'


class Gradescale(models.Model):
    gradescaleseq = models.IntegerField(primary_key=True)
    gradeseq = models.IntegerField(null=True, blank=True)
    curriculumnlevel = models.IntegerField(null=True, blank=True)
    gradescalevalue = models.DecimalField(null=True, max_digits=9, decimal_places=1, blank=True)
    scaleseq = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'gradescale'
        managed = 'false'


class Stugrades(models.Model):
    stugradesseq = models.IntegerField(primary_key=True)
    studentid = models.IntegerField(null=True, blank=True)
    gradeheadingseq = models.IntegerField(null=True, blank=True)
    schoolcourseseq = models.IntegerField(null=True, blank=True)
    gradeseq = models.IntegerField(null=True, blank=True)
    gradeheadingtermseq = models.IntegerField(null=True, blank=True)
    numcourseabsences = models.IntegerField(null=True, blank=True)
    coursesectionseq = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'stugrades'
        managed = 'false'
