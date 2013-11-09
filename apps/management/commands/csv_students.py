from optparse import make_option
from django.core.management.base import BaseCommand
from ...helpers import get_full_address, write_error
from stu_app.models import Student, Stuethnicx, Addressperson, Phoneperson, Entrywithdrawl, Guardianstudent, \
    Entrywithdrawlcodes, Stuschoolenroll, Roomcatalog
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
        # this will run the code to process the student tab from powerschool
        if action == 'output':
            startTime = datetime.now()
            my_format = "%m%d%y%H%M%S"
            error_file = 'student_error_%s.csv' % datetime.now().strftime(my_format)
            my_format2 = "%m_%d_%y_%H%M"
            # set CVS out file files
            csv_output_file = 'csv_output/csv_student_%s.csv' % datetime.now().strftime(my_format2)
            csv_header = 'csv_input/csv_student_header.txt'
            #use header_file to fill in csv header from csv_header
            header_file = open(csv_header, 'r')
            csv_header = csv.reader(header_file, delimiter=',', quotechar='"')
            header = csv_header.next()
            header_file.close()
            #open csv outpu file
            outfile = open(csv_output_file, "wb")
            my_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            my_writer.writerow(header)
            #get all students from student table except graldelevel 06
            student_data = Student.objects.all().order_by('studentid')\
                .exclude(gradelevel='06').exclude(deletedflag=1)
            #go threw each student and gather info
            for counter, a_student in enumerate(student_data):
                print "The Counts is %s of %i" % (counter, len(student_data))
                #here we are just setting all values so they will not be used from loop to loop
                sched_scheduled = 0
                mother_full_name, mother_phone_day, mother_phone_home, father_full_name, father_phone_day, \
                    father_phone_home, a_guardianship, guardian_fn, guardian_ln, a_student_race, emerg1_contact_name, \
                    emerg1_relationship, emerg1_phone, emerg1_ptype, emerg1_phone_number, emerg2_contact_name, \
                    emerg2_relationship, emerg2_phone, emerg2_ptype, emerg2_phone_number, emerg3_contact_name, \
                    emerg3_relationship, emerg3_phone, emerg3_ptype, emerg3_phone_number, school_number, enroll_status, \
                    entry_code, entry_sch_date, entry_date, next_school_number, fteid, home_room, exit_date = ('',)*34
                #get student oom because we have to take homeroom and look up seq of it in Table Roomcatalog
                try:
                    home_room = Roomcatalog.objects.get(roomcatalogseq=a_student.homeroom).roomcode
                except Roomcatalog.DoesNotExist:
                    write_error(error_file, "Roomcatalog", a_student.studentid)
                try: # get student race info
                    a_stuethnicx = Stuethnicx.objects.filter(studentid=a_student.studentid)[
                                   :1].get()  # student ethnicity
                    a_student_race_code = a_stuethnicx.ethnicracecodesseq.ethniccode
                    if a_student_race_code == '04':
                        a_student_race = 'W'
                    else:
                        a_student_race = a_student_race_code
                except Stuethnicx.DoesNotExist:
                    write_error(error_file, "Stuethnicx", a_student.studentid)

                try: # see if student is in the addressperson db and pick only student  address type
                    student_address = Addressperson.objects.filter(studentid=a_student.studentid, addresstypeseq=2)[
                                      :1].get()
                except Addressperson.DoesNotExist:
                    write_error(error_file, "student_address:Addressperson", a_student.studentid)

                try: # get student mailing address
                    mailing_address = Addressperson.objects.filter(studentid=a_student.studentid, addresstypeseq=5)[
                                      :1].get()
                except Addressperson.DoesNotExist:
                    write_error(error_file, "mailing_address:Addressperson", a_student.studentid)
                # have to join address from iPass address1,address2,address3 to 1 address field for powerschool
                #mailing_address_street() does this.
                mailing_address_street = get_full_address(mailing_address)
                home_address_street = get_full_address(student_address)

                try:  # get student home phone
                    home_phone = Phoneperson.objects.filter(studentid=a_student.studentid, phonetypeseq=1)[:1].get()
                except Phoneperson.DoesNotExist:
                    write_error(error_file, "home_phone", a_student.studentid)
                try:  # get father info
                    a_father = Guardianstudent.objects.filter(studentid=a_student.studentid, relationshipseq=1)[
                               :1].get()
                    father_full_name = a_father.personseq.firstname + ' ' + a_father.personseq.lastname
                    try:
                        father_phone = Phoneperson.objects.filter(personseq=a_father.personseq.personseq)
                    except Phoneperson.DoesNotExist:
                        write_error(error_file, "father_phone", a_student.studentid)
                    if father_phone:
                        try:
                            father_phone_day = father_phone.filter(phonetypeseq=2)[:1].get().phoneseq.phoneno
                        except Phoneperson.DoesNotExist:
                            write_error(error_file, "father_phone_day", a_student.studentid)
                        try:
                            father_phone_home = father_phone.filter(phonetypeseq=1)[:1].get().phoneseq.phoneno
                        except Phoneperson.DoesNotExist:
                            write_error(error_file, "Father_phone_home", a_student.studentid)
                except Guardianstudent.DoesNotExist:
                    write_error(error_file, "No Father Listed", a_student.studentid)
                try:  # get mother info
                    a_mother = Guardianstudent.objects.filter(studentid=a_student.studentid, relationshipseq=2)[
                               :1].get()
                    mother_full_name = a_mother.personseq.firstname + ' ' + a_mother.personseq.lastname
                    try:
                        mother_phone = Phoneperson.objects.filter(personseq=a_mother.personseq.personseq)
                    except Phoneperson.DoesNotExist:
                        write_error(error_file, 'mother_phone', a_student.studentid)
                    try:
                        mother_phone_day = mother_phone.filter(phonetypeseq=2)[:1].get().phoneseq.phoneno
                    except Phoneperson.DoesNotExist:
                        write_error(error_file, "Mother_phone_home", a_student.studentid)
                    try:
                        mother_phone_home = mother_phone.filter(phonetypeseq=1)[:1].get().phoneseq.phoneno
                    except Phoneperson.DoesNotExist:
                        write_error(error_file, "Mother_phone_home", a_student.studentid)
                except Guardianstudent.DoesNotExist:
                    write_error(error_file, "No Mother Listed", a_student.studentid)

                try:  # get the students guardian contact information
                    a_guardian = Guardianstudent.objects.filter(studentid=a_student.studentid, relationshipseq=32
                                                                )[:1].get()
                    a_guardianship = a_guardian.relationshipseq.relationshipdescr
                    guardian_fn = a_guardian.personseq.firstname
                    guardian_ln = a_guardian.personseq.lastname
                except Guardianstudent.DoesNotExist:
                    pass
                try:  # emergance contacts
                    emerg_contact = Guardianstudent.objects.filter(studentid=a_student.studentid, relationshipseq=37)
                    if emerg_contact:
                        if emerg_contact[0]:
                            emerg1_contact_name = emerg_contact[0].personseq.firstname + ' ' + emerg_contact[
                                0].personseq.lastname
                            emerg1_relationship = emerg_contact[0].relationshipseq.relationshipdescr
                            try:
                                emerg1_phone = Phoneperson.objects.filter(
                                    personseq=emerg_contact[0].personseq.personseq)[:1].get()
                                emerg1_ptype = emerg1_phone.phonetypeseq.phonetypedescr
                                emerg1_phone_number = emerg1_phone.phoneseq.phoneno
                            except Phoneperson.DoesNotExist:
                                pass
                    if len(emerg_contact) > 1:
                        if emerg_contact[1]:
                            emerg2_contact_name = emerg_contact[1].personseq.firstname + ' ' + emerg_contact[
                                1].personseq.lastname
                            emerg2_relationship = emerg_contact[1].relationshipseq.relationshipdescr
                            try:
                                emerg2_phone = Phoneperson.objects.filter(
                                    personseq=emerg_contact[1].personseq.personseq)[:1].get()
                                emerg2_ptype = emerg2_phone.phonetypeseq.phonetypedescr
                                emerg2_phone_number = emerg2_phone.phoneseq.phoneno
                            except Phoneperson.DoesNotExist:
                                pass
                    if len(emerg_contact) > 2:
                        if emerg_contact[2]:
                            emerg2_contact_name = emerg_contact[2].personseq.firstname + ' ' + emerg_contact[
                                2].personseq.lastname
                            emerg2_relationship = emerg_contact[2].relationshipseq.relationshipdescr
                            try:
                                emerg3_phone = Phoneperson.objects.filter(
                                    personseq=emerg_contact[2].personseq.personseq)[:1].get()
                                emerg3_ptype = emerg3_phone.phonetypeseq.phonetypedescr
                                emerg3_phone_number = emerg3_phone.phoneseq.phoneno
                            except Phoneperson.DoesNotExist:
                                pass
                except Guardianstudent.DoesNotExist:
                    pass
                #Getting student school code and next school code
                if a_student.gradelevel in ["12", "11", "10", "09"]:
                    school_number = '2056112'
                    fteid = 2
                    if a_student.gradelevel == '12':
                        next_school_number = '999999'
                    else:
                        next_school_number = '2056112'
                elif a_student.gradelevel in ["07", "08"]:
                    if a_student.gradelevel == "08":#if grade 8 we set next school to highschool code
                        next_school_number = '2056112'
                    try: # see what school middle school is
                        t_school_number = Stuschoolenroll.objects.filter(studentid=a_student.studentid
                          ).order_by('buildingentrydate')[:1].get()
                        if t_school_number.schoolprofileseq.schoolprofileseq == 2:
                            school_number = '2055212'
                            fteid = 4
                        elif t_school_number.schoolprofileseq.schoolprofileseq == 3:
                            school_number = '2055112'
                            fteid = 3
                        else:
                            school_number = '2050000'
                    except Stuschoolenroll.DoesNotExist:
                        write_error(error_file, 'stuschoolenroll', a_student.studentid)
                    if a_student.gradelevel == "07":#if grade 7 we set next school to present school
                        next_school_number = school_number
                elif a_student.gradelevel in ['G10', 'G11', 'G12', 'G13']:
                    school_number = 'Graduated'

                try:

                    district_entry_date = Entrywithdrawl.objects.filter(
                        Q(studentid=a_student.studentid), Q(entrywithdrawlcodeseq=5) | Q(entrywithdrawlcodeseq=6)
                        | Q(entrywithdrawlcodeseq=7) | Q(entrywithdrawlcodeseq=8) | Q(entrywithdrawlcodeseq=9)
                        | Q(entrywithdrawlcodeseq=10) | Q(entrywithdrawlcodeseq=11)
                    )[:1].get().entrywithdrawldate
                except Entrywithdrawl.DoesNotExist:
                     write_error(error_file, 'Entrywithdrawl:district_entry_date', a_student.studentid)
               # for enrollstatus are going to come from entrywithdrawlcodes
                #0 = Active 5-11
                #1 = Inac#tive is 19,20,42,49-55
                #2 = transfered out is 44-48,57
                #3 = gradutated 17
                #we are also getting entry code and entry date from this for all 0-active students
                try:
                    query_set =  Entrywithdrawl.objects.filter(
                        studentid=a_student.studentid
                    ).order_by('-entrywithdrawldate')
                    query_item = query_set[:1].get()
                    if query_item.entrywithdrawlcodeseq in [3, 4, 5, 6, 7, 10, 11]:
                        enroll_status = 0
                        sched_scheduled = 1
                        entry_date = query_item.entrywithdrawldate
                        t_entry_codeseq  = query_item.entrywithdrawlcodeseq
                        entry_code = Entrywithdrawlcodes.objects.get(
                            entrywithdrawlcodeseq=t_entry_codeseq
                        ).entrywithdrawlcode
                    elif query_item.entrywithdrawlcodeseq in [
                       19, 20, 42, 49, 50, 51, 52, 53, 54, 55
                    ]:
                        enroll_status = 1
                    elif query_item.entrywithdrawlcodeseq in [
                        13, 43, 44, 45, 46, 47, 48, 57
                    ]:

                        enroll_status = 2
                    elif query_item.entrywithdrawlcodeseq in [
                        17, 18
                    ]:
                        enroll_status = 3
                except Entrywithdrawl.DoesNotExist:
                    write_error(error_file, 'Entrywithdrawl:enroll_status', a_student.studentid)

                if query_item.entrywithdrawlcodeseq in [
                    13, 17, 18, 19, 20, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 57
                ]:
                    exit_date = query_item.entrywithdrawldate
                    for item in query_set[1:]:
                        if item.entrywithdrawlcodeseq in [3, 5, 6, 7, 10, 11, 56]:
                            entry_date = item.entrywithdrawldate
                            break
                try:
                    t_entry_sch_date = Entrywithdrawl.objects.filter(studentid=a_student.studentid)
                    entrywithdraw_count = t_entry_sch_date.count()
                    if a_student.gradelevel == "12" or "11" or "10" or "09":
                        if 5 >= t_entry_sch_date.count() >= 3:
                            try:
                                entry_sch_date = t_entry_sch_date.get(enrollcounter=3).entrywithdrawldate
                            except Entrywithdrawl.DoesNotExist:
                                write_error(error_file, "Entrywithdrawl:enrollcounter=3", a_student.studentid)
                        elif t_entry_sch_date.count() == 2:
                            try:
                                entry_sch_date = t_entry_sch_date.get(enrollcounter=2).entrywithdrawldate
                            except Entrywithdrawl.DoesNotExist:
                                write_error(error_file, "Entrywithdrawl:enrollcounter=2", a_student.studentid)
                        elif t_entry_sch_date.count() == 1:
                            try:
                                entry_sch_date = t_entry_sch_date.get(enrollcounter=1).entrywithdrawldate
                            except Entrywithdrawl.DoesNotExist:
                                write_error(error_file, "Entrywithdrawl:enrollcounter=1", a_student.studentid)
                        else:
                            entry_sch_date = ' ----school_entry date----'
                    elif a_student.gradelevel == "07" or "08":
                        entry_sch_date = t_entry_sch_date.get(enrollcounter=1).entrywithdrawldate
                except Entrywithdrawl.DoesNotExist:
                    write_error(error_file, "Entrywithdrawl:entry_sch_date", a_student.studentid)
                if a_student.gender == 0:
                    student_gender = 'F'
                elif a_student.gender == 1:
                    student_gender = 'M'
                my_csv_row = [a_student.studentid, school_number, a_student.personseq.firstname,
                          a_student.personseq.middleinitial, a_student.personseq.lastname, a_student.gradelevel,
                          student_gender, a_student_race, a_student.dateofbirth, a_student.ssn, fteid,
                          entry_date, exit_date, enroll_status, next_school_number, sched_scheduled,
                          a_student.originalyog, entry_code, "!---TransferComment---!", district_entry_date,
                          entry_sch_date, home_address_street, student_address.addressseq.city,
                          student_address.addressseq.state, student_address.addressseq.zipcode,
                          home_phone.phoneseq.phoneno, home_phone.phoneseq.phoneno, mailing_address_street,
                          mailing_address.addressseq.city, mailing_address.addressseq.state,
                          mailing_address.addressseq.zipcode, father_full_name, father_phone_day,
                          father_phone_home, mother_full_name, mother_phone_day, mother_phone_home,
                          a_guardianship, guardian_ln, guardian_fn, emerg1_contact_name, emerg1_relationship,
                          emerg1_ptype, emerg1_phone_number, emerg2_contact_name, emerg2_relationship,
                          emerg2_ptype, emerg2_phone_number, emerg3_contact_name, emerg3_relationship,
                          emerg3_ptype, emerg3_phone_number, home_room, entrywithdraw_count]
                my_writer.writerow(my_csv_row)
                print(datetime.now()-startTime)
