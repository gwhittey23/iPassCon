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


class Department(models.Model):
    departmentseq = models.IntegerField(primary_key=True)
    deptcode = models.CharField(max_length=44L, blank=True)
    deptdescr = models.CharField(max_length=51L, blank=True)

    class Meta:
        db_table = 'department'
        managed = 'false'


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


class Gradelevel(models.Model):
    gradelevelseq = models.IntegerField(primary_key=True)
    gradelevel = models.CharField(max_length=8L, blank=True)
    gradeleveldescr = models.CharField(max_length=33L, blank=True)
    nextgradelevelseq = models.IntegerField(null=True, blank=True)
    curryog = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'gradelevel'
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


class Person(models.Model):
    personseq = models.IntegerField(primary_key=True)
    lastname = models.CharField(max_length=55L)
    firstname = models.CharField(max_length=31L, blank=True)
    email = models.TextField(blank=True)
    middleinitial = models.CharField(max_length=23L, blank=True)
    persontitleseq = models.IntegerField(null=True, blank=True)
    imagefile = models.CharField(max_length=28L, blank=True)
    workplace = models.TextField(blank=True)
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    updatedate = models.DateField(null=True, blank=True)
    updatetime = models.IntegerField(null=True, blank=True)
    updateusersid = models.CharField(max_length=41L)
    createuser = models.CharField(max_length=21L, blank=True)
    personstatusseq = models.IntegerField(null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    maritalstatus = models.CharField(max_length=14L, blank=True)
    dateofbirth = models.DateField(null=True, blank=True)
    ssn = models.CharField(max_length=19L, blank=True)
    namesuffix = models.CharField(max_length=8L, blank=True)
    maidenname = models.CharField(max_length=25L, blank=True)
    persontypeseq = models.IntegerField(null=True, blank=True)
    corilastdate = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'person'
        managed = False

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.firstname + ' ' + self.lastname


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


class Schoolprofile(models.Model):
    schoolprofileseq = models.IntegerField(primary_key=True)
    lastpromotedyear = models.CharField(max_length=16L, blank=True)
    schoolcode = models.CharField(max_length=10L, blank=True)
    schooltype = models.CharField(max_length=6L, blank=True)
    schoolname = models.CharField(max_length=51L, blank=True)
    logoimagefilename = models.CharField(max_length=8L, blank=True)
    administrator = models.CharField(max_length=33L, blank=True)
    admintitle = models.CharField(max_length=38L, blank=True)
    dpsecretary = models.CharField(max_length=25L, blank=True)
    techdirector = models.CharField(max_length=23L, blank=True)
    guidancedir = models.CharField(max_length=24L, blank=True)
    guidancesec = models.CharField(max_length=21L, blank=True)
    technicalschool = models.IntegerField(null=True, blank=True)
    periodattendance = models.IntegerField(null=True, blank=True)
    startingid = models.IntegerField(null=True, blank=True)
    endingid = models.IntegerField(null=True, blank=True)
    website = models.CharField(max_length=49L, blank=True)
    datestamp = models.DateField(null=True, blank=True)
    phoneseq = models.IntegerField(null=True, blank=True)
    addressseq = models.IntegerField(null=True, blank=True)
    districtprofileseq = models.IntegerField(null=True, blank=True)
    cycletype = models.CharField(max_length=5L, blank=True)
    daysincycle = models.IntegerField(null=True, blank=True)
    numberofperiodsperday = models.IntegerField(null=True, blank=True)
    logoutpage = models.CharField(max_length=5L, blank=True)

    class Meta:
        db_table = 'schoolprofile'
        managed = 'false'


class Student(models.Model):
    gender = models.IntegerField(null=True, blank=True)
    dateofbirth = models.DateField(null=True, blank=True)
    gradelevel = models.CharField(max_length=8L, blank=True)
    studentid = models.IntegerField(primary_key=True)
    ssn = models.CharField(max_length=19L, blank=True)
    districtcode = models.CharField(max_length=5L, blank=True)
    birthcity = models.CharField(max_length=28L, blank=True)
    mailparentname = models.CharField(max_length=62L, blank=True)
    originalyog = models.IntegerField(null=True, blank=True)
    yog = models.IntegerField(null=True, blank=True)
    familycode = models.IntegerField(null=True, blank=True)
    deletedflag = models.IntegerField(null=True, blank=True)
    datestamp = models.DateField(null=True, blank=True)
    birthstate = models.CharField(max_length=8L, blank=True)
    namesuffix = models.CharField(max_length=10L, blank=True)
    birthcountrycode = models.CharField(max_length=54L, blank=True)
    sasid = models.CharField(max_length=20L, blank=True)
    lasid = models.CharField(max_length=11L, blank=True)
    preferredname = models.CharField(max_length=16L, blank=True)
    nextbus = models.CharField(max_length=5L, blank=True)
    buildingcode = models.CharField(max_length=5L, blank=True)
    immigrantseq = models.IntegerField(null=True, blank=True)
    migrantseq = models.IntegerField(null=True, blank=True)
    personseq = models.ForeignKey(Person, null=True, db_column='personseq', blank=True)
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    createuserid = models.CharField(max_length=5L, blank=True)
    updatedate = models.DateField(null=True, blank=True)
    updatetime = models.IntegerField(null=True, blank=True)
    updateuserid = models.CharField(max_length=20L, blank=True)
    homeroom = models.IntegerField(null=True, blank=True)
    towncodesseq = models.IntegerField(null=True, blank=True)
    counselor = models.IntegerField(null=True, blank=True)
    countryoforigin = models.IntegerField(null=True, blank=True)
    districtentrydate = models.DateField(null=True, blank=True)
    districtentryseq = models.IntegerField(null=True, blank=True)
    excluderank = models.IntegerField(null=True, blank=True)
    reporttodoe = models.IntegerField(null=True, blank=True)
    viceprincipal = models.IntegerField(null=True, blank=True)
    immigrantdate = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'student'
        managed = False

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.preferredname

class Transcript(models.Model):
    transcriptseq = models.IntegerField(primary_key=True)
    studentid = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)
    academicyear = models.CharField(max_length=16L, blank=True)
    coursename = models.CharField(max_length=45L, blank=True)
    curriculumlevel = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    schoolname = models.CharField(max_length=63L, blank=True)
    gradeseq = models.IntegerField(null=True, blank=True)
    gradecode = models.CharField(max_length=8L, blank=True)
    gradevalue = models.IntegerField(null=True, blank=True)
    coursesectionseq = models.IntegerField(null=True, blank=True)
    coursesecdesc = models.CharField(max_length=14L, blank=True)
    schoolcourseseq = models.IntegerField(null=True, blank=True)
    coursetitle = models.CharField(max_length=21L, blank=True)
    isfinalgrade = models.IntegerField(null=True, blank=True)
    gradelevelseq = models.IntegerField(null=True, blank=True)
    includeingpa = models.IntegerField(null=True, blank=True)
    transcriptterms = models.CharField(max_length=19L, blank=True)
    teachername = models.CharField(max_length=27L, blank=True)
    teacherseq = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'transcript'
        managed = 'false'


class Transcriptcredit(models.Model):
    transcriptseq = models.ForeignKey(Transcript, db_column='transcriptseq')
    departmentname = models.CharField(max_length=51L, blank=True, primary_key=True)
    departmentseq = models.ForeignKey(Department, null=True, db_column='departmentseq', blank=True)
    credits = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)
    studentid = models.ForeignKey(Student, null=True, db_column='studentid', blank=True)
    attemptedcredits = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)

    class Meta:
        db_table = 'transcriptcredit'
        managed = 'false'


class Transcriptqp(models.Model):
    transcriptqpseq = models.IntegerField(primary_key=True)
    transcriptseq = models.IntegerField(null=True, blank=True)
    scaleseq = models.IntegerField(null=True, blank=True)
    qualitypoints = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    includeincalc = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'transcriptqp'
        managed = 'false'
