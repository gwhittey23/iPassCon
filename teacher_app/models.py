from django.db import models

# Create your models here.


class Address(models.Model):
    addressseq = models.IntegerField(primary_key=True)
    address1 = models.CharField(max_length=40L, blank=True)
    address2 = models.CharField(max_length=44L, blank=True)
    address3 = models.CharField(max_length=5L, blank=True)
    streetno = models.CharField(max_length=32L, blank=True)
    aptno = models.CharField(max_length=33L, blank=True)
    city = models.CharField(max_length=37L, blank=True)
    state = models.CharField(max_length=18L, blank=True)
    zipcode = models.CharField(max_length=18L, blank=True)
    addresstypeseq = models.IntegerField(null=True, blank=True)
    gridcodeseq = models.IntegerField(null=True, blank=True)
    routeno = models.CharField(max_length=5L, blank=True)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'address'
        managed = False

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.address1


class Addressperson(models.Model):
    addressseq = models.ForeignKey('Address', null=True, db_column='addressseq')
    personseq = models.ForeignKey('Person', db_column='personseq')
    addresstypeseq = models.ForeignKey('Addresstype', null=True, db_column='addresstypeseq', blank=True)
    studentid = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'addressperson'
        managed = False


class Addresstype(models.Model):
    addresstypeseq = models.IntegerField(primary_key=True)
    addresstypedescr = models.CharField(max_length=14L, blank=True)
    displayorder = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'addresstype'
        managed = False


class Buildingcodes(models.Model):
    buildingcode = models.CharField(max_length=10L, blank=True)
    description = models.CharField(max_length=24L, blank=True)
    buildingcodesseq = models.IntegerField(primary_key=True)
    schoolprofileseq = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'buildingcodes'
        managed = False


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
        managed = False


class Phoneperson(models.Model):
    phoneseq = models.ForeignKey(Phone, db_column='phoneseq')
    personseq = models.IntegerField(null=True, blank=True)
    studentid = models.IntegerField(primary_key=True)
    rank = models.IntegerField(null=True, blank=True)
    phonetypeseq = models.ForeignKey('Phonetype', null=True, db_column='phonetypeseq', blank=True)

    class Meta:
        db_table = 'phoneperson'
        managed = False


class Phonetype(models.Model):
    phonetypeseq = models.IntegerField(primary_key=True)
    phonetypedescr = models.CharField(max_length=10L, blank=True)

    class Meta:
        db_table = 'phonetype'
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
        managed = False


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


class Teacherjobtypex(models.Model):
    jobtypescodeseq = models.IntegerField()
    teacherseq = models.ForeignKey(Teacher, db_column='teacherseq')
    schoolprofileseq = models.ForeignKey(Schoolprofile, db_column='schoolprofileseq')
    fet = models.IntegerField(primary_key=True, blank=True)
    islicensed = models.IntegerField(null=True, blank=True)
    ishighqualify = models.IntegerField(null=True, blank=True)
    mainjob = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'teacherjobtypex'
