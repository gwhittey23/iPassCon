from optparse import make_option
from django.core.management.base import BaseCommand
from ...helpers import get_full_address, write_error, find_title
from teacher_app.models import Addressperson, Phoneperson,  Teacherjobtypex, Hrsbio, Roomcatalog

from django.db.models import Q
import csv
from datetime import datetime


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--long', '-l', dest='long',
                    help='Help for the long options'),
        make_option('--action', '-a',
                    action='store',
                    help='the action',
                    dest='action',
                    default=False),
    )
    help = 'valid actions are output which outputs to csv file\n' \
           'more actions....'

    def handle(self, action=None, **options):
        # this will run the code to process the teacher tab from powerschool
        if action == 'output':
            startTime = datetime.now()
            my_format = "%m%d%y%H%M%S"
            error_file = 'teacher_error_%s.csv' % datetime.now().strftime(my_format)
            my_format2 = "%m_%d_%y_%H%M"
            # set CVS out file files
            csv_output_file = 'csv_output/teachers/csv_teacher_%s.csv' % datetime.now().strftime(my_format2)
            csv_header = 'csv_input/csv_teacher_header.txt'
            #use header_file to fill in csv header from csv_header
            header_file = open(csv_header, 'r')
            csv_header = csv.reader(header_file, delimiter=',', quotechar='"')
            header = csv_header.next()
            header_file.close()
            #open csv outpu file
            outfile = open(csv_output_file, "wb")
            my_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            my_writer.writerow(header)
            #get all teachers from teacher table except graldelevel 06
            teacher_data = Teacherjobtypex.objects.exclude(jobtypescodeseq__in=[12, 33, 40])
            #go threw each teacher and gather info
            for counter, a_teacher in enumerate(teacher_data):
                print "The Counts is %s of %i" % (counter, len(teacher_data))
                #"***************TeacherNumber"
                t_altempid = ""
                try:
                    t_altempid = Hrsbio.objects.get(personseq=a_teacher.teacherseq.personseq).altempid
                except Hrsbio.DoesNotExist:
                    write_error(error_file, "Hrsbio:teacher_altempid", a_teacher.teacherseq)
                #"***************SchoolID***************"
                t_schoolID = '205' + a_teacher.schoolprofileseq.schoolcode
                #***************!---Last Name---!", "!---First Name---!","!---Middle_name---!***************"
                t_last_name = a_teacher.teacherseq.personseq.lastname
                t_firstname = a_teacher.teacherseq.personseq.firstname
                t_middlename = a_teacher.teacherseq.personseq.maidenname
                #***************"!---Title---!***************"
                t_title = find_title(a_teacher.teacherseq.personseq.persontitleseq)
                #***************"!---Gender---!***************"
                t_gender = a_teacher.teacherseq.personseq.gender
                if t_gender == 0:
                    t_gender = 'F'
                elif t_gender == 1:
                    t_gender = 'M'
                #***************"!---DOB---!***************"
                t_dob = a_teacher.teacherseq.personseq.dateofbirth
                #***************"!---Email_Addr---!***************"
                t_email = a_teacher.teacherseq.personseq.email
                #***************"!---StaffStatus---!***************"
                t_staff_status = 1
                #"!----Status-----!"
                t_status = a_teacher.teacherseq.teacherstatusseq
                if t_status == 1:
                    t_status = 1
                if t_status == 4:
                    t_status = 4
                #"!---Home Phone---!", "!---School Phone---!"
                t_home_phone = ""
                t_work_phone = ""
                print(a_teacher.teacherseq.personseq.personseq)
                try:
                    phones = Phoneperson.objects.filter(personseq=a_teacher.teacherseq.personseq.personseq)
                    print phones.count()
                    try:
                        t_home_phone = phones.filter(phonetypeseq=1).get().phoneseq.phoneno
                    except Phoneperson.DoesNotExist:
                        write_error(error_file,"Home Phone Look Up Failed", a_teacher.teacherseq.personseq)
                    except Phoneperson.MultipleObjectsReturned:
                        err_code = "This Person has Multiable Phone Listsings phonetypeseq=1"
                        write_error(error_file, err_code, a_teacher.teacherseq.personseq)
                    try:
                        t_work_phone = phones.filter(phonetypeseq=2).get().phoneseq.phoneno
                    except Phoneperson.DoesNotExist:
                        write_error(error_file,"Work Phone Look Up Failed", a_teacher.teacherseq.personseq)
                    except Phoneperson.MultipleObjectsReturned:
                        err_code = "This Person has Multiable Phone Listsings phonetypeseq=2"
                        write_error(error_file, err_code, a_teacher.teacherseq.personseq)

                except Phoneperson.DoesNotExist:
                    write_error(error_file,"Phone Look Up Failed", a_teacher.teacherseq.personseq)
                #"!---SSN---!"
                t_ssn = a_teacher.teacherseq.personseq.ssn
                #need to add in 'code' for all !---xxxx---! items added in as placeholde
                #get address
                try: # see if student is in the addressperson db and pick only student  address type
                    t_address = Addressperson.objects.filter(personseq=a_teacher.teacherseq.personseq, addresstypeseq=2)[
                                      :1].get()
                    t_home_address_street = get_full_address(t_address)
                    t_city = t_address.addressseq.city
                    t_zip = t_address.addressseq.zipcode
                    t_state = t_address.addressseq.state
                except Addressperson.DoesNotExist:
                    write_error(error_file, "Teacher:Addressperson", a_teacher)
                #"!---Homeroom---!"homeroom and look up seq of it in Table Roomcatalog
                home_room = ""
                try:
                    home_room = Roomcatalog.objects.get(roomcatalogseq=a_teacher.teacherseq.homeroom).roomcode
                except Roomcatalog.DoesNotExist:
                    write_error(error_file, "Roomcatalog", a_teacher.teacherseq.teacherseq)
                #"!---Group---!"

                my_csv_row = [
                    t_altempid, t_schoolID, t_last_name, t_firstname, t_middlename,
                    t_title, t_gender, t_dob,
                    "!---Ethnicity---!", t_email,  t_staff_status, t_status,
                    t_home_phone, t_work_phone, t_ssn, t_home_address_street,
                    t_city, t_state, t_zip, home_room, "!---LoginID---!",
                    "!---Password---!", "!---PSaccess---!", "!---Group---!", "!---canchangeschool---!",
                    "!---TeacherLoginid---!", "!---Teacherloginpw---!", "!---Ptaccess---!",
                    "!---sched_scheduled---!"
                ]
                my_writer.writerow(my_csv_row)
