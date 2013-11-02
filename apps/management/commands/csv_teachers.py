__author__ = 'Gerard Whittey'

from optparse import make_option
from django.core.management.base import BaseCommand
import csv


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--action', '-a',
                    action='store',
                    help='the action',
                    dest='action',
                    default=False),
    )
    help = 'valid actions are output which outputs to csv file\n' \
           'more actions...'


    def handle(self, **options):
        #this will run the code to process the student tab from powerschool
        if options.get('action') == 'output':
            csv_output_file = 'csv_output/csv_teacher.txt'
            csv_student_header = 'csv_input/csv_teacher_header.txt'
            header_file = open(csv_student_header, 'r')
            csv_header = csv.reader(header_file,  delimiter=',', quotechar='"')
            header = csv_header.next()
            print header
            header_file.close()
            outfile = open(csv_output_file, "wb" )
            my_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            my_writer.writerow(header)
            #add in db code here
            from conv.models import Teacher
            teacher_data = Teacher.objects.all()
            for a_teacher in teacher_data:
                #need to add in 'code' for all !---xxxx---! items added in as placeholder
                my_csv_row = ["!---TeacherNumber---!", "!---SchoolID---!", "!---Last Name---!", "!---First Name---!",
                              "!---Middle_name---!", "!---Title---!", "!---Gender---!", "!---DOB---!",
                              "!---Ethnicity---!", "!---Email_Addr---!", "!---StaffStatus---!", "!---Status---!",
                              "!---Home Phone---!", "!---School Phone---!", "!---SSN---!", "!---Street---!",
                              "!---City---!", "!---State---!", "!---Zip---!", "!---Homeroom---!", "!---LoginID---!",
                              "!---Password---!", "!---PSaccess---!", "!---Group---!", "!---canchangeschool---!",
                              "!---TeacherLoginid---!", "!---Teacherloginpw---!", "!---Ptaccess---!",
                              "!---sched_scheduled---!"]
                my_writer.writerow(my_csv_row)

