from optparse import make_option
from django.core.management.base import BaseCommand
from ...helpers import get_full_address, write_error
from conv.models import Student, Stuethnicx, Addressperson, Phoneperson, Entrywithdrawl, Guardianstudent
import csv


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
            # set CVS out file files
            csv_output_file = 'csv_output/csv_student1.csv'
            print csv_output_file
            csv_header = 'csv_input/csv_student_header.txt'
            header_file = open(csv_header, 'r')
            csv_header = csv.reader(header_file, delimiter=',', quotechar='"')
            header = csv_header.next()
            header_file.close()
            outfile = open(csv_output_file, "wb")
            my_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            my_writer.writerow(header)

            student_data = Student.objects.all()[:100]
            for a_student in student_data:
                #print a_student.studentid
                mother_full_name = ''
                mother_phone_day = ''
                mother_phone_home = ''
                father_full_name = ''
                father_phone_day = ''
                father_phone_home = ''
                a_guardianship = ''
                guardian_fn = ''
                guardian_ln = ''
                a_student_race = ''
                emerg1_contact_name = ''
                emerg1_relationship = ''
                emerg1_phone = ''
                emerg1_ptype = ''
                emerg1_phone_number = ''
                emerg2_contact_name = ''
                emerg2_relationship = ''
                emerg2_phone = ''
                emerg2_ptype = ''
                emerg2_phone_number = ''
                emerg3_contact_name = ''
                emerg3_relationship = ''
                emerg3_phone = ''
                emerg3_ptype = ''
                emerg3_phone_number = ''
                try:
                    a_stuethnicx = Stuethnicx.objects.filter(studentid=a_student.studentid)[
                                   :1].get()  # student ethnicity
                    a_student_race = a_stuethnicx.ethnicracecodesseq.ethniccode
                except Stuethnicx.DoesNotExist:
                    write_error("a_stuethnicx", a_student.studentid)

                    print '*********'
                    print "a_stuethnicx"
                    print a_student.studentid
                    print '*********'
                try:
                    student_address = Addressperson.objects.filter(studentid=a_student.studentid, addresstypeseq=2)[
                                      :1].get()
                except Addressperson.DoesNotExist:
                    write_error("student_address", a_student.studentid)
                    print '*********'
                    print "student_address"
                    print a_student.studentid
                    print '*********'
                try:
                    mailing_address = Addressperson.objects.filter(studentid=a_student.studentid, addresstypeseq=5)[
                                      :1].get()
                except Addressperson.DoesNotExist:
                    write_error("mailing_address", a_student.studentid)
                    print '*********'
                    print 'mailing_address'
                    print a_student.studentid
                    print '*********'
                    # have to join address from iPass address1,address2,address3 to 1 address field for powerschool
                    #mailing_address_street() does this.
                mailing_address_street = get_full_address(mailing_address)
                home_address_street = get_full_address(student_address)
                try:
                    home_phone = Phoneperson.objects.filter(studentid=a_student.studentid, phonetypeseq=1)[:1].get()
                except Phoneperson.DoesNotExist:
                    write_error("home_phone", a_student.studentid)
                    print '*********'
                    print 'home_phone'
                    print a_student.studentid
                    print '*********'
                    # need to add in 'code' for all !---xxxx---! items added in as placeholder
                try:
                    entry_date = Entrywithdrawl.objects.filter(studentid=a_student.studentid) \
                        [:1].get().yearentrydate
                except Entrywithdrawl.DoesNotExist:
                    entry_date = ''
                    write_error("entry_date", a_student.studentid)
                try:
                    a_father = Guardianstudent.objects.filter(studentid=a_student.studentid, relationshipseq=1)[:1].get()
                    father_full_name = a_father.personseq.firstname + ' ' + a_father.personseq.lastname
                    try:
                        father_phone = Phoneperson.objects.filter(personseq=a_father.personseq.personseq)
                        father_phone_day = father_phone.filter(phonetypeseq=2)[:1].get().phoneseq.phoneno
                        father_phone_home = father_phone.filter(phonetypeseq=1)[:1].get().phoneseq.phoneno
                    except Phoneperson.DoesNotExist:
                        write_error("father_phone", a_student.studentid)
                except Guardianstudent.DoesNotExist:
                    write_error("No Father Listed", a_student.studentid)
                try:
                    a_mother = Guardianstudent.objects.filter(studentid=a_student.studentid, relationshipseq=2)[:1].get()
                    mother_full_name = a_mother.personseq.firstname + ' ' + a_mother.personseq.lastname
                    try:
                        mother_phone = Phoneperson.objects.filter(personseq=a_mother.personseq.personseq)
                        mother_phone_day = mother_phone.filter(phonetypeseq=2)[:1].get().phoneseq.phoneno
                        mother_phone_home = mother_phone.filter(phonetypeseq=1)[:1].get().phoneseq.phoneno
                    except Phoneperson.DoesNotExist:
                        write_error('mother_phone', a_student.studentid)
                except Guardianstudent.DoesNotExist:
                    write_error("No Mother Listed", a_student.studentid)
                try:
                    a_guardian = Guardianstudent.objects.filter(studentid=a_student.studentid, relationshipseq=32,
                                                                legalstatusseq=7)[:1].get()
                    a_guardianship = a_guardian.relationshipseq.relationshipdescr
                    guardian_fn = a_guardian.personseq.firstname
                    guardian_ln = a_guardian.personseq.lastname
                except Guardianstudent.DoesNotExist:
                    pass
                try:
                    emerg_contact = Guardianstudent.objects.filter(studentid=a_student.studentid, relationshipseq=37)
                    print len(emerg_contact)
                    if emerg_contact:
                        if emerg_contact[0]:
                            emerg1_contact_name = emerg_contact[0].personseq.firstname + ' ' + emerg_contact[0].personseq.lastname
                            emerg1_relationship = emerg_contact[0].relationshipseq.relationshipdescr
                            try:
                                emerg1_phone = Phoneperson.objects.filter(personseq=emerg_contact[0].personseq.personseq)[:1].get()
                                emerg1_ptype = emerg1_phone.phonetypeseq.phonetypedescr
                                emerg1_phone_number = emerg1_phone.phoneseq.phoneno
                            except Phoneperson.DoesNotExist:
                                pass
                    if len(emerg_contact) > 1:
                        if emerg_contact[1]:
                            emerg2_contact_name = emerg_contact[1].personseq.firstname + ' ' + emerg_contact[1].personseq.lastname
                            emerg2_relationship = emerg_contact[1].relationshipseq.relationshipdescr
                            try:
                                emerg2_phone = Phoneperson.objects.filter(personseq=emerg_contact[1].personseq.personseq)[:1].get()
                                emerg2_ptype = emerg2_phone.phonetypeseq.phonetypedescr
                                emerg2_phone_number = emerg2_phone.phoneseq.phoneno
                            except Phoneperson.DoesNotExist:
                                pass
                    if len(emerg_contact) > 2:
                        if emerg_contact[2]:
                            emerg2_contact_name = emerg_contact[2].personseq.firstname + ' ' + emerg_contact[2].personseq.lastname
                            emerg2_relationship = emerg_contact[2].relationshipseq.relationshipdescr
                            try:
                                emerg3_phone = Phoneperson.objects.filter(personseq=emerg_contact[2].personseq.personseq)[:1].get()
                                emerg3_ptype = emerg3_phone.phonetypeseq.phonetypedescr
                                emerg3_phone_number = emerg3_phone.phoneseq.phoneno
                            except Phoneperson.DoesNotExist:
                                pass
                except Guardianstudent.DoesNotExist:
                    pass
                my_csv_row = [a_student.studentid, "School ID", a_student.personseq.firstname,
                              a_student.personseq.middleinitial, a_student.personseq.lastname, a_student.gradelevel,
                              a_student.gender, a_student_race, a_student.dateofbirth, a_student.ssn, entry_date,
                              "!---Exitdate---!", "!---Enroll Statu---", a_student.gradelevel, "!---Next_School---",
                              "Sched_Scheduled---!", "!---Sched_YearOfGraduation---!", "!---EntryCode---!",
                              "!---TransferComment---!", "!---Districtentrydate---!", "!---Schoolentrydate---!",
                              home_address_street, student_address.addressseq.city, student_address.addressseq.state,
                              student_address.addressseq.zipcode, home_phone.phoneseq.phoneno, "!---Family_Ident---!",
                              mailing_address_street, mailing_address.addressseq.city, mailing_address.addressseq.state,
                              mailing_address.addressseq.zipcode, father_full_name, father_phone_day, father_phone_home,
                              mother_full_name, mother_phone_day, mother_phone_home, a_guardianship, guardian_ln,
                              guardian_fn, emerg1_contact_name, emerg1_relationship, emerg1_ptype, emerg1_phone_number,
                              emerg2_contact_name, emerg2_relationship, emerg2_ptype, emerg2_phone_number,
                              emerg3_contact_name, emerg3_relationship, emerg3_ptype, emerg3_phone_number,
                              a_student.homeroom]
                my_writer.writerow(my_csv_row)
