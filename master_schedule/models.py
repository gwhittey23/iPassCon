from django.db import models

# Create your models here.


class Calendaryear(models.Model):
    calendaryearseq = models.IntegerField(primary_key=True)
    academicyear = models.CharField(max_length=16L)
    displayorder = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'calendaryear'
        managed = 'false'


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


class Gradelevel(models.Model):
    gradelevelseq = models.IntegerField(primary_key=True)
    gradelevel = models.CharField(max_length=8L, blank=True)
    gradeleveldescr = models.CharField(max_length=33L, blank=True)
    nextgradelevelseq = models.IntegerField(null=True, blank=True)
    curryog = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'gradelevel'
        managed = 'false'


class Hrsbio(models.Model):
    childrennumber = models.IntegerField(null=True, blank=True)
    empid = models.IntegerField()
    employmentstatus = models.CharField(max_length=8L, blank=True)
    personseq = models.ForeignKey('Person', db_column='personseq')
    militarycodeseq = models.IntegerField(null=True, blank=True)
    militarydischargedate = models.DateField(null=True, blank=True)
    militaryvet = models.IntegerField(null=True, blank=True)
    skillshobbies = models.CharField(max_length=5L, blank=True)
    spousename = models.CharField(max_length=23L, blank=True)
    spouseoccupation = models.CharField(max_length=12L, blank=True)
    tradeexperience = models.CharField(max_length=5L, blank=True)
    currentcareerseq = models.IntegerField(null=True, blank=True)
    i90form = models.IntegerField(null=True, blank=True)
    altempid = models.CharField(max_length=12L, blank=True, primary_key=True)
    altdeptid = models.CharField(max_length=5L, blank=True)
    altdeptseq = models.IntegerField(null=True, blank=True)
    workcompcode = models.CharField(max_length=5L, blank=True)
    corilastdate = models.DateField(null=True, blank=True)
    highestedustatus = models.CharField(max_length=15L, blank=True)
    profstatus = models.CharField(max_length=20L, blank=True)
    stateid = models.IntegerField(null=True, blank=True)
    licensenum = models.CharField(max_length=18L, blank=True)
    reporttodoe = models.IntegerField(null=True, blank=True)
    attendancetype = models.CharField(max_length=5L, blank=True)

    class Meta:
        db_table = 'hrsbio'
        managed = False


class Masterschoolschedule(models.Model):
    scheduleseq = models.IntegerField(primary_key=True)
    schoolcourseseq = models.ForeignKey('Schoolcourse', null=True, db_column='schoolcourseseq', blank=True)
    schoolcycleseq = models.IntegerField(null=True, blank=True)
    schoolperiodsseq = models.IntegerField(null=True, blank=True)
    schooltermseq = models.ForeignKey('Schoolterm', null=True, db_column='schooltermseq', blank=True)
    roomcatalogseq = models.IntegerField(null=True, blank=True)
    coursesectionseq = models.ForeignKey(Coursesection, null=True, db_column='coursesectionseq', blank=True)
    gradelevelseq = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.ForeignKey(Calendaryear, null=True, db_column='calendaryearseq', blank=True)
    schoolprofileseq = models.ForeignKey('Schoolprofile', null=True, db_column='schoolprofileseq', blank=True)
    filledcount = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'masterschoolschedule'
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


