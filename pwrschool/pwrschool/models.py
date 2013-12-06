from django.db import models

# Create your models here.

class Pwrschmaster(models.Model):
    id = models.IntegerField(primary_key=True)
    course_number = models.CharField(max_length=6L, db_column='Course Number', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    course_name = models.CharField(max_length=41L, db_column='Course Name', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    section_number = models.IntegerField(db_column='Section Number', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    termid = models.IntegerField(db_column='TermID', blank=True, null=True) # Field name made lowercase.
    teacher_number = models.CharField(max_length=6L, db_column='Teacher Number', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    teacher_name = models.CharField(max_length=22L, db_column='Teacher Name', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    room = models.CharField(max_length=7L, db_column='Room', blank=True, null=True) # Field name made lowercase.
    expression = models.CharField(max_length=4L, db_column='Expression', blank=True, null=True) # Field name made lowercase.
    attendance_type_code = models.CharField(max_length=30L, db_column='Attendance_Type_Code', blank=True, null=True) # Field name made lowercase.
    att_mode_code = models.CharField(max_length=15L, db_column='Att_Mode_Code', blank=True, null=True) # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolID', blank=True, null=True) # Field name made lowercase.
    excludefromclassrank = models.IntegerField(db_column='ExcludeFromClassRank', blank=True, null=True) # Field name made lowercase.
    excludefromgpa = models.IntegerField(db_column='ExcludeFromGPA', blank=True, null=True) # Field name made lowercase.
    excludefromhonorroll = models.IntegerField(db_column='ExcludeFromHonorRoll', blank=True, null=True) # Field name made lowercase.
    excludefromstoredgrades = models.IntegerField(db_column='ExcludeFromStoredGrades', blank=True, null=True) # Field name made lowercase.
    maxenrollment = models.IntegerField(db_column='MaxEnrollment', blank=True, null=True) # Field name made lowercase.
    masterseq = models.IntegerField(db_column='MasterSEq', blank=True, null=True) # Field name made lowercase.
    day = models.CharField(max_length=1L, blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'Pwrschmaster'
        



class PwrschmasterOrange(models.Model):
    id = models.IntegerField(primary_key=True)
    course_number = models.CharField(max_length=6L, db_column='Course Number', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    course_name = models.CharField(max_length=41L, db_column='Course Name', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    section_number = models.IntegerField(db_column='Section Number', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    termid = models.IntegerField(db_column='TermID', blank=True, null=True) # Field name made lowercase.
    teacher_number = models.CharField(max_length=6L, db_column='Teacher Number', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    teacher_name = models.CharField(max_length=22L, db_column='Teacher Name', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    room = models.CharField(max_length=7L, db_column='Room', blank=True, null=True) # Field name made lowercase.
    expression = models.CharField(max_length=4L, db_column='Expression', blank=True, null=True) # Field name made lowercase.
    attendance_type_code = models.CharField(max_length=30L, db_column='Attendance_Type_Code', blank=True, null=True) # Field name made lowercase.
    att_mode_code = models.CharField(max_length=15L, db_column='Att_Mode_Code', blank=True, null=True) # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolID', blank=True, null=True) # Field name made lowercase.
    excludefromclassrank = models.IntegerField(db_column='ExcludeFromClassRank', blank=True, null=True) # Field name made lowercase.
    excludefromgpa = models.IntegerField(db_column='ExcludeFromGPA', blank=True, null=True) # Field name made lowercase.
    excludefromhonorroll = models.IntegerField(db_column='ExcludeFromHonorRoll', blank=True, null=True) # Field name made lowercase.
    excludefromstoredgrades = models.IntegerField(db_column='ExcludeFromStoredGrades', blank=True, null=True) # Field name made lowercase.
    maxenrollment = models.IntegerField(db_column='MaxEnrollment', blank=True, null=True) # Field name made lowercase.
    masterseq = models.IntegerField(db_column='MasterSEq', blank=True, null=True) # Field name made lowercase.
    day = models.CharField(max_length=1L, blank=True, null=True)
    period = models.CharField(max_length=6L, blank=True, null=True)
    class Meta:
        db_table = 'PwrschmasterOrange'
        

class PwrschmasterBethany(models.Model):
    id = models.IntegerField(primary_key=True)
    course_number = models.CharField(max_length=6L, db_column='Course Number', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    course_name = models.CharField(max_length=41L, db_column='Course Name', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    section_number = models.IntegerField(db_column='Section Number', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    termid = models.IntegerField(db_column='TermID', blank=True, null=True) # Field name made lowercase.
    teacher_number = models.CharField(max_length=6L, db_column='Teacher Number', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    teacher_name = models.CharField(max_length=22L, db_column='Teacher Name', blank=True, null=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    room = models.CharField(max_length=7L, db_column='Room', blank=True, null=True) # Field name made lowercase.
    expression = models.CharField(max_length=4L, db_column='Expression', blank=True, null=True) # Field name made lowercase.
    attendance_type_code = models.CharField(max_length=30L, db_column='Attendance_Type_Code', blank=True, null=True) # Field name made lowercase.
    att_mode_code = models.CharField(max_length=15L, db_column='Att_Mode_Code', blank=True, null=True) # Field name made lowercase.
    schoolid = models.IntegerField(db_column='SchoolID', blank=True, null=True) # Field name made lowercase.
    excludefromclassrank = models.IntegerField(db_column='ExcludeFromClassRank', blank=True, null=True) # Field name made lowercase.
    excludefromgpa = models.IntegerField(db_column='ExcludeFromGPA', blank=True, null=True) # Field name made lowercase.
    excludefromhonorroll = models.IntegerField(db_column='ExcludeFromHonorRoll', blank=True, null=True) # Field name made lowercase.
    excludefromstoredgrades = models.IntegerField(db_column='ExcludeFromStoredGrades', blank=True, null=True) # Field name made lowercase.
    maxenrollment = models.IntegerField(db_column='MaxEnrollment', blank=True, null=True) # Field name made lowercase.
    masterseq = models.IntegerField(db_column='MasterSEq', blank=True, null=True) # Field name made lowercase.
    day = models.CharField(max_length=1L, blank=True, null=True)
    period = models.CharField(max_length=6L, blank=True, null=True)
    
    class Meta:
        db_table = 'PwrschmasterBethany'