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

class Entrywithdrawl(models.Model):
    studentid = models.ForeignKey('Student', db_column='studentid')
    entrywithdrawlseq = models.IntegerField(primary_key=True)
    entrywithdrawldate = models.DateField(null=True, blank=True)
    createdate = models.DateField(null=True, blank=True)
    createusersid = models.CharField(max_length=19L, blank=True)
    comment_field = models.CharField(max_length=60L, db_column='comment_',
                                     blank=True)  # Field renamed because it ended with '_'.
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
        managed = False


class Enrollstatus(models.Model):
    enrollstatusseq = models.IntegerField(primary_key=True)
    enrollstatuscode = models.CharField(max_length=6L, blank=True)
    enrollstatusdescr = models.CharField(max_length=16L, blank=True)

    class Meta:
        db_table = 'enrollstatus'
        managed = False

class Entrywithdrawlcodes(models.Model):
    entrywithdrawlcodeseq = models.IntegerField(primary_key=True)
    entrywithdrawlcode = models.CharField(max_length=11L, blank=True)
    entrywithdrawldescr = models.TextField(blank=True)
    statecode = models.CharField(max_length=7L, blank=True)
    enrollstatusseq = models.ForeignKey(Enrollstatus, null=True, db_column='enrollstatusseq', blank=True)
    class Meta:
        db_table = 'entrywithdrawlcodes'
        managed = False

class Ethnicracecodes(models.Model):
    ethniccode = models.CharField(max_length=7L, blank=True)
    description = models.TextField(blank=True)
    statecode = models.CharField(max_length=7L, blank=True)
    ethnicracecodesseq = models.IntegerField(primary_key=True)
    mappingnumber = models.IntegerField(null=True, blank=True)
    show = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'ethnicracecodes'
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

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.firstname + ' ' + self.lastname


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
    disallowedpages = models.CharField(primary_key=True,max_length=5L, blank=True)

    class Meta:
        db_table = 'guardianstudent'
        managed = False

class Legalstatus(models.Model):
    legalstatusseq = models.IntegerField(primary_key=True)
    legalstatusdescr = models.CharField(max_length=31L, blank=True)

    class Meta:
        db_table = 'legalstatus'
        managed = False

class Relationship(models.Model):
    relationshipseq = models.IntegerField(primary_key=True)
    relationshipdescr = models.CharField(max_length=27L, blank=True)

    class Meta:
        db_table = 'relationship'
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


class Stuethnicx(models.Model):
    studentid = models.ForeignKey(Student, primary_key=True, to_field='studentid', db_column='studentid')
    ethnicracecodesseq = models.ForeignKey(Ethnicracecodes, db_column='ethnicracecodesseq')

    class Meta:
        db_table = 'stuethnicx'
        managed = False

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.ethnicracecodesseq


class Stuschoolenroll(models.Model):
    schoolprofileseq = models.ForeignKey(Schoolprofile, db_column='schoolprofileseq')
    studentid = models.ForeignKey(Student, db_column='studentid')
    buildingentrydate = models.DateField(null=True, blank=True)
    buildingentryseq = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'stuschoolenroll'
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
        managed = False
