# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Achievementtype(models.Model):
    achievementtypeseq = models.IntegerField(primary_key=True)
    achievementcode = models.CharField(max_length=12L, blank=True)
    achievementdescr = models.TextField(blank=True)
    organizationname = models.CharField(max_length=5L, blank=True)
    organizationseq = models.IntegerField(null=True, blank=True)
    achievementlevel = models.CharField(max_length=18L, blank=True)
    class Meta:
        db_table = 'achievementtype'

class Action(models.Model):
    actionseq = models.IntegerField(primary_key=True)
    actioncode = models.CharField(max_length=8L, blank=True)
    actiondescr = models.TextField(blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    categoryseq = models.IntegerField(null=True, blank=True)
    procintervcategory = models.CharField(max_length=6L, blank=True)
    class Meta:
        db_table = 'action'

class Actioncategory(models.Model):
    code = models.CharField(max_length=16L, blank=True)
    descr = models.TextField(blank=True)
    actioncategoryseq = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'actioncategory'

class Activity(models.Model):
    activitydescr = models.TextField(blank=True)
    activityenddate = models.DateField(null=True, blank=True)
    activityhtmldescr = models.CharField(max_length=5L, blank=True)
    activitypublic = models.IntegerField(null=True, blank=True)
    activityseq = models.IntegerField(primary_key=True)
    activityshortname = models.TextField(blank=True)
    activitystartdate = models.DateField(null=True, blank=True)
    athleticeligibility = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    showontranscript = models.IntegerField(null=True, blank=True)
    activitygroup = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'activity'

#class Activityleader(models.Model):
#    activitystatusseq = models.ForeignKey('Activitystatus', null=True, db_column='activitystatusseq', blank=True)
#    activityseq = models.IntegerField(null=True, blank=True)
#    personseq = models.ForeignKey('Person', null=True, db_column='personseq', blank=True)
#    activityleaderseq = models.IntegerField(primary_key=True)
#    class Meta:
#        db_table = 'activityleader'

class Activitymisc(models.Model):
    activitymiscseq = models.IntegerField(primary_key=True)
    activitymiscdescr = models.CharField(max_length=19L, blank=True)
    class Meta:
        db_table = 'activitymisc'

class Activitymiscfield(models.Model):
    activitymiscfieldseq = models.IntegerField(primary_key=True)
    activitymiscseq = models.IntegerField(null=True, blank=True)
    activitymisclabel = models.CharField(max_length=10L, blank=True)
    activitymiscdatatype = models.CharField(max_length=23L, blank=True)
    activitymiscselectvalues = models.CharField(max_length=10L, blank=True)
    activitymiscdisplayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'activitymiscfield'

class Activitymiscx(models.Model):
    activitymiscseq = models.ForeignKey(Activitymisc, null=True, db_column='activitymiscseq', blank=True)
    activitymiscdisplayorder = models.IntegerField()
    activityseq = models.ForeignKey(Activity, db_column='activityseq')
    class Meta:
        db_table = 'activitymiscx'

class Activityposition(models.Model):
    activitypositionseq = models.IntegerField(primary_key=True)
    activitypositionname = models.CharField(max_length=24L, blank=True)
    activitypositiondescr = models.CharField(max_length=24L, blank=True)
    adultstudent = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'activityposition'

class Activitypositionx(models.Model):
    activityseq = models.ForeignKey(Activity, db_column='activityseq')
    activitypositionseq = models.ForeignKey(Activityposition, null=True, db_column='activitypositionseq', blank=True)
    activitypositiondisplayord = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'activitypositionx'

class Activitystatus(models.Model):
    activitystatusseq = models.IntegerField(primary_key=True)
    activitystatusdescr = models.CharField(max_length=40L, blank=True)
    class Meta:
        db_table = 'activitystatus'


class Adminaction(models.Model):
    adminactionseq = models.IntegerField(primary_key=True)
    adminactioncode = models.CharField(max_length=8L, blank=True)
    adminactiondescr = models.CharField(max_length=38L, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'adminaction'

class Alert(models.Model):
    studentid = models.IntegerField()
    comment_field = models.TextField(db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    alerttypeseq = models.ForeignKey('Alerttype', null=True, db_column='alerttypeseq', blank=True)
    alertseq = models.IntegerField(primary_key=True)
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    createuserid = models.CharField(max_length=18L, blank=True)
    expirationdate = models.DateField(null=True, blank=True)
    active = models.IntegerField(null=True, blank=True)
    deactiveuser = models.CharField(max_length=19L, blank=True)
    deactivedate = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'alert'

class Alerttype(models.Model):
    alerttypeseq = models.IntegerField(primary_key=True)
    alerttitle = models.CharField(max_length=53L, blank=True)
    alertdescr = models.CharField(max_length=58L, blank=True)
    alertcomment = models.CharField(max_length=42L, blank=True)
    image_field = models.CharField(max_length=5L, db_column='image_', blank=True) # Field renamed because it ended with '_'.
    class Meta:
        db_table = 'alerttype'

class Alertusertype(models.Model):
    alerttypeseq = models.ForeignKey(Alerttype, db_column='alerttypeseq')
    usertypeseq = models.ForeignKey('Usertype', db_column='usertypeseq')
    canview = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'alertusertype'

class Allergy(models.Model):
    allergyseq = models.IntegerField(primary_key=True)
    allergycode = models.CharField(max_length=11L, blank=True)
    allergydescr = models.CharField(max_length=36L, blank=True)
    lifethreatening = models.IntegerField(null=True, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    treatment = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'allergy'

class Alumni(models.Model):
    studentid = models.IntegerField()
    stillindistrict = models.IntegerField(null=True, blank=True)
    kidsindistrict = models.IntegerField(null=True, blank=True)
    volunteer = models.IntegerField(null=True, blank=True)
    contributor = models.IntegerField(null=True, blank=True)
    lastdate = models.DateField(null=True, blank=True)
    contribution = models.CharField(max_length=5L, blank=True)
    postgraduateplansseq = models.ForeignKey('Postgraduateplans', null=True, db_column='postgraduateplansseq', blank=True)
    hourlysalary = models.IntegerField(null=True, blank=True)
    workfield = models.CharField(max_length=5L, blank=True)
    major = models.CharField(max_length=5L, blank=True)
    sameastrain = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'alumni'

class Assignment(models.Model):
    assignmentseq = models.IntegerField(primary_key=True)
    assigneddate = models.DateField(null=True, blank=True)
    duedate = models.DateField(null=True, blank=True)
    assignmenttypeseq = models.IntegerField(null=True, blank=True)
    assignmenttitle = models.TextField(blank=True)
    assignmentdescr = models.TextField(blank=True)
    createdate = models.DateField(null=True, blank=True)
    modifieddate = models.DateField(null=True, blank=True)
    teacherseq = models.IntegerField(null=True, blank=True)
    possiblepoints = models.IntegerField(null=True, blank=True)
    order_field = models.IntegerField(null=True, db_column='order_', blank=True) # Field renamed because it ended with '_'.
    coursesectionseq = models.IntegerField(null=True, blank=True)
    assignmentavg = models.DecimalField(null=True, max_digits=13, decimal_places=2, blank=True)
    ishomework = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    weblinks = models.CharField(max_length=5L, blank=True)
    schooltermseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'assignment'

class Assignmentgrade(models.Model):
    assignmentgradeseq = models.IntegerField(primary_key=True)
    assignmentgradecode = models.CharField(max_length=18L, blank=True)
    coursesectionseq = models.IntegerField(null=True, blank=True)
    teacherseq = models.IntegerField(null=True, blank=True)
    unweighted = models.DecimalField(null=True, max_digits=13, decimal_places=2, blank=True)
    nummin = models.IntegerField(null=True, blank=True)
    nummax = models.IntegerField(null=True, blank=True)
    calculationtypeseqhorizont = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'assignmentgrade'

class Assignmenttype(models.Model):
    assignmenttypeseq = models.IntegerField(primary_key=True)
    assignmenttypedescr = models.TextField(blank=True)
    teacherseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'assignmenttype'

class Assigntypesecweight(models.Model):
    schooltermseq = models.IntegerField()
    coursesectionseq = models.IntegerField()
    weight = models.DecimalField(null=True, max_digits=12, decimal_places=1, blank=True)
    assignmenttypeseq = models.IntegerField()
    teacherseq = models.ForeignKey('Teacher', null=True, db_column='teacherseq', blank=True)
    extracredit = models.IntegerField(null=True, blank=True)
    numofdropgrade = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'assigntypesecweight'

class Attendance(models.Model):
    calendaryearseq = models.IntegerField(null=True, blank=True)
    createusersid = models.CharField(max_length=24L, blank=True)
    studentid = models.ForeignKey('Student', db_column='studentid')
    attendancecodeseq = models.IntegerField(null=True, blank=True)
    attendancedate = models.DateField(null=True, blank=True)
    guardiannote = models.TextField(blank=True)
    createdate = models.DateField(null=True, blank=True)
    timein = models.IntegerField(null=True, blank=True)
    timeout = models.IntegerField(null=True, blank=True)
    attendanceseq = models.IntegerField(primary_key=True)
    timereturn = models.IntegerField(null=True, blank=True)
    schoolperiodsseq = models.IntegerField(null=True, blank=True)
    timeleft = models.IntegerField(null=True, blank=True)
    coursesectionseq = models.IntegerField(null=True, blank=True)
    studisciplineseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'attendance'

class Attendancecodes(models.Model):
    attendancecodeseq = models.IntegerField()
    attcode = models.CharField(max_length=27L, blank=True)
    attdescr = models.CharField(max_length=51L, blank=True)
    attendancetypeseq = models.IntegerField(null=True, blank=True)
    presentabsent = models.IntegerField(null=True, blank=True)
    excusedunexcused = models.IntegerField(null=True, blank=True)
    perfectatt = models.IntegerField(null=True, blank=True)
    timeinputrequired = models.IntegerField(null=True, blank=True)
    dailyperiod = models.IntegerField(null=True, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    dailytoperiodseq = models.IntegerField(null=True, blank=True)
    periodtodailyseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'attendancecodes'

class Attendancecomplete(models.Model):
    calendaryearseq = models.IntegerField(null=True, blank=True)
    teacherseq = models.IntegerField(null=True, blank=True)
    attendancedate = models.DateField(null=True, blank=True)
    createdate = models.DateField(null=True, blank=True)
    schoolperiodsseq = models.IntegerField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    createuserid = models.CharField(max_length=24L, blank=True)
    updatedate = models.DateField(null=True, blank=True)
    updatetime = models.IntegerField(null=True, blank=True)
    updateuserid = models.CharField(max_length=24L, blank=True)
    comment_field = models.CharField(max_length=5L, db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    completed = models.IntegerField(null=True, blank=True)
    attendancecompleteseq = models.IntegerField(primary_key=True)
    schoolcourseseq = models.IntegerField(null=True, blank=True)
    coursesectionseq = models.IntegerField(null=True, blank=True)
    roomcatalogseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'attendancecomplete'

class Attendanceconfig(models.Model):
    attendanceconfigseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    absentmode = models.CharField(max_length=15L, blank=True)
    periodsabsent = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)
    attendancecodeseq = models.IntegerField(null=True, blank=True)
    absentcomment = models.CharField(max_length=5L, blank=True)
    periodorder = models.IntegerField(null=True, blank=True)
    periodmode = models.CharField(max_length=31L, blank=True)
    class Meta:
        db_table = 'attendanceconfig'

class Attendancetypes(models.Model):
    attendancetypeseq = models.IntegerField()
    attendancetypedescr = models.CharField(max_length=36L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'attendancetypes'

class Auditdetail(models.Model):
    auditseq = models.IntegerField()
    lineno_field = models.IntegerField(db_column='lineno_') # Field renamed because it ended with '_'.
    group1 = models.CharField(max_length=16L, blank=True)
    group2 = models.CharField(max_length=20L, blank=True)
    group3 = models.CharField(max_length=5L, blank=True)
    auditlinedescr = models.TextField(blank=True)
    auditdata = models.CharField(max_length=28L, blank=True)
    auditdelimiter = models.CharField(max_length=6L, blank=True)
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'auditdetail'

class Batchcheck(models.Model):
    batchcheckdate = models.DateField()
    class Meta:
        db_table = 'batchcheck'

class Bilingualedstatus(models.Model):
    bilingualedstatuscode = models.CharField(max_length=7L, blank=True)
    description = models.TextField(blank=True)
    stateabbr = models.CharField(max_length=7L, blank=True)
    bilingualedstatusseq = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'bilingualedstatus'

class Buildingcodes(models.Model):
    buildingcode = models.CharField(max_length=10L, blank=True)
    description = models.CharField(max_length=24L, blank=True)
    buildingcodesseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'buildingcodes'

class Bus(models.Model):
    busseq = models.IntegerField(primary_key=True)
    busno = models.IntegerField(null=True, blank=True)
    driver = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'bus'

class Busroute(models.Model):
    busrouteseq = models.IntegerField(primary_key=True)
    busrouteid = models.CharField(max_length=15L, blank=True)
    busroutetypeseq = models.IntegerField(null=True, blank=True)
    starttime = models.IntegerField(null=True, blank=True)
    endtime = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'busroute'

class Busroutebusx(models.Model):
    busrouteseq = models.ForeignKey(Busroute, db_column='busrouteseq')
    busseq = models.ForeignKey(Bus, db_column='busseq')
    dayofweek = models.IntegerField()
    class Meta:
        db_table = 'busroutebusx'

class Busroutetype(models.Model):
    busroutetypeseq = models.IntegerField(primary_key=True)
    busroutetypename = models.CharField(max_length=23L, blank=True)
    class Meta:
        db_table = 'busroutetype'

class Busstop(models.Model):
    busstopseq = models.IntegerField(primary_key=True)
    busstopno = models.CharField(max_length=8L, blank=True)
    intersection = models.CharField(max_length=54L, blank=True)
    class Meta:
        db_table = 'busstop'

class Calculationtypes(models.Model):
    calculationtypesseq = models.IntegerField(primary_key=True)
    calculationtypesabbr = models.CharField(max_length=6L, blank=True)
    calculationtypesdescr = models.TextField(blank=True)
    class Meta:
        db_table = 'calculationtypes'

class Calendar(models.Model):
    schoolprofileseq = models.ForeignKey('Schoolprofile', db_column='schoolprofileseq')
    caldate = models.DateField()
    daynumber = models.IntegerField(null=True, blank=True)
    datestamp = models.DateField(null=True, blank=True)
    timestamp = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.ForeignKey('Calendaryear', null=True, db_column='calendaryearseq', blank=True)
    techedweekseq = models.IntegerField(null=True, blank=True)
    schoolcycleseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'calendar'

class Calendaryear(models.Model):
    calendaryearseq = models.IntegerField(primary_key=True)
    academicyear = models.CharField(max_length=16L)
    displayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'calendaryear'

class Careertechtype(models.Model):
    careertechtypeseq = models.IntegerField(primary_key=True)
    careertechtypecode = models.CharField(max_length=24L, blank=True)
    careertechtypedescr = models.TextField(blank=True)
    statecode = models.CharField(max_length=7L, blank=True)
    class Meta:
        db_table = 'careertechtype'

class College(models.Model):
    collegeseq = models.IntegerField(primary_key=True)
    collegecode = models.CharField(max_length=10L, blank=True)
    collegename = models.TextField(blank=True)
    personseq = models.IntegerField(null=True, blank=True)
    addressseq = models.IntegerField(null=True, blank=True)
    foreign_field = models.IntegerField(null=True, db_column='foreign_', blank=True) # Field renamed because it ended with '_'.
    updatedate = models.DateField(null=True, blank=True)
    updatecode = models.CharField(max_length=5L, blank=True)
    programyear = models.CharField(max_length=6L, blank=True)
    inststatus = models.CharField(max_length=5L, blank=True)
    phoneseq = models.IntegerField(null=True, blank=True)
    postgraduateplansseq = models.IntegerField(null=True, blank=True)
    ranking = models.CharField(max_length=5L, blank=True)
    shortname = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'college'

class Collegeappltype(models.Model):
    appltypeseq = models.IntegerField(null=True, blank=True)
    appltypecode = models.CharField(max_length=7L)
    appltypedescr = models.CharField(max_length=23L, blank=True)
    class Meta:
        db_table = 'collegeappltype'

class Comments(models.Model):
    commentsseq = models.IntegerField(primary_key=True)
    commentcode = models.CharField(max_length=8L, blank=True)
    commentdescr = models.TextField(blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    calculationtypesseq = models.IntegerField(null=True, blank=True)
    ineligibilitycalctypesseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'comments'

class Conductcodes(models.Model):
    conductcodesseq = models.IntegerField(primary_key=True)
    conductcode = models.CharField(max_length=6L, blank=True)
    conductcodedescr = models.CharField(max_length=42L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    calculationtypesseq = models.IntegerField(null=True, blank=True)
    ineligibilitycalctypesseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'conductcodes'

class Countrycodes(models.Model):
    countrycode = models.CharField(max_length=8L, blank=True)
    description = models.CharField(max_length=60L, blank=True)
    countrycodesseq = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'countrycodes'

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

class Courseschooltype(models.Model):
    courseseq = models.IntegerField()
    schooltype = models.CharField(max_length=6L)
    class Meta:
        db_table = 'courseschooltype'

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

class Coursetype(models.Model):
    coursetypeseq = models.IntegerField(primary_key=True)
    coursetypedescr = models.CharField(max_length=18L, blank=True)
    isstudyhall = models.IntegerField(null=True, blank=True)
    islunch = models.IntegerField(null=True, blank=True)
    isepims = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'coursetype'

class Department(models.Model):
    departmentseq = models.IntegerField(primary_key=True)
    deptcode = models.CharField(max_length=44L, blank=True)
    deptdescr = models.CharField(max_length=51L, blank=True)
    class Meta:
        db_table = 'department'

class Disciplinestatus(models.Model):
    disciplinestatusseq = models.IntegerField(primary_key=True)
    disciplinestatuscode = models.CharField(max_length=6L, blank=True)
    disciplinestatusdescr = models.CharField(max_length=12L, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'disciplinestatus'

class Districtphonex(models.Model):
    districtprofileseq = models.ForeignKey('Districtprofile', db_column='districtprofileseq')
    phoneseq = models.ForeignKey('Phone', db_column='phoneseq')
    rank = models.IntegerField(null=True, blank=True)
    phonetypeseq = models.ForeignKey('Phonetype', null=True, db_column='phonetypeseq', blank=True)
    class Meta:
        db_table = 'districtphonex'

class Districtprofile(models.Model):
    districtprofileseq = models.IntegerField(primary_key=True)
    academicyearto = models.IntegerField(null=True, blank=True)
    administrator = models.CharField(max_length=23L, blank=True)
    admintitle = models.CharField(max_length=23L, blank=True)
    techdirector = models.CharField(max_length=23L, blank=True)
    districtname = models.CharField(max_length=44L, blank=True)
    website = models.CharField(max_length=40L, blank=True)
    academicyearfrom = models.IntegerField(null=True, blank=True)
    licenseexpiration = models.DateField(null=True, blank=True)
    addressseq = models.IntegerField(null=True, blank=True)
    districtprofilecode = models.CharField(max_length=8L, blank=True)
    class Meta:
        db_table = 'districtprofile'

class Doedetail(models.Model):
    doefilesseq = models.ForeignKey('Doefiles', db_column='doefilesseq')
    doedetailline = models.IntegerField()
    datavalue = models.TextField(blank=True)
    doedetailmessage = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'doedetail'

class Doefield(models.Model):
    doefieldseq = models.IntegerField(primary_key=True)
    doename = models.TextField(blank=True)
    doedescription = models.TextField(blank=True)
    fieldlabel = models.TextField(blank=True)
    calculatedfield = models.IntegerField(null=True, blank=True)
    isfreeform = models.IntegerField(null=True, blank=True)
    doefieldvalueseq = models.IntegerField(null=True, blank=True)
    doefielddefault = models.CharField(max_length=10L, blank=True)
    functionname = models.CharField(max_length=33L, blank=True)
    functionparm = models.CharField(max_length=5L, blank=True)
    datatype = models.CharField(max_length=20L, blank=True)
    exportorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'doefield'

class Doefieldhtmlfile(models.Model):
    doefieldseq = models.ForeignKey(Doefield, db_column='doefieldseq')
    htmlfileseq = models.ForeignKey('Htmlfile', db_column='htmlfileseq')
    viewonly = models.IntegerField(null=True, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'doefieldhtmlfile'

class Doefieldvalue(models.Model):
    doefieldvalueseq = models.IntegerField(primary_key=True)
    doefieldseq = models.IntegerField(null=True, blank=True)
    doevaluecode = models.CharField(max_length=15L, blank=True)
    doevaluedescr = models.TextField(blank=True)
    doefieldstatecode = models.CharField(max_length=14L, blank=True)
    class Meta:
        db_table = 'doefieldvalue'

class Doefiles(models.Model):
    doefilesseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    usersid = models.CharField(max_length=19L)
    submitdate = models.DateField(null=True, blank=True)
    submittime = models.IntegerField(null=True, blank=True)
    processdate = models.DateField(null=True, blank=True)
    processtime = models.IntegerField(null=True, blank=True)
    mailsubject = models.CharField(max_length=41L, blank=True)
    mailto = models.TextField(blank=True)
    datalabels = models.TextField(blank=True)
    reportprogramseq = models.IntegerField(null=True, blank=True)
    doefilesstatus = models.CharField(max_length=38L, blank=True)
    filetype = models.CharField(max_length=21L, blank=True)
    class Meta:
        db_table = 'doefiles'

class Doeschoolcourse(models.Model):
    schoolcourseseq = models.ForeignKey('Schoolcourse', db_column='schoolcourseseq')
    statecode = models.CharField(max_length=5L, blank=True)
    subjectareacourseseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'doeschoolcourse'

class Doestucoursesection(models.Model):
    studentid = models.ForeignKey('Student', db_column='studentid')
    coursesectionseq = models.IntegerField()
    statecode = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'doestucoursesection'

class Emailmessage(models.Model):
    emailmessageseq = models.IntegerField(primary_key=True)
    emailmessagedescr = models.CharField(max_length=53L, blank=True)
    messageformat = models.CharField(max_length=10L, blank=True)
    textmessageseq = models.IntegerField(null=True, blank=True)
    emailmessagemnemonic = models.CharField(max_length=28L, blank=True)
    class Meta:
        db_table = 'emailmessage'

class Emailperson(models.Model):
    emailtypeseq = models.IntegerField(null=True, blank=True)
    personseq = models.IntegerField()
    emailformat = models.CharField(max_length=10L, blank=True)
    emailaddress = models.TextField(blank=True)
    emailpersonseq = models.IntegerField(primary_key=True)
    rank = models.IntegerField(null=True, blank=True)
    unlisted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'emailperson'

class Empcareercostcentx(models.Model):
    hrscostcenterseq = models.IntegerField()
    empid = models.IntegerField()
    empcareerseq = models.IntegerField()
    costcenterseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'empcareercostcentx'

class Englishprof(models.Model):
    englishprofcode = models.CharField(max_length=29L, blank=True)
    englishprofdescr = models.CharField(max_length=41L, blank=True)
    englishprofseq = models.IntegerField(primary_key=True)
    englishprofstateabbr = models.CharField(max_length=6L, blank=True)
    class Meta:
        db_table = 'englishprof'

class Enrollmentreason(models.Model):
    enrollmentreason = models.CharField(max_length=7L, blank=True)
    description = models.TextField(blank=True)
    enrollmentreasonseq = models.IntegerField(primary_key=True)
    statecode = models.CharField(max_length=7L, blank=True)
    class Meta:
        db_table = 'enrollmentreason'

class Enrollmentstatuscodes(models.Model):
    description = models.TextField(blank=True)
    enrollmentstatus = models.CharField(max_length=7L, blank=True)
    enrollmentstatuscodesseq = models.IntegerField(primary_key=True)
    statecode = models.CharField(max_length=7L, blank=True)
    class Meta:
        db_table = 'enrollmentstatuscodes'

class Enrollstatus(models.Model):
    enrollstatusseq = models.IntegerField(primary_key=True)
    enrollstatuscode = models.CharField(max_length=6L, blank=True)
    enrollstatusdescr = models.CharField(max_length=16L, blank=True)
    class Meta:
        db_table = 'enrollstatus'

class Entrywithdrawl(models.Model):
    studentid = models.ForeignKey('Student', db_column='studentid')
    entrywithdrawlseq = models.IntegerField(primary_key=True)
    entrywithdrawldate = models.DateField(null=True, blank=True)
    createdate = models.DateField(null=True, blank=True)
    createusersid = models.CharField(max_length=19L, blank=True)
    comment_field = models.CharField(max_length=60L, db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    enrollmentreasonseq = models.IntegerField(null=True, blank=True)
    enrollmentstatuscodesseq = models.IntegerField(null=True, blank=True)
    entrywithdrawlcodeseq = models.IntegerField(null=True, blank=True)
    reportingreasonseq = models.IntegerField(null=True, blank=True)
    fte = models.IntegerField(null=True, blank=True)
    yearentrydate = models.DateField(null=True, blank=True)
    yearentrycode = models.CharField(max_length=8L, blank=True)
    outplacement = models.IntegerField(null=True, blank=True)
    carryovermemberdays = models.IntegerField(null=True, blank=True)
    carryoverattendancedays = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    schoolid = models.CharField(max_length=11L, blank=True)
    previousschoolprofileseq = models.IntegerField(null=True, blank=True)
    previousschoolcomment = models.TextField(blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    enrollcounter = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'entrywithdrawl'

class Entrywithdrawlcodes(models.Model):
    entrywithdrawlcodeseq = models.IntegerField()
    entrywithdrawlcode = models.CharField(max_length=11L, blank=True)
    entrywithdrawldescr = models.TextField(blank=True)
    statecode = models.CharField(max_length=7L, blank=True)
    enrollstatusseq = models.ForeignKey(Enrollstatus, null=True, db_column='enrollstatusseq', blank=True)
    class Meta:
        db_table = 'entrywithdrawlcodes'

class Ethnicracecodes(models.Model):
    ethniccode = models.CharField(max_length=7L, blank=True)
    description = models.TextField(blank=True)
    statecode = models.CharField(max_length=7L, blank=True)
    ethnicracecodesseq = models.IntegerField(primary_key=True)
    mappingnumber = models.IntegerField(null=True, blank=True)
    show = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'ethnicracecodes'

class Eventcalendar(models.Model):
    eventcalendarseq = models.IntegerField(primary_key=True)
    eventtypesseq = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    eventdate = models.DateField(null=True, blank=True)
    eventtitle = models.CharField(max_length=50L, blank=True)
    eventdescription = models.TextField(blank=True)
    personseq = models.IntegerField(null=True, blank=True)
    datestamp = models.DateField(null=True, blank=True)
    eventtime = models.IntegerField(null=True, blank=True)
    roomcatalogseq = models.IntegerField(null=True, blank=True)
    endtime = models.IntegerField(null=True, blank=True)
    parenteventcalendarseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'eventcalendar'

class Eventtypes(models.Model):
    eventtypesseq = models.IntegerField(primary_key=True)
    eventtypestitle = models.CharField(max_length=23L, blank=True)
    eventicon = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'eventtypes'

class Eventview(models.Model):
    eventtypesseq = models.ForeignKey(Eventtypes, null=True, db_column='eventtypesseq', blank=True)
    usertypeseq = models.ForeignKey('Usertype', db_column='usertypeseq')
    class Meta:
        db_table = 'eventview'

class Exemptcode(models.Model):
    exemptcodeseq = models.IntegerField(primary_key=True)
    exemptcode = models.CharField(max_length=10L, blank=True)
    exemptcodedescr = models.CharField(max_length=33L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'exemptcode'

class Extrasecurity(models.Model):
    usersid = models.CharField(max_length=27L)
    extrasecuritymnem = models.CharField(max_length=28L)
    hasaccess = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'extrasecurity'

class Filetype(models.Model):
    filetypeseq = models.IntegerField(primary_key=True)
    filetypedescr = models.CharField(max_length=21L, blank=True)
    filetypeextension = models.CharField(max_length=10L, blank=True)
    filetypemnem = models.CharField(max_length=12L, blank=True)
    class Meta:
        db_table = 'filetype'

class Glperiodcycle(models.Model):
    schoolprofileseq = models.ForeignKey('Schoolprofile', db_column='schoolprofileseq')
    calendaryearseq = models.ForeignKey(Calendaryear, db_column='calendaryearseq')
    gradelevelseq = models.ForeignKey('Gradelevel', db_column='gradelevelseq')
    schoolperiodsseq = models.ForeignKey('Schoolperiods', db_column='schoolperiodsseq')
    schoolcycleseq = models.ForeignKey('Schoolcycle', db_column='schoolcycleseq')
    periodorder = models.IntegerField(null=True, blank=True)
    starttime = models.IntegerField(null=True, blank=True)
    endtime = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'glperiodcycle'

class Govtest(models.Model):
    govtestseq = models.IntegerField(primary_key=True)
    govtestname = models.CharField(max_length=20L, blank=True)
    govtestdescr = models.CharField(max_length=20L, blank=True)
    govtestcode = models.CharField(max_length=20L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    printontranscript = models.IntegerField(null=True, blank=True)
    scoretest = models.IntegerField(null=True, blank=True)
    scoregradelevelseq = models.IntegerField(null=True, blank=True)
    scoreentrydate = models.CharField(max_length=18L, blank=True)
    class Meta:
        db_table = 'govtest'

class Govtestattr(models.Model):
    govtestattrseq = models.IntegerField(primary_key=True)
    govtestseq = models.IntegerField(null=True, blank=True)
    govtestattrcode = models.CharField(max_length=15L, blank=True)
    govtestattrdescr = models.CharField(max_length=63L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    parentgovtestattrseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'govtestattr'

class Govtestscore(models.Model):
    govtestseq = models.IntegerField(null=True, blank=True)
    govtestattrseq = models.IntegerField(null=True, blank=True)
    gradelevelseq = models.ForeignKey('Gradelevel', null=True, db_column='gradelevelseq', blank=True)
    govtestscorevalue = models.CharField(max_length=16L, blank=True)
    scorecode = models.IntegerField(null=True, blank=True)
    assessdate = models.DateField(null=True, blank=True)
    descr = models.CharField(max_length=37L, blank=True)
    govtestscoreseq = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'govtestscore'

class Govteststats(models.Model):
    govtestseq = models.IntegerField(null=True, blank=True)
    govtestattrseq = models.IntegerField(null=True, blank=True)
    gradelevelseq = models.IntegerField(null=True, blank=True)
    assessdate = models.DateField()
    nummin = models.IntegerField(null=True, blank=True)
    nummax = models.IntegerField(null=True, blank=True)
    expectedscore = models.CharField(max_length=8L, blank=True)
    descr = models.CharField(max_length=47L, blank=True)
    class Meta:
        db_table = 'govteststats'

class Gpacalc(models.Model):
    schooltermseq = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.ForeignKey(Calendaryear, null=True, db_column='calendaryearseq', blank=True)
    schoolprofileseq = models.ForeignKey('Schoolprofile', null=True, db_column='schoolprofileseq', blank=True)
    gradelevelseq = models.ForeignKey('Gradelevel', null=True, db_column='gradelevelseq', blank=True)
    scaleseq = models.ForeignKey('Scale', null=True, db_column='scaleseq', blank=True)
    gpacalcdescr = models.CharField(max_length=24L, blank=True)
    singletermonly = models.IntegerField(null=True, blank=True)
    verticalavg = models.IntegerField(null=True, blank=True)
    ignoregpa = models.IntegerField(null=True, blank=True)
    finalgradeonly = models.IntegerField(null=True, blank=True)
    studentsrankedcount = models.IntegerField(null=True, blank=True)
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    createuser = models.CharField(max_length=19L, blank=True)
    updatedate = models.DateField(null=True, blank=True)
    updatetime = models.IntegerField(null=True, blank=True)
    updateuser = models.CharField(max_length=5L, blank=True)
    gpacalcseq = models.IntegerField(primary_key=True)
    rankoutof = models.IntegerField(null=True, blank=True)
    deletedflag = models.IntegerField(null=True, blank=True)
    testrun = models.IntegerField(null=True, blank=True)
    gradeheadingseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'gpacalc'

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

class Gradeheadingterm(models.Model):
    gradeheadingtermseq = models.IntegerField(primary_key=True)
    schooltermseq = models.IntegerField(null=True, blank=True)
    gradeheadingseq = models.IntegerField(null=True, blank=True)
    openclosed = models.IntegerField(null=True, blank=True)
    gradeparameterseq = models.IntegerField(null=True, blank=True)
    displaygrades = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'gradeheadingterm'

class Gradelevel(models.Model):
    gradelevelseq = models.IntegerField(primary_key=True)
    gradelevel = models.CharField(max_length=8L, blank=True)
    gradeleveldescr = models.CharField(max_length=33L, blank=True)
    nextgradelevelseq = models.IntegerField(null=True, blank=True)
    curryog = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'gradelevel'

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

class Guardianstudent(models.Model):
    personseq = models.ForeignKey('Person', db_column='personseq')
    candismiss = models.IntegerField(null=True, blank=True)
    legalstatusseq = models.ForeignKey('Legalstatus', null=True, db_column='legalstatusseq', blank=True)
    relationshipseq = models.ForeignKey('Relationship', null=True, db_column='relationshipseq', blank=True)
    receivestudent = models.IntegerField(null=True, blank=True)
    primarystudent = models.IntegerField(null=True, blank=True)
    studentid = models.IntegerField()
    liveswstudent = models.IntegerField(null=True, blank=True)
    receivesmail = models.IntegerField(null=True, blank=True)
    internetaccess = models.IntegerField(null=True, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    disallowedpages = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'guardianstudent'

class Healthactcode(models.Model):
    code = models.CharField(max_length=16L, blank=True)
    descr = models.TextField(blank=True)
    reportitem = models.CharField(max_length=8L, blank=True)
    healthactcodeseq = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'healthactcode'

class Healthtestcode(models.Model):
    healthtestcodeseq = models.IntegerField(primary_key=True)
    healthtestcodedescr = models.CharField(max_length=37L, blank=True)
    healthtestcodecomment = models.CharField(max_length=5L, blank=True)
    isrequired = models.IntegerField(null=True, blank=True)
    healthtestcode = models.CharField(max_length=18L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'healthtestcode'

class Holiday(models.Model):
    holidayseq = models.IntegerField(primary_key=True)
    holidaydatestart = models.DateField(null=True, blank=True)
    holidaydescr = models.CharField(max_length=40L, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)
    holidaydateend = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'holiday'

class Honorrolllevel(models.Model):
    honorrolllevelseq = models.IntegerField(primary_key=True)
    honorrollleveldescr = models.CharField(max_length=21L, blank=True)
    honorrollleveldisp = models.CharField(max_length=21L, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    honorrolllevelorder = models.IntegerField(null=True, blank=True)
    gradelevellist = models.CharField(max_length=19L, blank=True)
    listtype = models.CharField(max_length=16L, blank=True)
    class Meta:
        db_table = 'honorrolllevel'

class Honorrolllevelrule(models.Model):
    honorrolllevelseq = models.ForeignKey(Honorrolllevel, db_column='honorrolllevelseq')
    honorrollruleno = models.IntegerField()
    honorrule = models.CharField(max_length=7L, blank=True)
    numberofgrades = models.CharField(max_length=14L, blank=True)
    gradeseq = models.IntegerField(null=True, blank=True)
    majorminor = models.IntegerField(null=True, blank=True)
    credits = models.DecimalField(null=True, max_digits=10, decimal_places=1, blank=True)
    isaverage = models.IntegerField(null=True, blank=True)
    isgpa = models.IntegerField(null=True, blank=True)
    gpa = models.DecimalField(null=True, max_digits=9, decimal_places=1, blank=True)
    scaleseq = models.IntegerField(null=True, blank=True)
    andor = models.CharField(max_length=8L, blank=True)
    isnumcourses = models.IntegerField(null=True, blank=True)
    curriculumlevel = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'honorrolllevelrule'

class Horzavgrule(models.Model):
    horzavgruleseq = models.IntegerField(primary_key=True)
    horzavgrulename = models.CharField(max_length=7L, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'horzavgrule'

class Horzavgrulegradeheading(models.Model):
    horzavgruleseq = models.ForeignKey(Horzavgrule, db_column='horzavgruleseq')
    gradeheadingseq = models.ForeignKey(Gradeheading, db_column='gradeheadingseq')
    horzavgrulevalue = models.IntegerField(null=True, blank=True)
    gpahorzavgrulevalue = models.IntegerField(null=True, blank=True)
    hrhorzavgrulevalue = models.IntegerField(null=True, blank=True)
    horzavgrulepercent = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'horzavgrulegradeheading'

class Horzavgruleterm(models.Model):
    horzavgruleseq = models.ForeignKey(Horzavgrule, null=True, db_column='horzavgruleseq', blank=True)
    termseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'horzavgruleterm'

class Hrsattendance(models.Model):
    attendancecodeseq = models.IntegerField(null=True, blank=True)
    attendancedate = models.DateField(null=True, blank=True)
    attendanceseq = models.IntegerField()
    createdate = models.DateField(null=True, blank=True)
    empid = models.IntegerField(null=True, blank=True)
    approverempid = models.IntegerField(null=True, blank=True)
    compensationseq = models.IntegerField(null=True, blank=True)
    createempid = models.IntegerField(null=True, blank=True)
    dateapproved = models.DateField(null=True, blank=True)
    notes = models.CharField(max_length=57L, blank=True)
    excesshours = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'hrsattendance'

class Hrsattendancecodes(models.Model):
    attcode = models.CharField(max_length=15L, blank=True)
    attseq = models.IntegerField(null=True, blank=True)
    attleavetype = models.CharField(max_length=16L, blank=True)
    attcodedescr = models.CharField(max_length=44L, blank=True)
    attleavefraction = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    class Meta:
        db_table = 'hrsattendancecodes'

class Hrsbargunit(models.Model):
    bargunitseq = models.IntegerField()
    bargunitcode = models.CharField(max_length=10L, blank=True)
    bargunitname = models.CharField(max_length=10L, blank=True)
    bargunitcontactempid = models.IntegerField(null=True, blank=True)
    bargunitaddressseq = models.IntegerField(null=True, blank=True)
    hrscontractseq = models.IntegerField(null=True, blank=True)
    notes = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'hrsbargunit'

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
    altempid = models.CharField(max_length=12L, blank=True)
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

class Hrscareer(models.Model):
    bargunitseq = models.IntegerField(null=True, blank=True)
    buildingcodeseq = models.IntegerField(null=True, blank=True)
    dateend = models.DateField(null=True, blank=True)
    datestart = models.DateField(null=True, blank=True)
    departmentcodeseq = models.IntegerField(null=True, blank=True)
    empstatus = models.CharField(max_length=5L, blank=True)
    emptypeseq = models.IntegerField(null=True, blank=True)
    endcodeseq = models.IntegerField(null=True, blank=True)
    empid = models.IntegerField(null=True, blank=True)
    supervisorempid = models.IntegerField(null=True, blank=True)
    empcareerseq = models.IntegerField()
    dateapproved = models.DateField(null=True, blank=True)
    approverempid = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    fet = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    islicensed = models.IntegerField(null=True, blank=True)
    ishighqualify = models.IntegerField(null=True, blank=True)
    mainjob = models.IntegerField(null=True, blank=True)
    startcodeseq = models.IntegerField(null=True, blank=True)
    staffreportseq = models.IntegerField(null=True, blank=True)
    stepnum = models.IntegerField(null=True, blank=True)
    levelnum = models.IntegerField(null=True, blank=True)
    compenautoassign = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'hrscareer'

class Hrscompensation(models.Model):
    compensationtypeseq = models.IntegerField(null=True, blank=True)
    compensationseq = models.IntegerField()
    empid = models.IntegerField(null=True, blank=True)
    dateawarded = models.DateField(null=True, blank=True)
    unit = models.CharField(max_length=14L, blank=True)
    awardedbyempid = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    awardconfirmedbyempid = models.IntegerField(null=True, blank=True)
    debitorcredit = models.IntegerField(null=True, blank=True)
    amt = models.IntegerField(null=True, blank=True)
    hrscontractseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'hrscompensation'

class Hrscompensationtype(models.Model):
    compensationtypeseq = models.IntegerField()
    compensationtypecode = models.CharField(max_length=15L, blank=True)
    compensationtypedescr = models.CharField(max_length=25L, blank=True)
    class Meta:
        db_table = 'hrscompensationtype'

class Hrscompetencytype(models.Model):
    empcompetencytypeseq = models.IntegerField()
    empcompetencytypecode = models.CharField(max_length=21L, blank=True)
    empcompetencytypedescr = models.CharField(max_length=21L, blank=True)
    class Meta:
        db_table = 'hrscompetencytype'

class Hrscostcenter(models.Model):
    empcostcenterseq = models.IntegerField(primary_key=True)
    empcostcentercode = models.CharField(max_length=20L, blank=True)
    empcostcenterdescr = models.CharField(max_length=24L, blank=True)
    class Meta:
        db_table = 'hrscostcenter'

class Hrsdepartment(models.Model):
    departmentseq = models.ForeignKey(Department, db_column='departmentseq')
    deptcode = models.CharField(max_length=5L, blank=True)
    deptdescr = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'hrsdepartment'

class Hrsdiscipline(models.Model):
    empid = models.IntegerField(null=True, blank=True)
    offensetypeseq = models.IntegerField(null=True, blank=True)
    offensedate = models.DateField(null=True, blank=True)
    offensedescr = models.TextField(blank=True)
    disciplineactiontypeseq = models.IntegerField(null=True, blank=True)
    actionamount = models.IntegerField(null=True, blank=True)
    actionunit = models.CharField(max_length=10L, blank=True)
    actionexpireddate = models.DateField(null=True, blank=True)
    disciplineseq = models.IntegerField()
    servecompleted = models.IntegerField(null=True, blank=True)
    approverempid = models.IntegerField(null=True, blank=True)
    approveddate = models.DateField(null=True, blank=True)
    serveverifiedbyempid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'hrsdiscipline'

class Hrsdisciplineactiontype(models.Model):
    disciplineactiontypeseq = models.IntegerField()
    disciplineactiontypecode = models.CharField(max_length=16L, blank=True)
    disciplineactiontypedescr = models.CharField(max_length=16L, blank=True)
    class Meta:
        db_table = 'hrsdisciplineactiontype'

class Hrsendtype(models.Model):
    empendtypeseq = models.IntegerField(primary_key=True)
    empendtypecode = models.CharField(max_length=7L, blank=True)
    empendtypedescr = models.CharField(max_length=62L, blank=True)
    statecode = models.CharField(max_length=7L, blank=True)
    class Meta:
        db_table = 'hrsendtype'

class Hrsmilitarystatus(models.Model):
    militarystatusseq = models.IntegerField()
    militarystatuscode = models.CharField(max_length=23L, blank=True)
    militarystatusdescr = models.CharField(max_length=28L, blank=True)
    class Meta:
        db_table = 'hrsmilitarystatus'

class Hrsorganization(models.Model):
    organizationseq = models.IntegerField()
    organizationcode = models.CharField(max_length=11L, blank=True)
    organizationname = models.CharField(max_length=38L, blank=True)
    addressseq = models.IntegerField(null=True, blank=True)
    personseq = models.IntegerField(null=True, blank=True)
    phoneseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'hrsorganization'

class Hrsprofdeve(models.Model):
    empid = models.IntegerField(null=True, blank=True)
    datestarted = models.DateField(null=True, blank=True)
    datefinished = models.DateField(null=True, blank=True)
    iscompleted = models.IntegerField(null=True, blank=True)
    courseseq = models.ForeignKey(Course, null=True, db_column='courseseq', blank=True)
    cost = models.IntegerField(null=True, blank=True)
    reimbursecondition = models.CharField(max_length=51L, blank=True)
    reimpursepercent = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    oktoreimburse = models.IntegerField(null=True, blank=True)
    reimburseapproverempid = models.IntegerField(null=True, blank=True)
    coursegrade = models.CharField(max_length=7L, blank=True)
    datereimbursed = models.DateField(null=True, blank=True)
    profdeveseq = models.IntegerField()
    pdprogramseq = models.IntegerField(null=True, blank=True)
    pdstatus = models.CharField(max_length=5L, blank=True)
    applytodiscpn = models.IntegerField(null=True, blank=True)
    coursecredits = models.IntegerField(null=True, blank=True)
    coursehours = models.IntegerField(null=True, blank=True)
    courseprofdevepoints = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'hrsprofdeve'

class Hrsreview(models.Model):
    empreviewtypeseq = models.IntegerField(null=True, blank=True)
    empid = models.IntegerField(null=True, blank=True)
    empcompetencytypeseq = models.IntegerField(null=True, blank=True)
    competencyrating = models.CharField(max_length=20L, blank=True)
    reviewcomments = models.TextField(blank=True)
    reviewdate = models.DateField(null=True, blank=True)
    reviewbyempid = models.IntegerField(null=True, blank=True)
    empreviewseq = models.IntegerField()
    empcompetencytypelist = models.CharField(max_length=14L, blank=True)
    class Meta:
        db_table = 'hrsreview'

class Hrsreviewtype(models.Model):
    empreviewtypeseq = models.IntegerField()
    empreviewtypecode = models.CharField(max_length=18L, blank=True)
    empreviewtypedescr = models.CharField(max_length=18L, blank=True)
    class Meta:
        db_table = 'hrsreviewtype'

class Hrsstaffreport(models.Model):
    staffreportseq = models.IntegerField()
    reportsection = models.CharField(max_length=6L, blank=True)
    reportsubsection = models.CharField(max_length=6L, blank=True)
    reportline = models.CharField(max_length=7L, blank=True)
    reporttitle = models.TextField(blank=True)
    class Meta:
        db_table = 'hrsstaffreport'

class Hrsstaffreportheading(models.Model):
    headingsection = models.CharField(max_length=6L)
    headingsubsection = models.CharField(max_length=6L, blank=True)
    headingprintout = models.CharField(max_length=50L, blank=True)
    class Meta:
        db_table = 'hrsstaffreportheading'

class Hrstimeoff(models.Model):
    dateasof = models.DateField(null=True, blank=True)
    excesshours = models.IntegerField(null=True, blank=True)
    sickcover = models.IntegerField(null=True, blank=True)
    sickearned = models.IntegerField(null=True, blank=True)
    vacationcover = models.IntegerField(null=True, blank=True)
    vacationearned = models.IntegerField(null=True, blank=True)
    personalcover = models.IntegerField(null=True, blank=True)
    personalearned = models.IntegerField(null=True, blank=True)
    profcover = models.IntegerField(null=True, blank=True)
    profearned = models.IntegerField(null=True, blank=True)
    othercover = models.IntegerField(null=True, blank=True)
    otherearned = models.IntegerField(null=True, blank=True)
    hrstimeoffseq = models.IntegerField(primary_key=True)
    empid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'hrstimeoff'

class Hthdisposition(models.Model):
    hthdispositionseq = models.IntegerField(primary_key=True)
    hthdispositiondescr = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'hthdisposition'

class Htmlfile(models.Model):
    htmlfileseq = models.IntegerField(primary_key=True)
    htmlfilename = models.CharField(max_length=45L, blank=True)
    htmlfiledescr = models.CharField(max_length=57L, blank=True)
    htmlhelppage = models.TextField(blank=True)
    htmlimagefilename = models.CharField(max_length=34L, blank=True)
    class Meta:
        db_table = 'htmlfile'

class Htmlmessage(models.Model):
    htmlfileseq = models.ForeignKey(Htmlfile, db_column='htmlfileseq')
    pagelocationseq = models.IntegerField(null=True, blank=True)
    textmessageseq = models.IntegerField(null=True, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'htmlmessage'

class Illnesscode(models.Model):
    illnesscodeseq = models.IntegerField(primary_key=True)
    illnesscode = models.CharField(max_length=8L, blank=True)
    illnessdescr = models.CharField(max_length=44L, blank=True)
    comment_field = models.CharField(max_length=25L, db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    displayorder = models.IntegerField(null=True, blank=True)
    illnesstypeseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'illnesscode'

class Illnesstype(models.Model):
    illnesstypeseq = models.IntegerField(primary_key=True)
    illnesstypecode = models.CharField(max_length=15L, blank=True)
    illnesstypedescr = models.CharField(max_length=44L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'illnesstype'

class Immigrant(models.Model):
    immigrantseq = models.IntegerField(primary_key=True)
    immigrantcode = models.CharField(max_length=7L, blank=True)
    immigrantdesc = models.CharField(max_length=28L, blank=True)
    class Meta:
        db_table = 'immigrant'

class Immunizationcode(models.Model):
    immunizationcodeseq = models.IntegerField(primary_key=True)
    immunizationcode = models.CharField(max_length=18L, blank=True)
    immunizationdescr = models.CharField(max_length=46L, blank=True)
    immunizationname = models.CharField(max_length=19L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'immunizationcode'

class Intervention(models.Model):
    interventionseq = models.IntegerField(primary_key=True)
    interventioncode = models.CharField(max_length=7L, blank=True)
    interventiondescr = models.CharField(max_length=32L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'intervention'

class Jobtypes(models.Model):
    jobtypescodeseq = models.IntegerField()
    description = models.CharField(max_length=44L, blank=True)
    jobgroup = models.CharField(max_length=21L, blank=True)
    staffreportseq = models.IntegerField(null=True, blank=True)
    statecode = models.CharField(max_length=8L, blank=True)
    class Meta:
        db_table = 'jobtypes'

class Languagecodes(models.Model):
    languagecode = models.CharField(max_length=10L, blank=True)
    description = models.CharField(max_length=37L, blank=True)
    stateabbr = models.CharField(max_length=8L, blank=True)
    languagecodesseq = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'languagecodes'

class Languageword(models.Model):
    englishword = models.TextField()
    languagecodesseq = models.ForeignKey(Languagecodes, db_column='languagecodesseq')
    translatedword = models.TextField(blank=True)
    class Meta:
        db_table = 'languageword'

class Legalstatus(models.Model):
    legalstatusseq = models.IntegerField(primary_key=True)
    legalstatusdescr = models.CharField(max_length=31L, blank=True)
    class Meta:
        db_table = 'legalstatus'

class Letter(models.Model):
    letterdescr = models.CharField(max_length=38L, blank=True)
    letterseq = models.IntegerField(primary_key=True)
    lettertext = models.TextField(blank=True)
    lettertypeseq = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'letter'

class Letterdata(models.Model):
    letterdataseq = models.IntegerField(primary_key=True)
    letterdataname = models.CharField(max_length=45L, blank=True)
    letterdatadescr = models.TextField(blank=True)
    lettertypeseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'letterdata'

class Lettertypes(models.Model):
    lettertypeseq = models.IntegerField()
    lettertypedescr = models.CharField(max_length=18L, blank=True)
    class Meta:
        db_table = 'lettertypes'

class Locker(models.Model):
    lockerseq = models.IntegerField(primary_key=True)
    lockerno = models.CharField(max_length=11L, blank=True)
    lockertypeseq = models.IntegerField(null=True, blank=True)
    roomcatalogseq = models.IntegerField(null=True, blank=True)
    serialno = models.CharField(max_length=5L, blank=True)
    comment_field = models.CharField(max_length=28L, db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    brokenflag = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'locker'

class Lockercombo(models.Model):
    lockerseq = models.ForeignKey(Locker, db_column='lockerseq')
    combono = models.IntegerField()
    combination = models.CharField(max_length=15L, blank=True)
    currcombo = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'lockercombo'

class Lockertype(models.Model):
    lockertypeseq = models.IntegerField(primary_key=True)
    lockertypeabbr = models.CharField(max_length=14L, blank=True)
    lockertypedescr = models.CharField(max_length=23L, blank=True)
    class Meta:
        db_table = 'lockertype'

class Loginattempt(models.Model):
    loginattemptseq = models.IntegerField(primary_key=True)
    usersid = models.TextField()
    logindate = models.DateField(null=True, blank=True)
    logintime = models.IntegerField(null=True, blank=True)
    ipaddress = models.CharField(max_length=24L, blank=True)
    loginmsg = models.TextField(blank=True)
    attemptcount = models.IntegerField(null=True, blank=True)
    succeed = models.IntegerField(null=True, blank=True)
    logingroup = models.TextField(blank=True)
    sessionid = models.CharField(max_length=38L, blank=True)
    class Meta:
        db_table = 'loginattempt'

class Lowincome(models.Model):
    lowincomecode = models.CharField(max_length=7L, blank=True)
    lowincomedescr = models.CharField(max_length=63L)
    lowincomeseq = models.IntegerField(primary_key=True)
    lowincomestateabbr = models.CharField(max_length=6L, blank=True)
    class Meta:
        db_table = 'lowincome'

class Lunch(models.Model):
    lunchseq = models.IntegerField(primary_key=True)
    lunchdescr = models.CharField(max_length=21L, blank=True)
    statecode = models.CharField(max_length=6L, blank=True)
    class Meta:
        db_table = 'lunch'

class Lunchtype(models.Model):
    lunchtypeseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    descr = models.CharField(max_length=14L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'lunchtype'

class Mailerprocess(models.Model):
    mailerprocessseq = models.IntegerField(primary_key=True)
    startdate = models.DateField(null=True, blank=True)
    starttime = models.IntegerField(null=True, blank=True)
    currentstatus = models.CharField(max_length=14L, blank=True)
    cycledate = models.DateField(null=True, blank=True)
    cycletime = models.IntegerField(null=True, blank=True)
    stopdate = models.DateField(null=True, blank=True)
    stoptime = models.IntegerField(null=True, blank=True)
    timeoutcount = models.IntegerField(null=True, blank=True)
    transactioncount = models.IntegerField(null=True, blank=True)
    usersid = models.CharField(max_length=11L)
    pid = models.IntegerField(null=True, blank=True)
    hostname = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'mailerprocess'

class Massdoe(models.Model):
    doe001 = models.CharField(max_length=6L, blank=True)
    doe002 = models.CharField(max_length=5L, blank=True)
    doe003 = models.CharField(max_length=5L, blank=True)
    doe004 = models.CharField(max_length=5L)
    doe005 = models.CharField(max_length=5L, blank=True)
    doe006 = models.DateField(null=True, blank=True)
    doe007 = models.CharField(max_length=8L, blank=True)
    doe008 = models.CharField(max_length=5L, blank=True)
    doe009 = models.CharField(max_length=6L, blank=True)
    doe010 = models.CharField(max_length=5L, blank=True)
    doe011 = models.CharField(max_length=5L, blank=True)
    doe012 = models.CharField(max_length=5L, blank=True)
    doe013 = models.CharField(max_length=5L, blank=True)
    doe014 = models.CharField(max_length=5L, blank=True)
    doe015 = models.CharField(max_length=5L, blank=True)
    doe016 = models.CharField(max_length=5L, blank=True)
    doe017 = models.IntegerField(null=True, blank=True)
    doe018 = models.IntegerField(null=True, blank=True)
    doe019 = models.CharField(max_length=5L, blank=True)
    doe020 = models.CharField(max_length=5L, blank=True)
    doe021 = models.CharField(max_length=5L, blank=True)
    doe022 = models.CharField(max_length=5L, blank=True)
    doe023 = models.CharField(max_length=5L, blank=True)
    doe024 = models.CharField(max_length=5L, blank=True)
    doe025 = models.CharField(max_length=5L, blank=True)
    doe026 = models.CharField(max_length=5L, blank=True)
    doe027 = models.CharField(max_length=5L, blank=True)
    doe028 = models.CharField(max_length=5L, blank=True)
    doe029 = models.IntegerField(null=True, blank=True)
    doe030 = models.IntegerField(null=True, blank=True)
    doe031 = models.IntegerField(null=True, blank=True)
    doe032 = models.CharField(max_length=5L, blank=True)
    doe033 = models.CharField(max_length=5L, blank=True)
    doe034 = models.CharField(max_length=5L, blank=True)
    doe035 = models.CharField(max_length=5L, blank=True)
    studentid = models.IntegerField()
    class Meta:
        db_table = 'massdoe'

class Massdoelabel(models.Model):
    massdoelabelseq = models.IntegerField(primary_key=True)
    doe001 = models.CharField(max_length=12L, blank=True)
    doe002 = models.CharField(max_length=12L, blank=True)
    doe003 = models.CharField(max_length=19L, blank=True)
    doe004 = models.CharField(max_length=20L, blank=True)
    doe005 = models.CharField(max_length=18L, blank=True)
    doe006 = models.CharField(max_length=23L, blank=True)
    doe007 = models.CharField(max_length=19L, blank=True)
    doe008 = models.CharField(max_length=19L, blank=True)
    doe009 = models.CharField(max_length=14L, blank=True)
    doe010 = models.CharField(max_length=11L, blank=True)
    doe011 = models.CharField(max_length=27L, blank=True)
    doe012 = models.CharField(max_length=28L, blank=True)
    doe013 = models.CharField(max_length=28L, blank=True)
    doe014 = models.CharField(max_length=23L, blank=True)
    doe015 = models.CharField(max_length=19L, blank=True)
    doe016 = models.CharField(max_length=20L, blank=True)
    doe017 = models.CharField(max_length=29L, blank=True)
    doe018 = models.CharField(max_length=29L, blank=True)
    doe019 = models.CharField(max_length=28L, blank=True)
    doe020 = models.CharField(max_length=33L, blank=True)
    doe021 = models.CharField(max_length=24L, blank=True)
    doe022 = models.CharField(max_length=27L, blank=True)
    doe023 = models.CharField(max_length=28L, blank=True)
    doe024 = models.CharField(max_length=34L, blank=True)
    doe025 = models.CharField(max_length=41L, blank=True)
    doe026 = models.CharField(max_length=49L, blank=True)
    doe027 = models.CharField(max_length=33L, blank=True)
    doe028 = models.CharField(max_length=33L, blank=True)
    doe029 = models.CharField(max_length=21L, blank=True)
    doe030 = models.CharField(max_length=33L, blank=True)
    doe031 = models.CharField(max_length=46L, blank=True)
    doe032 = models.CharField(max_length=36L, blank=True)
    doe033 = models.CharField(max_length=29L, blank=True)
    doe034 = models.CharField(max_length=37L, blank=True)
    doe035 = models.CharField(max_length=40L, blank=True)
    class Meta:
        db_table = 'massdoelabel'

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

class Mcassubjects(models.Model):
    mcassubjectseq = models.IntegerField()
    mcassubject = models.CharField(max_length=37L, blank=True)
    class Meta:
        db_table = 'mcassubjects'

class Medication(models.Model):
    medicationseq = models.IntegerField(primary_key=True)
    medicationtypeseq = models.IntegerField(null=True, blank=True)
    medicationname = models.CharField(max_length=40L, blank=True)
    medicationcode = models.CharField(max_length=8L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    eshsp8named = models.IntegerField(null=True, blank=True)
    eshsp8otherotc = models.IntegerField(null=True, blank=True)
    eshsp8otherpsy = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'medication'

class Medicationsource(models.Model):
    medicationsourceseq = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20L, blank=True)
    class Meta:
        db_table = 'medicationsource'

class Medicationtype(models.Model):
    medicationtypeseq = models.IntegerField(primary_key=True)
    medicationtypename = models.CharField(max_length=18L, blank=True)
    medicationtypeclass = models.CharField(max_length=16L, blank=True)
    medicationtypedescr = models.CharField(max_length=34L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    medicationtypecode = models.CharField(max_length=8L, blank=True)
    class Meta:
        db_table = 'medicationtype'

class Menu(models.Model):
    menuseq = models.IntegerField(primary_key=True)
    parentmenuseq = models.IntegerField(null=True, blank=True)
    menuname = models.CharField(max_length=50L, blank=True)
    image_field = models.CharField(max_length=23L, db_column='image_', blank=True) # Field renamed because it ended with '_'.
    htmlfileseq = models.IntegerField(null=True, blank=True)
    target = models.CharField(max_length=20L, blank=True)
    tabmenuseq = models.IntegerField(null=True, blank=True)
    tabdisplayorder = models.IntegerField(null=True, blank=True)
    tabdisplayname = models.CharField(max_length=59L, blank=True)
    class Meta:
        db_table = 'menu'

class Menuprofile(models.Model):
    profileseq = models.IntegerField(null=True, blank=True)
    menuseq = models.ForeignKey(Menu, db_column='menuseq')
    displayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'menuprofile'

class Menuusertype(models.Model):
    menuseq = models.IntegerField()
    usertypeseq = models.ForeignKey('Usertype', db_column='usertypeseq')
    class Meta:
        db_table = 'menuusertype'

class Messages(models.Model):
    msgno = models.IntegerField()
    msgdescr = models.TextField(blank=True)
    class Meta:
        db_table = 'messages'

class Migrant(models.Model):
    migrantcode = models.CharField(max_length=6L, blank=True)
    migrantdesc = models.CharField(max_length=19L)
    migrantseq = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'migrant'

class Msbcourseseccycle(models.Model):
    coursesectionseq = models.IntegerField()
    schoolcycleseq = models.ForeignKey('Schoolcycle', null=True, db_column='schoolcycleseq', blank=True)
    class Meta:
        db_table = 'msbcourseseccycle'

class Msbcoursesecperiods(models.Model):
    coursesectionseq = models.IntegerField()
    schoolperiodsseq = models.ForeignKey('Schoolperiods', db_column='schoolperiodsseq')
    startendmeet = models.CharField(max_length=10L, blank=True)
    class Meta:
        db_table = 'msbcoursesecperiods'

class Msbcoursesecterms(models.Model):
    coursesectionseq = models.IntegerField()
    schooltermseq = models.ForeignKey('Schoolterm', db_column='schooltermseq')
    startendmeet = models.CharField(max_length=10L, blank=True)
    class Meta:
        db_table = 'msbcoursesecterms'

class Msbcssave(models.Model):
    msbsaveseq = models.ForeignKey('Msbsave', db_column='msbsaveseq')
    coursesectionseq = models.IntegerField()
    schoolcourseseq = models.IntegerField(null=True, blank=True)
    coursesecdesc = models.CharField(max_length=19L, blank=True)
    maxseats = models.IntegerField(null=True, blank=True)
    filledcount = models.IntegerField(null=True, blank=True)
    techedweekseq = models.IntegerField(null=True, blank=True)
    linkedmsbcssaveseq = models.IntegerField(null=True, blank=True)
    horzavgruleseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'msbcssave'

class Msbmsssave(models.Model):
    msbsaveseq = models.ForeignKey('Msbsave', db_column='msbsaveseq')
    scheduleseq = models.IntegerField()
    schoolcourseseq = models.IntegerField(null=True, blank=True)
    schoolcycleseq = models.IntegerField(null=True, blank=True)
    schoolperiodsseq = models.IntegerField(null=True, blank=True)
    schooltermseq = models.ForeignKey('Schoolterm', null=True, db_column='schooltermseq', blank=True)
    roomcatalogseq = models.IntegerField(null=True, blank=True)
    coursesectionseq = models.IntegerField(null=True, blank=True)
    gradelevelseq = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.ForeignKey(Calendaryear, null=True, db_column='calendaryearseq', blank=True)
    schoolprofileseq = models.ForeignKey('Schoolprofile', null=True, db_column='schoolprofileseq', blank=True)
    class Meta:
        db_table = 'msbmsssave'

class Msbpcsave(models.Model):
    msbsaveseq = models.ForeignKey('Msbsave', db_column='msbsaveseq')
    schoolprofileseq = models.ForeignKey('Schoolprofile', null=True, db_column='schoolprofileseq', blank=True)
    schoolcycleseq = models.ForeignKey('Schoolcycle', db_column='schoolcycleseq')
    schoolperiodsseq = models.ForeignKey('Schoolperiods', db_column='schoolperiodsseq')
    periodorder = models.IntegerField(null=True, blank=True)
    starttime = models.IntegerField(null=True, blank=True)
    endtime = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.ForeignKey(Calendaryear, db_column='calendaryearseq')
    class Meta:
        db_table = 'msbpcsave'

class Msbroomteacher(models.Model):
    msbroomteacherseq = models.IntegerField(primary_key=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    schoolcourseseq = models.IntegerField(null=True, blank=True)
    coursesectionseq = models.IntegerField(null=True, blank=True)
    roomcatalogseq = models.IntegerField(null=True, blank=True)
    teacherseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'msbroomteacher'

class Msbrtsave(models.Model):
    msbsaveseq = models.ForeignKey('Msbsave', db_column='msbsaveseq')
    msbrtsaveseq = models.IntegerField(primary_key=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    schoolcourseseq = models.IntegerField(null=True, blank=True)
    coursesectionseq = models.IntegerField(null=True, blank=True)
    roomcatalogseq = models.IntegerField(null=True, blank=True)
    teacherseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'msbrtsave'

class Msbsave(models.Model):
    msbsaveseq = models.IntegerField(primary_key=True)
    savename = models.CharField(max_length=41L, blank=True)
    savecomment = models.TextField(blank=True)
    daysincycle = models.IntegerField(null=True, blank=True)
    numberofperiodsperday = models.IntegerField(null=True, blank=True)
    createuser = models.CharField(max_length=19L, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)
    createdate = models.DateField(null=True, blank=True)
    totalrequests = models.IntegerField(null=True, blank=True)
    totalscheduled = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'msbsave'

class Msbsavegl(models.Model):
    msbsaveseq = models.ForeignKey(Msbsave, db_column='msbsaveseq')
    gradelevel = models.CharField(max_length=7L)
    totalrequests = models.IntegerField(null=True, blank=True)
    totalscheduled = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'msbsavegl'

class Msbsavesc(models.Model):
    msbsaveseq = models.ForeignKey(Msbsave, db_column='msbsaveseq')
    totalrequests = models.IntegerField(null=True, blank=True)
    totalscheduled = models.IntegerField(null=True, blank=True)
    schoolcourseseq = models.IntegerField()
    class Meta:
        db_table = 'msbsavesc'

class Msbscsave(models.Model):
    msbsaveseq = models.ForeignKey(Msbsave, db_column='msbsaveseq')
    schoolcourseseq = models.IntegerField()
    schoolprofileseq = models.ForeignKey('Schoolprofile', null=True, db_column='schoolprofileseq', blank=True)
    calendaryearseq = models.ForeignKey(Calendaryear, null=True, db_column='calendaryearseq', blank=True)
    courseseq = models.ForeignKey(Course, null=True, db_column='courseseq', blank=True)
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
    linkedmsbscsaveseq = models.IntegerField(null=True, blank=True)
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
        db_table = 'msbscsave'

class Msbsrsave(models.Model):
    msbsaveseq = models.ForeignKey(Msbsave, db_column='msbsaveseq')
    studentid = models.ForeignKey('Student', db_column='studentid')
    calendaryearseq = models.ForeignKey(Calendaryear, null=True, db_column='calendaryearseq', blank=True)
    schoolcourseseq = models.IntegerField()
    priority = models.IntegerField(null=True, blank=True)
    isalternate = models.IntegerField(null=True, blank=True)
    prischoolcourseseq = models.IntegerField(null=True, blank=True)
    isscheduled = models.IntegerField(null=True, blank=True)
    alternateno = models.IntegerField(null=True, blank=True)
    islocked = models.IntegerField(null=True, blank=True)
    curriculumlevel = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'msbsrsave'

class Msbstussave(models.Model):
    msbsaveseq = models.ForeignKey(Msbsave, db_column='msbsaveseq')
    schoolcycleseq = models.IntegerField(null=True, blank=True)
    schoolperiodsseq = models.IntegerField(null=True, blank=True)
    schooltermseq = models.ForeignKey('Schoolterm', null=True, db_column='schooltermseq', blank=True)
    studentid = models.ForeignKey('Student', db_column='studentid')
    scheduleseq = models.IntegerField()
    class Meta:
        db_table = 'msbstussave'

class Msbstutcsave(models.Model):
    msbsaveseq = models.ForeignKey(Msbsave, db_column='msbsaveseq')
    studentid = models.ForeignKey('Student', db_column='studentid')
    calendaryearseq = models.ForeignKey(Calendaryear, db_column='calendaryearseq')
    schooltermseq = models.ForeignKey('Schoolterm', db_column='schooltermseq')
    schoolcourseseq = models.IntegerField()
    coursesectionseq = models.IntegerField()
    class Meta:
        db_table = 'msbstutcsave'

class Msbtcsave(models.Model):
    msbsaveseq = models.ForeignKey(Msbsave, db_column='msbsaveseq')
    teacherseq = models.IntegerField()
    calendaryearseq = models.ForeignKey(Calendaryear, db_column='calendaryearseq')
    schooltermseq = models.ForeignKey('Schoolterm', db_column='schooltermseq')
    schoolcourseseq = models.IntegerField()
    coursesectionseq = models.IntegerField()
    class Meta:
        db_table = 'msbtcsave'

class Msbtssave(models.Model):
    msbsaveseq = models.ForeignKey(Msbsave, db_column='msbsaveseq')
    teacherseq = models.IntegerField()
    scheduleseq = models.IntegerField()
    class Meta:
        db_table = 'msbtssave'

class Myquery(models.Model):
    myqueryseq = models.IntegerField(primary_key=True)
    usersid = models.CharField(max_length=24L)
    myqueryname = models.CharField(max_length=63L, blank=True)
    myquerydescr = models.TextField(blank=True)
    class Meta:
        db_table = 'myquery'

class Myquerydocs(models.Model):
    myqueryseq = models.ForeignKey(Myquery, null=True, db_column='myqueryseq', blank=True)
    myquerydocsseq = models.IntegerField(primary_key=True)
    filetypeseq = models.IntegerField(null=True, blank=True)
    pageorientation = models.CharField(max_length=15L, blank=True)
    pagesize = models.IntegerField(null=True, blank=True)
    formfont = models.CharField(max_length=5L, blank=True)
    formfontsize = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'myquerydocs'

class Myqueryfields(models.Model):
    myqueryseq = models.ForeignKey(Myquery, null=True, db_column='myqueryseq', blank=True)
    myqueryfieldsseq = models.IntegerField(primary_key=True)
    tablename = models.CharField(max_length=31L, blank=True)
    fieldname = models.CharField(max_length=37L, blank=True)
    calculatedfieldname = models.CharField(max_length=5L, blank=True)
    fieldformat = models.CharField(max_length=20L, blank=True)
    columnlabel = models.CharField(max_length=49L, blank=True)
    iscalculated = models.IntegerField(null=True, blank=True)
    fieldorder = models.IntegerField(null=True, blank=True)
    subqueryfieldsseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'myqueryfields'

class Myquerysort(models.Model):
    myqueryseq = models.ForeignKey(Myquery, null=True, db_column='myqueryseq', blank=True)
    myquerysortseq = models.IntegerField(primary_key=True)
    tablename = models.CharField(max_length=27L, blank=True)
    fieldname = models.CharField(max_length=25L, blank=True)
    issubtotal = models.IntegerField(null=True, blank=True)
    subtotaltype = models.CharField(max_length=11L, blank=True)
    sortorder = models.IntegerField(null=True, blank=True)
    totaltablename = models.CharField(max_length=24L, blank=True)
    totalfieldname = models.CharField(max_length=18L, blank=True)
    pagebreak = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'myquerysort'

class Myquerytables(models.Model):
    myqueryseq = models.ForeignKey(Myquery, null=True, db_column='myqueryseq', blank=True)
    myquerytablesseq = models.IntegerField(primary_key=True)
    queryorder = models.IntegerField(null=True, blank=True)
    querytype = models.CharField(max_length=11L, blank=True)
    tablename = models.CharField(max_length=31L, blank=True)
    isbuffer = models.IntegerField(null=True, blank=True)
    subqueryseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'myquerytables'

class Myqueryusersx(models.Model):
    myqueryseq = models.IntegerField()
    usersid = models.ForeignKey('Users', db_column='usersid')
    isowner = models.IntegerField(null=True, blank=True)
    canupdate = models.IntegerField(null=True, blank=True)
    canshare = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'myqueryusersx'

class Myquerywhere(models.Model):
    myqueryseq = models.ForeignKey(Myquery, null=True, db_column='myqueryseq', blank=True)
    filtertype = models.CharField(max_length=25L, blank=True)
    leftbracket = models.CharField(max_length=6L, blank=True)
    lefttablename = models.CharField(max_length=31L, blank=True)
    leftfieldname = models.CharField(max_length=37L, blank=True)
    operation = models.CharField(max_length=12L, blank=True)
    righttablename = models.CharField(max_length=31L, blank=True)
    rightfieldname = models.CharField(max_length=32L, blank=True)
    rightconstant = models.TextField(blank=True)
    rightbracket = models.CharField(max_length=6L, blank=True)
    myquerywhereseq = models.IntegerField(primary_key=True)
    candophrase = models.CharField(max_length=5L, blank=True)
    myquerytablesseq = models.IntegerField(null=True, blank=True)
    filterorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'myquerywhere'

class Notes(models.Model):
    areaname = models.CharField(max_length=27L)
    uniquekey = models.CharField(max_length=12L)
    personseq = models.IntegerField()
    createusersid = models.CharField(max_length=24L, blank=True)
    createdate = models.DateField()
    createtime = models.IntegerField()
    updateusersid = models.CharField(max_length=24L)
    updatedate = models.DateField(null=True, blank=True)
    updatetime = models.IntegerField(null=True, blank=True)
    notedata = models.TextField(blank=True)
    class Meta:
        db_table = 'notes'

class Nurse(models.Model):
    nurseseq = models.IntegerField(primary_key=True)
    personseq = models.IntegerField(null=True, blank=True)
    active = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'nurse'

class Offenses(models.Model):
    offenseseq = models.IntegerField()
    offensecode = models.CharField(max_length=11L, blank=True)
    offensedescr = models.TextField(blank=True)
    schoolprofileseq = models.ForeignKey('Schoolprofile', null=True, db_column='schoolprofileseq', blank=True)
    offensetypeseq = models.ForeignKey('Offensetype', null=True, db_column='offensetypeseq', blank=True)
    offensestatecode = models.CharField(max_length=10L, blank=True)
    class Meta:
        db_table = 'offenses'

class Offensetype(models.Model):
    offensetypeseq = models.IntegerField(primary_key=True)
    offensetypedescr = models.CharField(max_length=23L, blank=True)
    offensetypecode = models.CharField(max_length=14L, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    reporttodoe = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'offensetype'

class Osfile(models.Model):
    osfileseq = models.IntegerField(primary_key=True)
    filename = models.CharField(max_length=23L, blank=True)
    filetypeseq = models.CharField(max_length=6L, blank=True)
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    usersid = models.CharField(max_length=19L, blank=True)
    osfilesize = models.IntegerField(null=True, blank=True)
    numdownload = models.IntegerField(null=True, blank=True)
    descr = models.CharField(max_length=16L, blank=True)
    osfilelocation = models.CharField(max_length=21L, blank=True)
    class Meta:
        db_table = 'osfile'

class Osfiledata(models.Model):
    osfileseq = models.ForeignKey(Osfile, db_column='osfileseq')
    order_field = models.IntegerField(db_column='order_') # Field renamed because it ended with '_'.
    data = models.CharField(max_length=23L, blank=True)
    class Meta:
        db_table = 'osfiledata'

class Osfilextable(models.Model):
    tablename = models.CharField(max_length=11L)
    areaname = models.CharField(max_length=14L)
    keyvalue = models.CharField(max_length=19L)
    osfileseq = models.ForeignKey(Osfile, null=True, db_column='osfileseq', blank=True)
    class Meta:
        db_table = 'osfilextable'

class Outputdevice(models.Model):
    outputdeviceseq = models.IntegerField(primary_key=True)
    outputdevicename = models.CharField(max_length=24L, blank=True)
    outputdevicecmd = models.TextField(blank=True)
    outputdevicetype = models.CharField(max_length=6L, blank=True)
    iscolor = models.IntegerField(null=True, blank=True)
    canprintduplex = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'outputdevice'

class Pagelocation(models.Model):
    pagelocationseq = models.IntegerField(primary_key=True)
    pagelocationdescr = models.CharField(max_length=12L, blank=True)
    class Meta:
        db_table = 'pagelocation'

class Parentaction(models.Model):
    parentactionseq = models.IntegerField(primary_key=True)
    parentactioncode = models.CharField(max_length=8L, blank=True)
    parentactiondescr = models.TextField(blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'parentaction'

class Parms(models.Model):
    application = models.CharField(max_length=63L)
    groupname = models.CharField(max_length=41L)
    parmname = models.TextField()
    parmvalue = models.TextField(blank=True)
    class Meta:
        db_table = 'parms'

class Pclcmdmnem(models.Model):
    pclcommandmnem = models.CharField(max_length=19L)
    class Meta:
        db_table = 'pclcmdmnem'

class Pclcommand(models.Model):
    pclcommandseq = models.IntegerField(primary_key=True)
    pclcommandmnem = models.CharField(max_length=19L, blank=True)
    pclcommandname = models.CharField(max_length=38L, blank=True)
    pclcommandvalue = models.CharField(max_length=12L, blank=True)
    pclcommandpdfvalue = models.CharField(max_length=16L, blank=True)
    class Meta:
        db_table = 'pclcommand'

class Pcldocumenttype(models.Model):
    pcldocumenttypeseq = models.IntegerField(primary_key=True)
    pcldocumenttypename = models.CharField(max_length=31L, blank=True)
    multipageform = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'pcldocumenttype'

class Pcldocumenttypefield(models.Model):
    pcldocumenttypeseq = models.ForeignKey(Pcldocumenttype, db_column='pcldocumenttypeseq')
    pclfieldseq = models.ForeignKey('Pclfield', db_column='pclfieldseq')
    class Meta:
        db_table = 'pcldocumenttypefield'

class Pclfield(models.Model):
    pclfieldseq = models.IntegerField(primary_key=True)
    pclfieldmnem = models.CharField(max_length=47L, blank=True)
    pclfielddescr = models.TextField(blank=True)
    iscalculated = models.IntegerField(null=True, blank=True)
    dbfieldname = models.TextField(blank=True)
    reportsection = models.CharField(max_length=12L, blank=True)
    dependantpclfieldseq = models.IntegerField(null=True, blank=True)
    isobject = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'pclfield'

class Pclform(models.Model):
    pclformseq = models.IntegerField(primary_key=True)
    pcldocumenttypeseq = models.IntegerField(null=True, blank=True)
    pclformname = models.CharField(max_length=54L, blank=True)
    defaultsymbolset = models.IntegerField(null=True, blank=True)
    defaultfont = models.IntegerField(null=True, blank=True)
    defaultfontsize = models.IntegerField(null=True, blank=True)
    pageorientation = models.IntegerField(null=True, blank=True)
    pagesize = models.IntegerField(null=True, blank=True)
    numberofpages = models.IntegerField(null=True, blank=True)
    defaultfontcolor = models.IntegerField(null=True, blank=True)
    defaultlinecolor = models.IntegerField(null=True, blank=True)
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    createuser = models.CharField(max_length=19L, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    numbodylines = models.IntegerField(null=True, blank=True)
    bodytype = models.CharField(max_length=15L, blank=True)
    bodyxpos = models.IntegerField(null=True, blank=True)
    bodyypos = models.IntegerField(null=True, blank=True)
    numbodycols = models.IntegerField(null=True, blank=True)
    numofforms = models.IntegerField(null=True, blank=True)
    isfullpage = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'pclform'

class Pclformbodydtl(models.Model):
    pclformseq = models.ForeignKey(Pclform, db_column='pclformseq')
    lineno_field = models.IntegerField(db_column='lineno_') # Field renamed because it ended with '_'.
    xpos = models.IntegerField(null=True, blank=True)
    ypos = models.IntegerField(null=True, blank=True)
    colno = models.IntegerField()
    class Meta:
        db_table = 'pclformbodydtl'

class Pclformfield(models.Model):
    pclformfieldseq = models.IntegerField(primary_key=True)
    pclfieldseq = models.IntegerField(null=True, blank=True)
    symbolset = models.IntegerField(null=True, blank=True)
    fieldfont = models.IntegerField(null=True, blank=True)
    fieldfontcolor = models.IntegerField(null=True, blank=True)
    fieldfontsize = models.IntegerField(null=True, blank=True)
    xpos = models.IntegerField(null=True, blank=True)
    ypos = models.IntegerField(null=True, blank=True)
    reportsection = models.CharField(max_length=12L, blank=True)
    numinstances = models.IntegerField(null=True, blank=True)
    pclformseq = models.IntegerField(null=True, blank=True)
    parentlineno = models.IntegerField(null=True, blank=True)
    parentpclformfieldseq = models.IntegerField(null=True, blank=True)
    fieldfontweight = models.IntegerField(null=True, blank=True)
    fieldfontstyle = models.IntegerField(null=True, blank=True)
    fieldfontunderline = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    formnum = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'pclformfield'

class Pclformfielddtl(models.Model):
    pclformfieldseq = models.IntegerField()
    lineno_field = models.IntegerField(db_column='lineno_') # Field renamed because it ended with '_'.
    xpos = models.IntegerField(null=True, blank=True)
    ypos = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'pclformfielddtl'

class Pclformlayout(models.Model):
    pclformlayoutseq = models.IntegerField(primary_key=True)
    pclformseq = models.IntegerField(null=True, blank=True)
    layouttype = models.CharField(max_length=10L, blank=True)
    x1pos = models.IntegerField(null=True, blank=True)
    y1pos = models.IntegerField(null=True, blank=True)
    x2pos = models.IntegerField(null=True, blank=True)
    y2pos = models.IntegerField(null=True, blank=True)
    fieldfont = models.IntegerField(null=True, blank=True)
    fieldfontcolor = models.IntegerField(null=True, blank=True)
    fieldfontsize = models.IntegerField(null=True, blank=True)
    symbolset = models.IntegerField(null=True, blank=True)
    pclformlayoutdescr = models.TextField(blank=True)
    pclformlayoutvalue = models.TextField(blank=True)
    fieldfontweight = models.IntegerField(null=True, blank=True)
    fieldfontstyle = models.IntegerField(null=True, blank=True)
    fieldfontunderline = models.IntegerField(null=True, blank=True)
    formnum = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'pclformlayout'

class Periodcycle(models.Model):
    schoolprofileseq = models.ForeignKey('Schoolprofile', null=True, db_column='schoolprofileseq', blank=True)
    schoolcycleseq = models.ForeignKey('Schoolcycle', db_column='schoolcycleseq')
    schoolperiodsseq = models.ForeignKey('Schoolperiods', db_column='schoolperiodsseq')
    periodorder = models.IntegerField(null=True, blank=True)
    starttime = models.IntegerField(null=True, blank=True)
    endtime = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.ForeignKey(Calendaryear, db_column='calendaryearseq')
    class Meta:
        db_table = 'periodcycle'

class Perkinslowincome(models.Model):
    perkinslowincomecode = models.CharField(max_length=7L, blank=True)
    perkinslowincomedescr = models.CharField(max_length=58L, blank=True)
    perkinslowincomeseq = models.IntegerField(primary_key=True)
    perkinslowincomestateabbr = models.CharField(max_length=7L, blank=True)
    class Meta:
        db_table = 'perkinslowincome'

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

class Personactivity(models.Model):
    activityseq = models.ForeignKey(Activity, null=True, db_column='activityseq', blank=True)
    activitystatusseq = models.IntegerField(null=True, blank=True)
    gradelevel = models.CharField(max_length=8L, blank=True)
    personactivityenddate = models.DateField(null=True, blank=True)
    personactivityseq = models.IntegerField(primary_key=True)
    personactivitystartdate = models.DateField(null=True, blank=True)
    personseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'personactivity'

class Personactivitypositionx(models.Model):
    personseq = models.ForeignKey(Person, db_column='personseq')
    activitypositionseq = models.ForeignKey(Activityposition, null=True, db_column='activitypositionseq', blank=True)
    personactivityseq = models.ForeignKey(Personactivity, null=True, db_column='personactivityseq', blank=True)
    class Meta:
        db_table = 'personactivitypositionx'

class Persondoefield(models.Model):
    doefieldseq = models.ForeignKey(Doefield, db_column='doefieldseq')
    doefieldvalueseq = models.IntegerField(null=True, blank=True)
    doefieldfreeformvalue = models.CharField(max_length=10L, blank=True)
    personseq = models.ForeignKey(Person, db_column='personseq')
    alternatekey = models.CharField(max_length=19L, blank=True)
    datestamp = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'persondoefield'

class Personethnicx(models.Model):
    personseq = models.ForeignKey(Person, db_column='personseq')
    ethnicracecodesseq = models.ForeignKey(Ethnicracecodes, db_column='ethnicracecodesseq')
    class Meta:
        db_table = 'personethnicx'

class Personstatus(models.Model):
    personstatusseq = models.IntegerField(primary_key=True)
    personstatusdescr = models.CharField(max_length=15L, blank=True)
    class Meta:
        db_table = 'personstatus'

class Persontitle(models.Model):
    persontitleseq = models.IntegerField(primary_key=True)
    persontitledescr = models.CharField(max_length=10L, blank=True)
    class Meta:
        db_table = 'persontitle'

class Personuserfee(models.Model):
    personuserfeeseq = models.IntegerField(primary_key=True)
    personseq = models.IntegerField()
    createdate = models.DateField(null=True, blank=True)
    userfeeseq = models.IntegerField(null=True, blank=True)
    cancelled = models.IntegerField(null=True, blank=True)
    cancelleddate = models.DateField(null=True, blank=True)
    cancelledusersid = models.CharField(max_length=5L)
    class Meta:
        db_table = 'personuserfee'

class Personuserfeeinv(models.Model):
    personuserfeeinvseq = models.IntegerField(primary_key=True)
    cancelled = models.IntegerField(null=True, blank=True)
    cancelleddate = models.DateField(null=True, blank=True)
    cancelledusersid = models.CharField(max_length=19L)
    personuserfeeseq = models.IntegerField(null=True, blank=True)
    userfeeschedseq = models.IntegerField(null=True, blank=True)
    paidinfull = models.IntegerField(null=True, blank=True)
    discountamtper = models.IntegerField(null=True, blank=True)
    discountamt = models.IntegerField(null=True, blank=True)
    discountcomment = models.CharField(max_length=7L, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    duedate = models.DateField(null=True, blank=True)
    invoicedate = models.DateField(null=True, blank=True)
    modusersid = models.CharField(max_length=19L, blank=True)
    modifieddate = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'personuserfeeinv'

class Personuserfeepmt(models.Model):
    personuserfeepmtseq = models.IntegerField(primary_key=True)
    paiddate = models.DateField(null=True, blank=True)
    voided = models.IntegerField(null=True, blank=True)
    voiddate = models.DateField(null=True, blank=True)
    voidusersid = models.CharField(max_length=19L)
    amount = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    personuserfeeinvseq = models.IntegerField(null=True, blank=True)
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    createusersid = models.CharField(max_length=19L, blank=True)
    comments = models.TextField(blank=True)
    dbcr = models.IntegerField(null=True, blank=True)
    checkno = models.CharField(max_length=19L, blank=True)
    receiptno = models.CharField(max_length=10L, blank=True)
    userfeeacctseq = models.IntegerField()
    modusersid = models.CharField(max_length=19L, blank=True)
    modifieddate = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'personuserfeepmt'

class Pgstatus(models.Model):
    pgstatusseq = models.IntegerField(primary_key=True)
    pgstatuscode = models.CharField(max_length=8L, blank=True)
    pgstatusdescr = models.CharField(max_length=19L, blank=True)
    class Meta:
        db_table = 'pgstatus'

class Phone(models.Model):
    phoneseq = models.IntegerField(primary_key=True)
    phoneno = models.CharField(max_length=24L, blank=True)
    phonetypeseq = models.IntegerField(null=True, blank=True)
    personseq = models.IntegerField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    extension = models.CharField(max_length=19L, blank=True)
    unlisted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'phone'

class Phoneperson(models.Model):
    phoneseq = models.ForeignKey(Phone, db_column='phoneseq')
    personseq = models.IntegerField(null=True, blank=True)
    studentid = models.IntegerField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    phonetypeseq = models.ForeignKey('Phonetype', null=True, db_column='phonetypeseq', blank=True)
    class Meta:
        db_table = 'phoneperson'

class Phonetype(models.Model):
    phonetypeseq = models.IntegerField(primary_key=True)
    phonetypedescr = models.CharField(max_length=10L, blank=True)
    class Meta:
        db_table = 'phonetype'

class Postgraduateplans(models.Model):
    description = models.CharField(max_length=57L, blank=True)
    statecode = models.CharField(max_length=8L, blank=True)
    postgraduateplanscode = models.CharField(max_length=24L, blank=True)
    postgraduateplansseq = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'postgraduateplans'

class Profiles(models.Model):
    profileseq = models.IntegerField()
    profilename = models.CharField(max_length=40L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    menuseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'profiles'

class Publisheddocs(models.Model):
    publisheddocsseq = models.IntegerField(primary_key=True)
    osfileseq = models.IntegerField(null=True, blank=True)
    reportdueseq = models.IntegerField(null=True, blank=True)
    publishdate = models.DateField(null=True, blank=True)
    totaldownloads = models.IntegerField(null=True, blank=True)
    usersid = models.CharField(max_length=19L)
    filetypeseq = models.IntegerField(null=True, blank=True)
    lastused = models.DateField(null=True, blank=True)
    documentlabel = models.CharField(max_length=29L, blank=True)
    documentcomment = models.CharField(max_length=31L, blank=True)
    publishtime = models.IntegerField(null=True, blank=True)
    personseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'publisheddocs'

class Punishments(models.Model):
    punishmentseq = models.IntegerField()
    punishmentcode = models.CharField(max_length=10L, blank=True)
    punishmentdescr = models.TextField(blank=True)
    punishmenttypeseq = models.IntegerField(null=True, blank=True)
    punishmentuomseq = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.ForeignKey('Schoolprofile', null=True, db_column='schoolprofileseq', blank=True)
    punishmentstatecode = models.CharField(max_length=10L, blank=True)
    class Meta:
        db_table = 'punishments'

class Punishmenttypes(models.Model):
    punishmenttypeseq = models.IntegerField()
    punishmenttypecode = models.CharField(max_length=14L, blank=True)
    punishmenttypedescr = models.CharField(max_length=41L, blank=True)
    schoolprofileseq = models.ForeignKey('Schoolprofile', null=True, db_column='schoolprofileseq', blank=True)
    class Meta:
        db_table = 'punishmenttypes'

class Punishmentunits(models.Model):
    punishmentuomseq = models.IntegerField()
    punishmentuomdescr = models.CharField(max_length=31L, blank=True)
    class Meta:
        db_table = 'punishmentunits'

class Reason(models.Model):
    reasonseq = models.IntegerField(primary_key=True)
    reasoncode = models.CharField(max_length=8L, blank=True)
    reasondescr = models.CharField(max_length=46L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    illinjure = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'reason'

class Regaddress(models.Model):
    addressseq = models.IntegerField()
    address1 = models.CharField(max_length=42L, blank=True)
    address2 = models.CharField(max_length=54L, blank=True)
    streetno = models.CharField(max_length=33L, blank=True)
    aptno = models.CharField(max_length=16L, blank=True)
    city = models.CharField(max_length=29L, blank=True)
    state = models.CharField(max_length=7L, blank=True)
    zipcode = models.CharField(max_length=18L, blank=True)
    addresstypeseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'regaddress'

class Regaddressperson(models.Model):
    addressseq = models.IntegerField(null=True, blank=True)
    personseq = models.IntegerField()
    addresstypeseq = models.IntegerField(null=True, blank=True)
    studentid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'regaddressperson'

class Regguardstudata(models.Model):
    personseq = models.IntegerField()
    relationshipseq = models.ForeignKey('Relationship', null=True, db_column='relationshipseq', blank=True)
    primarystudent = models.IntegerField(null=True, blank=True)
    studentid = models.ForeignKey('Student', db_column='studentid')
    stufirstname = models.CharField(max_length=29L, blank=True)
    stulastname = models.CharField(max_length=28L, blank=True)
    stumiddlename = models.CharField(max_length=29L, blank=True)
    dob = models.DateField(null=True, blank=True)
    cityofbirth = models.CharField(max_length=44L, blank=True)
    ssn = models.CharField(max_length=19L, blank=True)
    livewithyou = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'regguardstudata'

class Regperson(models.Model):
    personseq = models.IntegerField()
    lastname = models.TextField()
    firstname = models.CharField(max_length=33L, blank=True)
    password = models.CharField(max_length=25L)
    email = models.TextField(blank=True)
    middleinitial = models.CharField(max_length=24L, blank=True)
    persontitleseq = models.ForeignKey(Persontitle, null=True, db_column='persontitleseq', blank=True)
    imagefile = models.CharField(max_length=5L, blank=True)
    workplace = models.TextField(blank=True)
    reqdate = models.DateField(null=True, blank=True)
    reqtime = models.IntegerField(null=True, blank=True)
    personstatusseq = models.ForeignKey(Personstatus, null=True, db_column='personstatusseq', blank=True)
    gender = models.IntegerField(null=True, blank=True)
    usersid = models.CharField(max_length=47L)
    processeddate = models.DateField(null=True, blank=True)
    processedtime = models.IntegerField(null=True, blank=True)
    processeduser = models.CharField(max_length=5L, blank=True)
    reqstatus = models.CharField(max_length=15L, blank=True)
    assignedpersonseq = models.IntegerField(null=True, blank=True)
    comments = models.CharField(max_length=58L, blank=True)
    class Meta:
        db_table = 'regperson'

class Regphone(models.Model):
    phoneseq = models.IntegerField()
    phoneno = models.CharField(max_length=24L, blank=True)
    phonetypeseq = models.ForeignKey(Phonetype, null=True, db_column='phonetypeseq', blank=True)
    personseq = models.IntegerField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    extension = models.CharField(max_length=33L, blank=True)
    unlisted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'regphone'

class Relationship(models.Model):
    relationshipseq = models.IntegerField(primary_key=True)
    relationshipdescr = models.CharField(max_length=27L, blank=True)
    class Meta:
        db_table = 'relationship'

class Reportdue(models.Model):
    reportrecurringseq = models.IntegerField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    reportdataname = models.TextField(blank=True)
    reportdatavalue = models.TextField(blank=True)
    state = models.CharField(max_length=12L, blank=True)
    submitdate = models.DateField(null=True, blank=True)
    submittime = models.IntegerField(null=True, blank=True)
    processdate = models.DateField(null=True, blank=True)
    processtime = models.IntegerField(null=True, blank=True)
    reportdueseq = models.IntegerField(primary_key=True)
    usersid = models.CharField(max_length=24L)
    maildataname = models.TextField(blank=True)
    maildatavalue = models.TextField(blank=True)
    reportprogramseq = models.IntegerField(null=True, blank=True)
    inputlabelnames = models.TextField(blank=True)
    inputdata = models.TextField(blank=True)
    userstate = models.CharField(max_length=18L, blank=True)
    viewed = models.IntegerField(null=True, blank=True)
    startdate = models.DateField(null=True, blank=True)
    starttime = models.IntegerField(null=True, blank=True)
    savereport = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'reportdue'

class Reportingreason(models.Model):
    description = models.TextField(blank=True)
    reportingreason = models.CharField(max_length=7L, blank=True)
    reportingreasonseq = models.IntegerField(primary_key=True)
    statecode = models.CharField(max_length=7L, blank=True)
    class Meta:
        db_table = 'reportingreason'

class Reportmessage(models.Model):
    reportmessageseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    reportprogramseq = models.IntegerField(null=True, blank=True)
    textmessageseq = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=8L, blank=True)
    class Meta:
        db_table = 'reportmessage'

class Reportparms(models.Model):
    reportprogramname = models.CharField(max_length=16L)
    groupname = models.CharField(max_length=7L)
    parmname = models.CharField(max_length=24L)
    parmvalue = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'reportparms'

class Reportpostprocess(models.Model):
    reportpostprocessseq = models.IntegerField(primary_key=True)
    reportprogramseq = models.IntegerField(null=True, blank=True)
    pptype = models.CharField(max_length=8L, blank=True)
    server = models.CharField(max_length=24L, blank=True)
    ppuserid = models.CharField(max_length=15L, blank=True)
    pppassword = models.CharField(max_length=16L, blank=True)
    ppscript = models.CharField(max_length=5L, blank=True)
    outputtypes = models.CharField(max_length=16L, blank=True)
    ppdestfilename = models.CharField(max_length=28L, blank=True)
    class Meta:
        db_table = 'reportpostprocess'

class Reportprocess(models.Model):
    reportprocessseq = models.IntegerField(primary_key=True)
    startdate = models.DateField(null=True, blank=True)
    starttime = models.IntegerField(null=True, blank=True)
    currentstatus = models.CharField(max_length=14L, blank=True)
    cycledate = models.DateField(null=True, blank=True)
    cycletime = models.IntegerField(null=True, blank=True)
    stopdate = models.DateField(null=True, blank=True)
    stoptime = models.IntegerField(null=True, blank=True)
    timeoutcount = models.IntegerField(null=True, blank=True)
    transactioncount = models.IntegerField(null=True, blank=True)
    usersid = models.CharField(max_length=11L)
    processbatch = models.IntegerField(null=True, blank=True)
    pid = models.IntegerField(null=True, blank=True)
    hostname = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'reportprocess'

class Reportprogram(models.Model):
    htmlfileseq = models.IntegerField(null=True, blank=True)
    reportprogramname = models.CharField(max_length=37L, blank=True)
    attachname = models.CharField(max_length=44L, blank=True)
    reportdescr = models.CharField(max_length=53L)
    reportprogramseq = models.IntegerField(primary_key=True)
    createmyreport = models.IntegerField(null=True, blank=True)
    reporttypeseq = models.IntegerField(null=True, blank=True)
    sendemail = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'reportprogram'

class Reportrecurring(models.Model):
    reportrecurringseq = models.IntegerField(primary_key=True)
    occurance = models.CharField(max_length=11L, blank=True)
    daily = models.CharField(max_length=14L, blank=True)
    monday = models.IntegerField(null=True, blank=True)
    tuesday = models.IntegerField(null=True, blank=True)
    wednesday = models.IntegerField(null=True, blank=True)
    thursday = models.IntegerField(null=True, blank=True)
    friday = models.IntegerField(null=True, blank=True)
    saturday = models.IntegerField(null=True, blank=True)
    sunday = models.IntegerField(null=True, blank=True)
    monthly = models.CharField(max_length=14L, blank=True)
    maildataname = models.CharField(max_length=28L, blank=True)
    maildatavalue = models.CharField(max_length=45L, blank=True)
    reportprogramseq = models.IntegerField(null=True, blank=True)
    inputlabelnames = models.TextField(blank=True)
    inputdata = models.TextField(blank=True)
    reportdataname = models.TextField(blank=True)
    reportdatavalue = models.TextField(blank=True)
    usersid = models.CharField(max_length=19L)
    starttime = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'reportrecurring'

class Reporttype(models.Model):
    reporttypeseq = models.IntegerField(primary_key=True)
    reporttypename = models.CharField(max_length=20L, blank=True)
    class Meta:
        db_table = 'reporttype'

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

class Scale(models.Model):
    scaleseq = models.IntegerField(primary_key=True)
    scalecode = models.CharField(max_length=10L, blank=True)
    scaledescr = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'scale'

class Schedulerhist(models.Model):
    schedulerhistseq = models.IntegerField(primary_key=True)
    usersid = models.CharField(max_length=20L)
    startdate = models.DateField(null=True, blank=True)
    starttime = models.IntegerField(null=True, blank=True)
    summaryfile = models.TextField(blank=True)
    detailfile = models.TextField(blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    endtime = models.IntegerField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    success = models.IntegerField(null=True, blank=True)
    reason = models.CharField(max_length=32L, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'schedulerhist'

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

class Schoolcoursedept(models.Model):
    departmentseq = models.ForeignKey(Department, db_column='departmentseq')
    schoolcourseseq = models.ForeignKey(Schoolcourse, db_column='schoolcourseseq')
    credits = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)
    class Meta:
        db_table = 'schoolcoursedept'

class Schoolcourseprereq(models.Model):
    schoolcourseseq = models.ForeignKey(Schoolcourse, db_column='schoolcourseseq')
    prereqschoolcourseseq = models.IntegerField()
    class Meta:
        db_table = 'schoolcourseprereq'

class Schoolcoursescale(models.Model):
    schoolcourseseq = models.IntegerField()
    scaleseq = models.ForeignKey(Scale, db_column='scaleseq')
    includeincalc = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'schoolcoursescale'

class Schoolcycle(models.Model):
    schoolcycleseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    daytitle = models.CharField(max_length=16L, blank=True)
    daytitleabbr = models.CharField(max_length=11L, blank=True)
    dayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'schoolcycle'

class Schoolgradeschedweight(models.Model):
    schoolprofileseq = models.ForeignKey('Schoolprofile', db_column='schoolprofileseq')
    gradelevelseq = models.ForeignKey(Gradelevel, db_column='gradelevelseq')
    weight = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'schoolgradeschedweight'

class Schooloutputx(models.Model):
    schoolprofileseq = models.ForeignKey('Schoolprofile', db_column='schoolprofileseq')
    outputdeviceseq = models.ForeignKey(Outputdevice, db_column='outputdeviceseq')
    class Meta:
        db_table = 'schooloutputx'

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

class Schoolphonex(models.Model):
    rank = models.IntegerField(null=True, blank=True)
    phonetypeseq = models.ForeignKey(Phonetype, null=True, db_column='phonetypeseq', blank=True)
    schoolprofileseq = models.ForeignKey('Schoolprofile', db_column='schoolprofileseq')
    phoneseq = models.ForeignKey(Phone, db_column='phoneseq')
    class Meta:
        db_table = 'schoolphonex'

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

class Schoolprofilegradex(models.Model):
    schoolprofileseq = models.ForeignKey(Schoolprofile, db_column='schoolprofileseq')
    gradelevelseq = models.ForeignKey(Gradelevel, null=True, db_column='gradelevelseq', blank=True)
    class Meta:
        db_table = 'schoolprofilegradex'

class Schooltechedweeks(models.Model):
    schoolprofileseq = models.ForeignKey(Schoolprofile, null=True, db_column='schoolprofileseq', blank=True)
    techedweekseq = models.IntegerField(primary_key=True)
    techedweekdesc = models.CharField(max_length=31L, blank=True)
    cycleweek = models.CharField(max_length=11L, blank=True)
    class Meta:
        db_table = 'schooltechedweeks'

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

class Schooltype(models.Model):
    schooltype = models.CharField(max_length=6L)
    schooltypedescr = models.CharField(max_length=21L, blank=True)
    class Meta:
        db_table = 'schooltype'

class Schoolyear(models.Model):
    schoolyearseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField()
    calendaryearseq = models.IntegerField(null=True, blank=True)
    daysincycle = models.IntegerField(null=True, blank=True)
    numberofperiodsperday = models.IntegerField(null=True, blank=True)
    cycletype = models.CharField(max_length=15L, blank=True)
    periodattendance = models.IntegerField(null=True, blank=True)
    displaymsb = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'schoolyear'

class Schoolyearcycle(models.Model):
    schoolyearseq = models.IntegerField()
    schoolcycleseq = models.ForeignKey(Schoolcycle, null=True, db_column='schoolcycleseq', blank=True)
    schoolprofileseq = models.ForeignKey(Schoolprofile, null=True, db_column='schoolprofileseq', blank=True)
    class Meta:
        db_table = 'schoolyearcycle'

class Schoolyearperiod(models.Model):
    schoolyearseq = models.IntegerField()
    schoolperiodsseq = models.ForeignKey(Schoolperiods, null=True, db_column='schoolperiodsseq', blank=True)
    schoolprofileseq = models.ForeignKey(Schoolprofile, null=True, db_column='schoolprofileseq', blank=True)
    class Meta:
        db_table = 'schoolyearperiod'

class Spedservices(models.Model):
    spedservicesseq = models.IntegerField(primary_key=True)
    spedservicesno = models.CharField(max_length=20L, blank=True)
    servicesvalue = models.CharField(max_length=20L, blank=True)
    class Meta:
        db_table = 'spedservices'

class Spedstatus(models.Model):
    description = models.CharField(max_length=45L, blank=True)
    statecode = models.CharField(max_length=6L, blank=True)
    spedstatuscode = models.CharField(max_length=8L, blank=True)
    spedstatusseq = models.IntegerField(primary_key=True)
    specialneedsflag = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'spedstatus'

class State(models.Model):
    stateabbr = models.CharField(max_length=8L, blank=True)
    statename = models.CharField(max_length=24L, blank=True)
    stateseq = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'state'

class Stuallergy(models.Model):
    stuallergyseq = models.IntegerField(primary_key=True)
    studentid = models.IntegerField()
    allergyseq = models.IntegerField(null=True, blank=True)
    comment_field = models.CharField(max_length=41L, db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    stuallergydate = models.DateField(null=True, blank=True)
    lifethreatening = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stuallergy'

class Stuassignment(models.Model):
    stuassignmentseq = models.IntegerField(primary_key=True)
    assignmentseq = models.IntegerField(null=True, blank=True)
    studentid = models.IntegerField()
    assignmentgradeseq = models.IntegerField(null=True, blank=True)
    dropgrade = models.IntegerField(null=True, blank=True)
    ignoregrade = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stuassignment'

class Stuassignsecavg(models.Model):
    studentid = models.ForeignKey('Student', db_column='studentid')
    schooltermseq = models.IntegerField()
    coursesectionseq = models.ForeignKey(Coursesection, db_column='coursesectionseq')
    possiblepoints = models.IntegerField(null=True, blank=True)
    earnedpoints = models.DecimalField(null=True, max_digits=14, decimal_places=2, blank=True)
    avg_field = models.DecimalField(decimal_places=2, null=True, max_digits=13, db_column='avg_', blank=True) # Field renamed because it ended with '_'.
    assignmenttypeseq = models.IntegerField()
    class Meta:
        db_table = 'stuassignsecavg'

class Stubus(models.Model):
    studentid = models.ForeignKey('Student', db_column='studentid')
    comment_field = models.CharField(max_length=5L, db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    stubusseq = models.IntegerField(primary_key=True)
    busrouteseq = models.IntegerField(null=True, blank=True)
    dayofweek = models.IntegerField(null=True, blank=True)
    schoolhome = models.IntegerField(null=True, blank=True)
    busstopseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stubus'

class Stucreditgpa(models.Model):
    stucreditgpaseq = models.IntegerField(primary_key=True)
    studentid = models.IntegerField(null=True, blank=True)
    createdate = models.DateField(null=True, blank=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)
    termqualitypoints = models.IntegerField(null=True, blank=True)
    termgpa = models.IntegerField(null=True, blank=True)
    termattemptedcredit = models.IntegerField(null=True, blank=True)
    ytdgpa = models.DecimalField(null=True, max_digits=13, decimal_places=3, blank=True)
    careergpa = models.DecimalField(null=True, max_digits=13, decimal_places=3, blank=True)
    ytdrank = models.IntegerField(null=True, blank=True)
    careerrank = models.IntegerField(null=True, blank=True)
    numberofterms = models.IntegerField(null=True, blank=True)
    termrank = models.IntegerField(null=True, blank=True)
    ytdrankoutof = models.IntegerField(null=True, blank=True)
    gpacalcseq = models.IntegerField(null=True, blank=True)
    careerrankoutof = models.IntegerField(null=True, blank=True)
    ytdattemptedcredit = models.DecimalField(null=True, max_digits=13, decimal_places=3, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    careerattemptedcredit = models.DecimalField(null=True, max_digits=13, decimal_places=3, blank=True)
    updatedate = models.DateField(null=True, blank=True)
    ytdqualitypoints = models.DecimalField(null=True, max_digits=14, decimal_places=3, blank=True)
    careerqualitypoints = models.DecimalField(null=True, max_digits=14, decimal_places=3, blank=True)
    deletedflag = models.IntegerField(null=True, blank=True)
    manualinput = models.IntegerField(null=True, blank=True)
    createuser = models.CharField(max_length=19L, blank=True)
    updatetime = models.IntegerField(null=True, blank=True)
    updateuser = models.CharField(max_length=19L, blank=True)
    blankgrades = models.IntegerField(null=True, blank=True)
    excluderank = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stucreditgpa'

class Stucreditoverride(models.Model):
    studentid = models.ForeignKey('Student', db_column='studentid')
    schoolcourseseq = models.ForeignKey(Schoolcourse, db_column='schoolcourseseq')
    departmentseq = models.ForeignKey(Department, db_column='departmentseq')
    credits = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)
    coursesectionseq = models.IntegerField()
    class Meta:
        db_table = 'stucreditoverride'

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

class Studiscipline(models.Model):
    studisciplineseq = models.IntegerField(primary_key=True)
    studentid = models.IntegerField()
    adminactionseq = models.IntegerField(null=True, blank=True)
    offenseseq = models.IntegerField(null=True, blank=True)
    punishmentseq = models.IntegerField(null=True, blank=True)
    parentactionseq = models.IntegerField(null=True, blank=True)
    sturesponseseq = models.IntegerField(null=True, blank=True)
    roomcatalogseq = models.IntegerField(null=True, blank=True)
    punishunitvalue = models.IntegerField(null=True, blank=True)
    printletter = models.IntegerField(null=True, blank=True)
    reportedby = models.IntegerField(null=True, blank=True)
    reportedto = models.IntegerField(null=True, blank=True)
    offensedate = models.DateField(null=True, blank=True)
    offensetime = models.IntegerField(null=True, blank=True)
    period = models.CharField(max_length=6L, blank=True)
    offensecomments = models.TextField(blank=True)
    parentcomments = models.TextField(blank=True)
    studentcomments = models.TextField(blank=True)
    tobeservedstartdate = models.DateField(null=True, blank=True)
    toendserverdate = models.DateField(null=True, blank=True)
    dateservedstart = models.DateField(null=True, blank=True)
    dateservedend = models.DateField(null=True, blank=True)
    actualpunishmentunitvalue = models.IntegerField(null=True, blank=True)
    disciplinestatusseq = models.IntegerField(null=True, blank=True)
    academicyear = models.CharField(max_length=5L, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    punishmentcomments = models.CharField(max_length=5L, blank=True)
    adminactioncomments = models.TextField(blank=True)
    studisciplinepriseq = models.IntegerField(null=True, blank=True)
    reporttodoe = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'studiscipline'

class Studisciplineoffense(models.Model):
    studisciplineseq = models.ForeignKey(Studiscipline, db_column='studisciplineseq')
    offenseseq = models.IntegerField(null=True, blank=True)
    offensenumber = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'studisciplineoffense'

class Studiscpundate(models.Model):
    studisciplineseq = models.ForeignKey(Studiscipline, db_column='studisciplineseq')
    dateserved = models.DateField(null=True, blank=True)
    datetobeserved = models.DateField(null=True, blank=True)
    punishunitvalue = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)
    actualpunishmentunitvalue = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)
    studiscpunishmentseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'studiscpundate'

class Studiscpunishment(models.Model):
    studisciplineseq = models.ForeignKey(Studiscipline, null=True, db_column='studisciplineseq', blank=True)
    offensenumber = models.IntegerField(null=True, blank=True)
    punishmentnumber = models.IntegerField(null=True, blank=True)
    punishmentcomments = models.TextField(blank=True)
    punishmentseq = models.IntegerField(null=True, blank=True)
    punishunitvalue = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)
    dateservedend = models.DateField(null=True, blank=True)
    dateservedstart = models.DateField(null=True, blank=True)
    tobeservedstartdate = models.DateField(null=True, blank=True)
    tobeservedenddate = models.DateField(null=True, blank=True)
    studiscpunishmentseq = models.IntegerField(primary_key=True)
    actualpunishmentunitvalue = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'studiscpunishment'

class Studoefield(models.Model):
    studentid = models.IntegerField()
    doefieldseq = models.IntegerField()
    doefieldvalueseq = models.IntegerField(null=True, blank=True)
    doefieldfreeformvalue = models.CharField(max_length=25L, blank=True)
    class Meta:
        db_table = 'studoefield'

class Stueconomicstatus(models.Model):
    lunchseq = models.IntegerField(null=True, blank=True)
    lowincomeseq = models.ForeignKey(Lowincome, null=True, db_column='lowincomeseq', blank=True)
    studentid = models.IntegerField()
    ridno = models.CharField(max_length=5L, blank=True)
    perkinslowincomeseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stueconomicstatus'

class Stuethnicx(models.Model):
    studentid = models.IntegerField()
    ethnicracecodesseq = models.IntegerField()
    class Meta:
        db_table = 'stuethnicx'

class Stugovtest(models.Model):
    stugovtestseq = models.IntegerField(primary_key=True)
    studentid = models.IntegerField()
    govtestseq = models.IntegerField(null=True, blank=True)
    gradelevelseq = models.IntegerField(null=True, blank=True)
    stugovtestdate = models.DateField(null=True, blank=True)
    createusersid = models.CharField(max_length=18L, blank=True)
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stugovtest'

class Stugovtestattr(models.Model):
    stugovtestseq = models.ForeignKey(Stugovtest, db_column='stugovtestseq')
    govtestattrseq = models.ForeignKey(Govtestattr, db_column='govtestattrseq')
    stugovtestattrvalue = models.CharField(max_length=10L, blank=True)
    govtestscoreseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stugovtestattr'

class Stugradecomment(models.Model):
    stugradecommentseq = models.IntegerField(primary_key=True)
    commentsseq = models.IntegerField(null=True, blank=True)
    stugradesseq = models.IntegerField(null=True, blank=True)
    commentnumber = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stugradecomment'

class Stugradeconduct(models.Model):
    stugradeconductseq = models.IntegerField(primary_key=True)
    conductcodesseq = models.IntegerField(null=True, blank=True)
    stugradesseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stugradeconduct'

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

class Stuhealth(models.Model):
    studentid = models.ForeignKey(Student, db_column='studentid')
    specialinstructions = models.TextField(blank=True)
    createdby = models.CharField(max_length=18L, blank=True)
    createdate = models.DateField(null=True, blank=True)
    modifiedby = models.CharField(max_length=18L, blank=True)
    modifieddate = models.DateField(null=True, blank=True)
    healthinsuranceinfo = models.CharField(max_length=5L, blank=True)
    treatmentapproved = models.IntegerField(null=True, blank=True)
    doctoronfile = models.IntegerField(null=True, blank=True)
    dentistonfile = models.IntegerField(null=True, blank=True)
    historyonfile = models.IntegerField(null=True, blank=True)
    birthcertonfile = models.IntegerField(null=True, blank=True)
    healthwithschool = models.IntegerField(null=True, blank=True)
    healthinsurance = models.IntegerField(null=True, blank=True)
    hospitalcontactseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stuhealth'

class Stuhealthtest(models.Model):
    stuhealthtestseq = models.IntegerField(primary_key=True)
    studentid = models.IntegerField()
    healthtestcodeseq = models.IntegerField(null=True, blank=True)
    lastdate = models.DateField(null=True, blank=True)
    nextdate = models.DateField(null=True, blank=True)
    lastresult = models.TextField(blank=True)
    comment_field = models.TextField(db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    series = models.IntegerField(null=True, blank=True)
    passfail = models.IntegerField(null=True, blank=True)
    referral = models.IntegerField(null=True, blank=True)
    completerefdate = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'stuhealthtest'

class Stuhonorlevel(models.Model):
    studentid = models.ForeignKey(Student, db_column='studentid')
    honorrolllevelseq = models.ForeignKey(Honorrolllevel, db_column='honorrolllevelseq')
    calendaryearseq = models.ForeignKey(Calendaryear, null=True, db_column='calendaryearseq', blank=True)
    schooltermseq = models.ForeignKey(Schoolterm, db_column='schooltermseq')
    gpa = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    average = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stuhonorlevel'

class Stuillness(models.Model):
    stuillnessseq = models.IntegerField(primary_key=True)
    studentid = models.IntegerField()
    illnesscodeseq = models.IntegerField(null=True, blank=True)
    comment_field = models.CharField(max_length=34L, db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    series = models.IntegerField(null=True, blank=True)
    stuillnessdate = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'stuillness'

class Stuimmunization(models.Model):
    stuimmunizationseq = models.IntegerField(primary_key=True)
    studentid = models.IntegerField()
    immunizationcodeseq = models.IntegerField(null=True, blank=True)
    lastdate = models.DateField(null=True, blank=True)
    nextdate = models.DateField(null=True, blank=True)
    comment_field = models.CharField(max_length=5L, db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    exemptcodeseq = models.IntegerField(null=True, blank=True)
    series = models.IntegerField(null=True, blank=True)
    batchnum = models.CharField(max_length=5L, blank=True)
    medicationsourceseq = models.IntegerField(null=True, blank=True)
    admlocation = models.CharField(max_length=5L, blank=True)
    admby = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'stuimmunization'

class Stulanguage(models.Model):
    studentid = models.IntegerField()
    englishprofseq = models.IntegerField(null=True, blank=True)
    bilingualedstatusseq = models.IntegerField(null=True, blank=True)
    eslteacher = models.IntegerField(null=True, blank=True)
    tbeteacher = models.IntegerField(null=True, blank=True)
    tbeorallanguagetestsseq = models.IntegerField(null=True, blank=True)
    tbeorallangtestscore = models.CharField(max_length=8L, blank=True)
    tbeexittypeseq = models.IntegerField(null=True, blank=True)
    tbelasrwreadscore = models.IntegerField(null=True, blank=True)
    tbelasrwwritingscore = models.IntegerField(null=True, blank=True)
    languagecodesseq = models.IntegerField(null=True, blank=True)
    title1teacher = models.IntegerField(null=True, blank=True)
    tbeyearsinprogram = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stulanguage'

class Stulockerx(models.Model):
    studentid = models.ForeignKey(Student, db_column='studentid')
    lockerseq = models.ForeignKey(Locker, db_column='lockerseq')
    class Meta:
        db_table = 'stulockerx'

class Stumedication(models.Model):
    stumedicationseq = models.IntegerField(primary_key=True)
    studentid = models.IntegerField()
    medicationseq = models.IntegerField(null=True, blank=True)
    onhand = models.IntegerField(null=True, blank=True)
    reorder = models.IntegerField(null=True, blank=True)
    quantityperdose = models.DecimalField(null=True, max_digits=9, decimal_places=1, blank=True)
    dose = models.IntegerField(null=True, blank=True)
    strength = models.CharField(max_length=16L, blank=True)
    active = models.IntegerField(null=True, blank=True)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    scheduled = models.IntegerField(null=True, blank=True)
    expirationdate = models.DateField(null=True, blank=True)
    pharmacy = models.CharField(max_length=16L, blank=True)
    doctor = models.CharField(max_length=5L, blank=True)
    comment_field = models.TextField(db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    stumedinfoseq = models.IntegerField(null=True, blank=True)
    dosage = models.CharField(max_length=16L, blank=True)
    parentalapproval = models.IntegerField(null=True, blank=True)
    prn = models.IntegerField(null=True, blank=True)
    quantityonhand = models.DecimalField(null=True, max_digits=10, decimal_places=1, blank=True)
    specialistseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stumedication'

class Stumedicationadm(models.Model):
    stumedicationadmseq = models.IntegerField(primary_key=True)
    stumedicationseq = models.IntegerField(null=True, blank=True)
    admintime = models.IntegerField(null=True, blank=True)
    admindate = models.DateField(null=True, blank=True)
    administered = models.IntegerField(null=True, blank=True)
    comment_field = models.TextField(db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    scheddate = models.DateField(null=True, blank=True)
    schedtime = models.IntegerField(null=True, blank=True)
    personseq = models.IntegerField(null=True, blank=True)
    adminusersid = models.CharField(max_length=12L)
    dosegiven = models.DecimalField(null=True, max_digits=9, decimal_places=1, blank=True)
    class Meta:
        db_table = 'stumedicationadm'

class Stuprischoolyear(models.Model):
    schoolprofileseq = models.IntegerField()
    studentid = models.IntegerField()
    calendaryearseq = models.IntegerField()
    gradelevelseq = models.IntegerField(null=True, blank=True)
    roomcatalogseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stuprischoolyear'

class Sturecrequest(models.Model):
    sturecrequestseq = models.IntegerField(primary_key=True)
    studentid = models.IntegerField(null=True, blank=True)
    schoolcourseseq = models.IntegerField(null=True, blank=True)
    coursesectionseq = models.IntegerField(null=True, blank=True)
    sturecpriseq = models.IntegerField(null=True, blank=True)
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    createuser = models.CharField(max_length=29L, blank=True)
    isalternate = models.IntegerField(null=True, blank=True)
    alternateno = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sturecrequest'

class Sturecrequsersx(models.Model):
    usersid = models.CharField(max_length=29L, blank=True)
    sturecrequestseq = models.IntegerField()
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    comment_field = models.TextField(db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    recstatus = models.CharField(max_length=5L, blank=True)
    fromschoolcourseseq = models.IntegerField(null=True, blank=True)
    fromcoursesectionseq = models.IntegerField(null=True, blank=True)
    studentid = models.ForeignKey(Student, db_column='studentid')
    class Meta:
        db_table = 'sturecrequsersx'

class Sturequest(models.Model):
    studentid = models.ForeignKey(Student, db_column='studentid')
    calendaryearseq = models.ForeignKey(Calendaryear, null=True, db_column='calendaryearseq', blank=True)
    schoolcourseseq = models.IntegerField()
    priority = models.IntegerField(null=True, blank=True)
    isalternate = models.IntegerField(null=True, blank=True)
    prischoolcourseseq = models.IntegerField(null=True, blank=True)
    isscheduled = models.IntegerField(null=True, blank=True)
    alternateno = models.IntegerField(null=True, blank=True)
    islocked = models.IntegerField(null=True, blank=True)
    curriculumlevel = models.IntegerField(null=True, blank=True)
    sturecrequestseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sturequest'

class Sturesponse(models.Model):
    sturesponseseq = models.IntegerField(primary_key=True)
    sturesponsecode = models.CharField(max_length=7L, blank=True)
    sturesponsedescr = models.CharField(max_length=28L, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sturesponse'

class Stuschedhistory(models.Model):
    calendaryearseq = models.ForeignKey(Calendaryear, null=True, db_column='calendaryearseq', blank=True)
    studentid = models.ForeignKey(Student, db_column='studentid')
    schoolcourseseq = models.IntegerField(null=True, blank=True)
    coursesectionseq = models.IntegerField(null=True, blank=True)
    action = models.CharField(max_length=8L, blank=True)
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    usersid = models.ForeignKey('Users', db_column='usersid')
    stuschedhistoryseq = models.IntegerField(primary_key=True)
    schooltermseq = models.IntegerField(null=True, blank=True)
    manual = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stuschedhistory'

class Stuschedule(models.Model):
    schoolcycleseq = models.IntegerField(null=True, blank=True)
    schoolperiodsseq = models.IntegerField(null=True, blank=True)
    schooltermseq = models.ForeignKey(Schoolterm, null=True, db_column='schooltermseq', blank=True)
    studentid = models.ForeignKey(Student, db_column='studentid')
    scheduleseq = models.IntegerField()
    class Meta:
        db_table = 'stuschedule'

class Stuschoolenroll(models.Model):
    schoolprofileseq = models.ForeignKey(Schoolprofile, db_column='schoolprofileseq')
    studentid = models.ForeignKey(Student, db_column='studentid')
    buildingentrydate = models.DateField(null=True, blank=True)
    buildingentryseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stuschoolenroll'

class Stuspecialneeds(models.Model):
    studentid = models.IntegerField()
    specialneedsflag = models.IntegerField(null=True, blank=True)
    spedliaison = models.CharField(max_length=20L, blank=True)
    spedoutplacement = models.CharField(max_length=37L, blank=True)
    spedliaisonseq = models.IntegerField(null=True, blank=True)
    spedtitle1teacher = models.IntegerField(null=True, blank=True)
    spedtransportation = models.CharField(max_length=5L, blank=True)
    spedstatusseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stuspecialneeds'

class Stusuccessassist(models.Model):
    stusuccessplanseq = models.ForeignKey('Stusuccessplan', db_column='stusuccessplanseq')
    successassistoptionseq = models.IntegerField(null=True, blank=True)
    ordernum = models.IntegerField(null=True, blank=True)
    offered = models.IntegerField(null=True, blank=True)
    utilized = models.IntegerField(null=True, blank=True)
    documented = models.IntegerField(null=True, blank=True)
    completed = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stusuccessassist'

class Stusuccessplan(models.Model):
    stusuccessplanseq = models.IntegerField(primary_key=True)
    studentid = models.IntegerField()
    createdate = models.DateField(null=True, blank=True)
    monitorseq = models.IntegerField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    createuser = models.CharField(max_length=14L, blank=True)
    updatedate = models.DateField(null=True, blank=True)
    updatetime = models.IntegerField(null=True, blank=True)
    updateuser = models.CharField(max_length=14L, blank=True)
    contexts = models.CharField(max_length=12L, blank=True)
    updatecount = models.IntegerField(null=True, blank=True)
    datecomplete = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'stusuccessplan'

class Stuteched(models.Model):
    careertechtypeseq = models.ForeignKey(Careertechtype, null=True, db_column='careertechtypeseq', blank=True)
    coopsupervisor = models.CharField(max_length=5L, blank=True)
    coopphoneno = models.CharField(max_length=5L, blank=True)
    employmenttype = models.CharField(max_length=5L, blank=True)
    hourlysalary = models.IntegerField(null=True, blank=True)
    coopplacement = models.CharField(max_length=5L, blank=True)
    coopphoneext = models.CharField(max_length=5L, blank=True)
    physdisadv = models.IntegerField(null=True, blank=True)
    edudisadv = models.IntegerField(null=True, blank=True)
    econdisadv = models.IntegerField(null=True, blank=True)
    coopflag = models.IntegerField(null=True, blank=True)
    studentid = models.IntegerField()
    techedseq = models.IntegerField()
    homeroom = models.IntegerField(null=True, blank=True)
    techedweekseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stuteched'

class Stutermcourse(models.Model):
    studentid = models.ForeignKey(Student, db_column='studentid')
    calendaryearseq = models.ForeignKey(Calendaryear, db_column='calendaryearseq')
    schooltermseq = models.ForeignKey(Schoolterm, db_column='schooltermseq')
    schoolcourseseq = models.ForeignKey(Schoolcourse, db_column='schoolcourseseq')
    coursesectionseq = models.ForeignKey(Coursesection, db_column='coursesectionseq')
    class Meta:
        db_table = 'stutermcourse'

class Stuvisit(models.Model):
    stuvisitseq = models.IntegerField(primary_key=True)
    studentid = models.IntegerField()
    stuvisitdate = models.DateField(null=True, blank=True)
    timein = models.IntegerField(null=True, blank=True)
    timeout = models.IntegerField(null=True, blank=True)
    completed = models.IntegerField(null=True, blank=True)
    series = models.IntegerField(null=True, blank=True)
    schedtime = models.IntegerField(null=True, blank=True)
    comment_field = models.TextField(db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    createpersonseq = models.IntegerField(null=True, blank=True)
    isteacher = models.IntegerField(null=True, blank=True)
    teacherseq = models.IntegerField(null=True, blank=True)
    emergencyref = models.IntegerField(null=True, blank=True)
    called911 = models.IntegerField(null=True, blank=True)
    disposedismissill = models.IntegerField(null=True, blank=True)
    disposedismissinjure = models.IntegerField(null=True, blank=True)
    disposeclass = models.IntegerField(null=True, blank=True)
    disposeother = models.IntegerField(null=True, blank=True)
    hthdispositionseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stuvisit'

class Stuvisitdetail(models.Model):
    stuvisitdetailseq = models.IntegerField(primary_key=True)
    actionseq = models.IntegerField(null=True, blank=True)
    reasonseq = models.IntegerField(null=True, blank=True)
    stuvisitseq = models.IntegerField(null=True, blank=True)
    reasoncomment = models.TextField(blank=True)
    actioncomment = models.TextField(blank=True)
    series = models.IntegerField(null=True, blank=True)
    personseq = models.IntegerField(null=True, blank=True)
    secissue = models.IntegerField(null=True, blank=True)
    interventionseq = models.IntegerField(null=True, blank=True)
    interventioncomment = models.TextField(blank=True)
    stumedicationadmseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'stuvisitdetail'

class Subjectareacourse(models.Model):
    subjectareacourseseq = models.IntegerField(primary_key=True)
    subjectareacoursetitle = models.TextField(blank=True)
    subjectareacoursedescr = models.TextField(blank=True)
    statecode = models.CharField(max_length=11L, blank=True)
    class Meta:
        db_table = 'subjectareacourse'

class Successassistoption(models.Model):
    successassistoptionseq = models.IntegerField(primary_key=True)
    descr = models.CharField(max_length=32L, blank=True)
    name = models.CharField(max_length=32L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    gradelevelseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'successassistoption'

class Successgeneralarea(models.Model):
    successgeneralareaseq = models.IntegerField(primary_key=True)
    successsubjectseq = models.IntegerField(null=True, blank=True)
    descr = models.CharField(max_length=45L, blank=True)
    name = models.CharField(max_length=34L, blank=True)
    displayorder = models.CharField(max_length=8L, blank=True)
    gradelevelseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'successgeneralarea'

class Successspecificarea(models.Model):
    successspecificareaseq = models.IntegerField(primary_key=True)
    successgeneralareaseq = models.IntegerField(null=True, blank=True)
    descr = models.TextField(blank=True)
    name = models.TextField(blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    gradelevelseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'successspecificarea'

class Successsubject(models.Model):
    successsubjectseq = models.IntegerField(primary_key=True)
    descr = models.CharField(max_length=28L, blank=True)
    name = models.CharField(max_length=19L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'successsubject'

class Tabmenu(models.Model):
    tabmenuseq = models.IntegerField(primary_key=True)
    tabmenudescr = models.CharField(max_length=44L, blank=True)
    relatedtabmenu = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'tabmenu'

class Tbeexittype(models.Model):
    tbeexittypeseq = models.IntegerField(primary_key=True)
    tbeexittypecode = models.CharField(max_length=8L, blank=True)
    tbeexitdescr = models.CharField(max_length=28L, blank=True)
    stateabbr = models.CharField(max_length=8L, blank=True)
    class Meta:
        db_table = 'tbeexittype'

class Tbeorallanguagetests(models.Model):
    description = models.TextField(blank=True)
    stateabbr = models.CharField(max_length=15L, blank=True)
    tbeorallanguagetest = models.CharField(max_length=15L, blank=True)
    tbeorallanguagetestsseq = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'tbeorallanguagetests'

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

class Teachercourse(models.Model):
    teacherseq = models.ForeignKey(Teacher, db_column='teacherseq')
    calendaryearseq = models.ForeignKey(Calendaryear, db_column='calendaryearseq')
    schooltermseq = models.ForeignKey(Schoolterm, db_column='schooltermseq')
    schoolcourseseq = models.ForeignKey(Schoolcourse, db_column='schoolcourseseq')
    coursesectionseq = models.ForeignKey(Coursesection, db_column='coursesectionseq')
    class Meta:
        db_table = 'teachercourse'

class Teacherjobtypex(models.Model):
    jobtypescodeseq = models.IntegerField()
    teacherseq = models.ForeignKey(Teacher, db_column='teacherseq')
    schoolprofileseq = models.ForeignKey(Schoolprofile, db_column='schoolprofileseq')
    fet = models.IntegerField(null=True, blank=True)
    islicensed = models.IntegerField(null=True, blank=True)
    ishighqualify = models.IntegerField(null=True, blank=True)
    mainjob = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'teacherjobtypex'

class Teacherperiodsexclude(models.Model):
    calendaryearseq = models.ForeignKey(Calendaryear, null=True, db_column='calendaryearseq', blank=True)
    teacherseq = models.ForeignKey(Teacher, db_column='teacherseq')
    schoolperiodsseq = models.ForeignKey(Schoolperiods, null=True, db_column='schoolperiodsseq', blank=True)
    class Meta:
        db_table = 'teacherperiodsexclude'

class Teacherschedule(models.Model):
    teacherseq = models.ForeignKey(Teacher, db_column='teacherseq')
    scheduleseq = models.ForeignKey(Masterschoolschedule, db_column='scheduleseq')
    class Meta:
        db_table = 'teacherschedule'

class Teacherschoolx(models.Model):
    teacherseq = models.ForeignKey(Teacher, db_column='teacherseq')
    schoolprofileseq = models.ForeignKey(Schoolprofile, db_column='schoolprofileseq')
    class Meta:
        db_table = 'teacherschoolx'

class Teacherstatus(models.Model):
    teacherstatusseq = models.IntegerField(primary_key=True)
    teacherstatusdescr = models.CharField(max_length=24L, blank=True)
    statecode = models.CharField(max_length=7L, blank=True)
    class Meta:
        db_table = 'teacherstatus'

class Teched(models.Model):
    techedseq = models.IntegerField(primary_key=True)
    techedcode = models.CharField(max_length=11L, blank=True)
    techeddescr = models.CharField(max_length=18L, blank=True)
    cipno = models.IntegerField(null=True, blank=True)
    chapter74 = models.IntegerField(null=True, blank=True)
    nontradetype = models.CharField(max_length=5L, blank=True)
    sectechvoc = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'teched'

class Terms(models.Model):
    termseq = models.IntegerField()
    schoolprofileseq = models.ForeignKey(Schoolprofile, null=True, db_column='schoolprofileseq', blank=True)
    termcode = models.CharField(max_length=7L, blank=True)
    termdescr = models.CharField(max_length=18L, blank=True)
    termabbr = models.CharField(max_length=7L, blank=True)
    class Meta:
        db_table = 'terms'

class Textmessage(models.Model):
    textmessageseq = models.IntegerField(primary_key=True)
    textmessagedescr = models.CharField(max_length=49L, blank=True)
    textmessagevalue = models.TextField(blank=True)
    textmessagetype = models.CharField(max_length=11L, blank=True)
    class Meta:
        db_table = 'textmessage'

class Towncodes(models.Model):
    towncode = models.CharField(max_length=8L, blank=True)
    city = models.CharField(max_length=18L, blank=True)
    state = models.CharField(max_length=8L, blank=True)
    zip = models.CharField(max_length=11L, blank=True)
    statetowncode = models.CharField(max_length=8L, blank=True)
    towncodesseq = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'towncodes'

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

class Transcriptcredit(models.Model):
    transcriptseq = models.ForeignKey(Transcript, db_column='transcriptseq')
    departmentname = models.CharField(max_length=51L, blank=True)
    departmentseq = models.ForeignKey(Department, null=True, db_column='departmentseq', blank=True)
    credits = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)
    studentid = models.ForeignKey(Student, null=True, db_column='studentid', blank=True)
    attemptedcredits = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)
    class Meta:
        db_table = 'transcriptcredit'

class Transcriptqp(models.Model):
    transcriptqpseq = models.IntegerField(primary_key=True)
    transcriptseq = models.IntegerField(null=True, blank=True)
    scaleseq = models.IntegerField(null=True, blank=True)
    qualitypoints = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    includeincalc = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'transcriptqp'

class Userdatalabel(models.Model):
    userdatalabelseq = models.IntegerField(primary_key=True)
    tablename = models.CharField(max_length=21L, blank=True)
    userdatalabel = models.CharField(max_length=59L, blank=True)
    userinputtype = models.CharField(max_length=21L, blank=True)
    userinputdatavalues = models.TextField(blank=True)
    userdatafieldsize = models.IntegerField(null=True, blank=True)
    userdatafieldmaxsize = models.IntegerField(null=True, blank=True)
    printontranscript = models.IntegerField(null=True, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)
    userinputdatadisplays = models.TextField(blank=True)
    class Meta:
        db_table = 'userdatalabel'

class Userdatatablex(models.Model):
    tablename = models.CharField(max_length=14L)
    schematable = models.CharField(max_length=5L, blank=True)
    class Meta:
        db_table = 'userdatatablex'

class Userdatavalue(models.Model):
    tablename = models.CharField(max_length=21L)
    userdatalabelseq = models.ForeignKey(Userdatalabel, db_column='userdatalabelseq')
    userdatavalue = models.TextField(blank=True)
    keyvalue = models.CharField(max_length=16L)
    class Meta:
        db_table = 'userdatavalue'

class Userdocuments(models.Model):
    userdocumentsseq = models.IntegerField(primary_key=True)
    usersid = models.CharField(max_length=18L)
    studentid = models.IntegerField(null=True, blank=True)
    publisheddocsseq = models.IntegerField()
    lastused = models.DateField(null=True, blank=True)
    totaldownloads = models.IntegerField(null=True, blank=True)
    filename = models.CharField(max_length=32L, blank=True)
    active = models.IntegerField(null=True, blank=True)
    archived = models.IntegerField(null=True, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    viewed = models.IntegerField(null=True, blank=True)
    filepath = models.CharField(max_length=21L, blank=True)
    comment_field = models.CharField(max_length=5L, db_column='comment_', blank=True) # Field renamed because it ended with '_'.
    personseq = models.IntegerField(null=True, blank=True)
    filesize = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'userdocuments'

class Userfee(models.Model):
    userfeeseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    calendaryearseq = models.IntegerField(null=True, blank=True)
    userfeedescr = models.TextField(blank=True)
    userfeetypeseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'userfee'

class Userfeesched(models.Model):
    userfeeschedseq = models.IntegerField(primary_key=True)
    userfeeseq = models.IntegerField(null=True, blank=True)
    amountdue = models.DecimalField(null=True, max_digits=13, decimal_places=2, blank=True)
    duedate = models.DateField(null=True, blank=True)
    cancelled = models.IntegerField(null=True, blank=True)
    cancelleddate = models.DateField(null=True, blank=True)
    cancelledusersid = models.CharField(max_length=19L)
    class Meta:
        db_table = 'userfeesched'

class Userfeetype(models.Model):
    userfeetypeseq = models.IntegerField(primary_key=True)
    userfeetypedescr = models.CharField(max_length=23L, blank=True)
    class Meta:
        db_table = 'userfeetype'

class Userprofile(models.Model):
    profileseq = models.IntegerField(null=True, blank=True)
    usersid = models.CharField(max_length=47L)
    displayorder = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'userprofile'

class Userreport(models.Model):
    usersid = models.CharField(max_length=24L)
    reportdueseq = models.IntegerField()
    createdate = models.DateField(null=True, blank=True)
    createtime = models.IntegerField(null=True, blank=True)
    userreportname = models.CharField(max_length=59L, blank=True)
    class Meta:
        db_table = 'userreport'

class Userreportfiles(models.Model):
    reportdueseq = models.IntegerField()
    fileno = models.IntegerField()
    filename = models.CharField(max_length=62L, blank=True)
    filetypeseq = models.ForeignKey(Filetype, null=True, db_column='filetypeseq', blank=True)
    publabel = models.CharField(max_length=5L, blank=True)
    published = models.IntegerField(null=True, blank=True)
    pubdate = models.DateField(null=True, blank=True)
    pubtime = models.IntegerField(null=True, blank=True)
    pubreportdueseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'userreportfiles'

class Users(models.Model):
    usersid = models.CharField(max_length=47L, primary_key=True)
    password = models.CharField(max_length=25L)
    email = models.TextField(blank=True)
    personseq = models.IntegerField(null=True, blank=True)
    active = models.IntegerField(null=True, blank=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    sessiontimeout = models.IntegerField(null=True, blank=True)
    pampersionseq = models.IntegerField(null=True, blank=True)
    forcepasswordchange = models.IntegerField(null=True, blank=True)
    lastpasswordchangedate = models.DateField(null=True, blank=True)
    languagecodesseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'users'

class Usersactivity(models.Model):
    usersid = models.CharField(max_length=21L)
    activityseq = models.IntegerField(null=True, blank=True)
    isowner = models.IntegerField(null=True, blank=True)
    canshare = models.IntegerField(null=True, blank=True)
    canupdate = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'usersactivity'

class Userschool(models.Model):
    usersid = models.CharField(max_length=59L)
    schoolprofileseq = models.ForeignKey(Schoolprofile, null=True, db_column='schoolprofileseq', blank=True)
    class Meta:
        db_table = 'userschool'

class Usersparms(models.Model):
    usersid = models.CharField(max_length=29L)
    application = models.CharField(max_length=27L)
    groupname = models.CharField(max_length=41L)
    parmname = models.CharField(max_length=51L)
    parmvalue = models.TextField(blank=True)
    class Meta:
        db_table = 'usersparms'

class Usersteacher(models.Model):
    usersid = models.CharField(max_length=24L)
    teacherseq = models.ForeignKey(Teacher, null=True, db_column='teacherseq', blank=True)
    module = models.CharField(max_length=36L, blank=True)
    class Meta:
        db_table = 'usersteacher'

class Usersusertype(models.Model):
    personseq = models.IntegerField()
    usertypeseq = models.ForeignKey('Usertype', null=True, db_column='usertypeseq', blank=True)
    class Meta:
        db_table = 'usersusertype'

class Usertype(models.Model):
    usertypeseq = models.IntegerField(primary_key=True)
    usertypedescr = models.CharField(max_length=55L, blank=True)
    class Meta:
        db_table = 'usertype'

class Webstate(models.Model):
    sessionid = models.CharField(max_length=42L, blank=True)
    pagename = models.TextField(blank=True)
    dataname = models.CharField(max_length=38L, blank=True)
    datavalue = models.TextField(blank=True)
    delimiters = models.CharField(max_length=6L, blank=True)
    createdate = models.DateField()
    createtime = models.IntegerField()
    class Meta:
        db_table = 'webstate'