class Roomcatalog(models.Model):
    description = models.TextField(blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    schcounter = models.IntegerField(null=True, blank=True)
    usedashomeroom = models.IntegerField(null=True, blank=True)
    hrteacher = models.CharField(max_length=5L, blank=True)
    gradelevel = models.CharField(max_length=18L, blank=True)
    comment_field = models.CharField(max_length=31L, db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    roomcatalogseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    roomcode = models.CharField(max_length=18L, blank=True)
    buildingcodesseq = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'roomcatalog'
        managed = False


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
    credits = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)

    class Meta:
        db_table = 'schoolcoursedept'
        managed = 'false'


class Schoolcycle(models.Model):
    schoolcycleseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    daytitle = models.CharField(max_length=16L, blank=True)
    daytitleabbr = models.CharField(max_length=11L, blank=True)
    dayorder = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'schoolcycle'
        managed = 'false'


class Schoolperiods(models.Model):
    schoolperiodsseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    periodtitle = models.CharField(max_length=19L, blank=True)
    periodtitleabbr = models.CharField(max_length=7L, blank=True)
    periodorder = models.IntegerField(null=True, blank=True)
    starttime = models.IntegerField(null=True, blank=True)
    endtime = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'schoolperiods'
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
        managed = 'false'


class Teacher(models.Model):
    personseq = models.ForeignKey(Person, null=True, db_column='personseq', blank=True)
    initials = models.CharField(max_length=8L, blank=True)
    officephone = models.CharField(max_length=14L, blank=True)
    fulltime = models.IntegerField(null=True, blank=True)
    office = models.CharField(max_length=8L, blank=True)
    telephoneext = models.IntegerField(null=True, blank=True)
    printname = models.CharField(max_length=37L, blank=True)
    addressseq = models.IntegerField(null=True, blank=True)
    towncodesseq = models.IntegerField(null=True, blank=True)
    buildingcodesseq = models.IntegerField(null=True, blank=True)
    teacherseq = models.IntegerField(primary_key=True)
    homeroom = models.IntegerField(null=True, blank=True)
    teacherstatusseq = models.IntegerField(null=True, blank=True)
    departmentseq = models.IntegerField(null=True, blank=True)
    deletedflag = models.IntegerField(null=True, blank=True)
    consecutiveperiods = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'teacher'
        managed = 'false'


class Teachercourse(models.Model):
    teacherseq = models.ForeignKey(Teacher, db_column='teacherseq')
    calendaryearseq = models.ForeignKey(Calendaryear, db_column='calendaryearseq')
    schooltermseq = models.ForeignKey(Schoolterm, db_column='schooltermseq')
    schoolcourseseq = models.ForeignKey(Schoolcourse, db_column='schoolcourseseq')
    coursesectionseq = models.ForeignKey(Coursesection, db_column='coursesectionseq')

    class Meta:
        db_table = 'teachercourse'
        managed = 'false'


class Teacherschedule(models.Model):
    teacherseq = models.ForeignKey(Teacher, db_column='teacherseq',primary_key=True)
    scheduleseq = models.ForeignKey(Masterschoolschedule, db_column='scheduleseq')

    class Meta:
        db_table = 'teacherschedule'
        managed = 'false'


class Terms(models.Model):
    termseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.ForeignKey(Schoolprofile, null=True, db_column='schoolprofileseq', blank=True)
    termcode = models.CharField(max_length=7L, blank=True)
    termdescr = models.CharField(max_length=18L, blank=True)
    termabbr = models.CharField(max_length=7L, blank=True)

    class Meta:
        db_table = 'terms'
        managed = 'false'


class Pwrschmaster(models.Model):
    id = models.IntegerField(primary_key=True)
    course_number = models.CharField(max_length=6L, db_column='Course Number', blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    course_name = models.CharField(max_length=41L, db_column='Course Name', blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    section_number = models.CharField(max_length=8L, db_column='Section Number', blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    termid = models.IntegerField(null=True, db_column='TermID', blank=True) # Field name made lowercase.
    teacher_number = models.CharField(max_length=6L, db_column='Teacher Number', blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    teacher_name = models.CharField(max_length=22L, db_column='Teacher Name', blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    room = models.CharField(max_length=7L, db_column='Room', blank=True) # Field name made lowercase.
    expression = models.CharField(max_length=4L, db_column='Expression', blank=True) # Field name made lowercase.
    attendance_type_code = models.CharField(max_length=30L, db_column='Attendance_Type_Code', blank=True) # Field name made lowercase.
    att_mode_code = models.CharField(max_length=15L, db_column='Att_Mode_Code', blank=True) # Field name made lowercase.
    schoolid = models.IntegerField(null=True, db_column='SchoolID', blank=True) # Field name made lowercase.
    excludefromclassrank = models.IntegerField(null=True, db_column='ExcludeFromClassRank', blank=True) # Field name made lowercase.
    excludefromgpa = models.IntegerField(null=True, db_column='ExcludeFromGPA', blank=True) # Field name made lowercase.
    excludefromhonorroll = models.IntegerField(null=True, db_column='ExcludeFromHonorRoll', blank=True) # Field name made lowercase.
    excludefromstoredgrades = models.IntegerField(null=True, db_column='ExcludeFromStoredGrades', blank=True) # Field name made lowercase.
    maxenrollment = models.IntegerField(null=True, db_column='MaxEnrollment', blank=True) # Field name made lowercase.
    masterseq = models.IntegerField(null=True, db_column='MasterSEq', blank=True) # Field name made lowercase.
    day = models.CharField(max_length=1L, blank=True)
    period = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'Pwrschmaster'
