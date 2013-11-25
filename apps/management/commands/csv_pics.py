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
            csv_output_file = 'csv_output/csv_pic_%s.csv' % datetime.now().strftime(my_format2)
            csv_header = 'csv_input/csv_pic_header.txt'
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
                stu_year = a_student.originalyog
                stu_year = stu_year - 2000
                student_id = a_student.studentid
                student_id2 ="%s.jpg" %  a_student.studentid
                student_pic = ''
                student_pic = "%s%s" % (student_id, stu_year)

                my_csv_row = [student_id2,student_pic ]
                my_writer.writerow(my_csv_row)
                print(datetime.now()-startTime)
