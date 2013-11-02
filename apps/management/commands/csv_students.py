from optparse import make_option
from django.core.management.base import BaseCommand
from ...helpers import get_full_address
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
            csv_output_file = 'csv_output/csv_student1.txt'
            print csv_output_file
            csv_header = 'csv_input/csv_student_header.txt'
            header_file = open(csv_header, 'r')
            csv_header = csv.reader(header_file, delimiter=',', quotechar='"')
            header = csv_header.next()
            header_file.close()
            outfile = open(csv_output_file, "wb")
            my_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            my_writer.writerow(header)
            import conv.models
            student_data = conv.models.Student.objects.all()
            for a_student in student_data:
                a_stuethnicx = conv.models.Stuethnicx.objects.get(studentid=a_student.studentid)  # student ethnicity
                student_address = conv.models.Addressperson.objects.get(studentid=a_student.studentid, addresstypeseq=1)
                mailing_address = conv.models.Addressperson.objects.get(studentid=a_student.studentid, addresstypeseq=5)
                # have to join address from iPass address1,address2,address3 to 1 address field for powerschool
                 #mailing_address_street() does this.
                mailing_address_street = get_full_address(mailing_address)
                home_address_street = get_full_address(student_address)
                home_phone = conv.models.Phoneperson.objects.get(studentid=a_student.studentid, phonetypeseq=1)
                # need to add in 'code' for all !---xxxx---! items added in as placeholder
                my_csv_row = [a_student.studentid, a_student.buildingcode, a_student.personseq.firstname,
                              a_student.personseq.middleinitial, a_student.personseq.lastname, a_student.gradelevel,
                              a_student.gender, a_stuethnicx.ethnicracecodesseq.ethniccode, a_student.dateofbirth,
                              a_student.ssn, "!---EntryDate---!", "!---Exitdate---!", "!---Enroll Statu---",
                              a_student.gradelevel, "!---Next_School---", "Sched_Scheduled---!",
                              "!---Sched_YearOfGraduation---!", "!---EntryCode---!", "!---TransferComment---!",
                              "!---Districtentrydate---!", "!---Schoolentrydate---!", home_address_street,
                              student_address.addressseq.city, student_address.addressseq.state,
                              student_address.addressseq.zipcode, home_phone.phoneseq.phoneno, "!---Family_Ident---!",
                              mailing_address_street, mailing_address.addressseq.city, mailing_address.addressseq.state,
                              mailing_address.addressseq.zipcode, "!---Father---!", "!---fatherdayphone---!",
                              "!---Father_home_phone---!", "!---Mother---!", "!---MotherDayPhone---!",
                              "!---Mother_home_phone---!", "!---Guardianship---!", "!---Guardian_ln---!",
                              "!---Guardian_fn---!", "!---Emerg Contact 1---!", "!---Emerg_1_rel---!",
                              "!---Emerg_1_Ptype---!", "!---Emerg Phone 1---!", "!---Emerg Contact 2---!",
                              "!---Emerg_2_rel---!", "!---Emerg_2_Ptype---!", "!---Emerg Phone 2---!",
                              "!---Emerg Contact 3---!", "!---Emerg_3_rel---!", "!---Emerg_3_Ptype---!",
                              "!---Emerg_3_Phone---!", "!---home_room---!"]
                my_writer.writerow(my_csv_row)
