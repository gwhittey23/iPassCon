__author__ = 'Gerard Whittey'

from optparse import make_option
from django.core.management.base import BaseCommand
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
           'more actions...'


    def handle(self, **options):
        #this will run the code to process the student tab from powerschool
        if options.get('action') == 'output':
            csv_output_file = 'csv_output/csv_courses.txt'
            csv_header = 'csv_input/csv_courses_header.txt'
            header_file = open(csv_header, 'r')
            csv_header = csv.reader(header_file,  delimiter=',', quotechar='"')
            header = csv_header.next()
            print header
            header_file.close()
            outfile = open(csv_output_file, "wb" )
            my_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            my_writer.writerow(header)
            #add in db code here
            student_data = ["1", "2"]
            for a_student in student_data:
                #need to add in 'code' for all !---xxxx---! items added in as placeholder
                my_csv_row = ["!---Course Number---!", "!---Course Name---!", "!---Credit Hours---!",
                              "!---MaxCredit---!", "!---CreditType---!", "!---GradeScaleID---!",
                              "!---ExcludeFromClassRank---!", "!---ExcludeFromGPA---!", "!---ExcludeFromHonorRoll---!",
                              "!---ExcludeFromStoredGrades---!", "!---alt_course_number---!", "!---MaxClassSize---!",
                              "!---Sched_Department---!"]
                my_writer.writerow(my_csv_row)


