from optparse import make_option
from django.core.management.base import BaseCommand
from ...helpers import get_full_address, write_error, find_title
from historical_grades.models import Stugrades, Grade
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
            error_file = 'historical_grade__error_%s.csv' % datetime.now().strftime(my_format)
            my_format2 = "%m_%d_%y_%H%M"
            # set CVS out file files
            csv_output_file = 'csv_output/historical_grade/csv_historical_grade_%s.csv' % datetime.now().strftime(my_format2)
            csv_header = 'csv_input/historical_grade_header.txt'
            #use header_file to fill in csv header from csv_header
            header_file = open(csv_header, 'r')
            csv_header = csv.reader(header_file, delimiter=',', quotechar='"')
            header = csv_header.next()
            header_file.close()
            #open csv outpu file
            outfile = open(csv_output_file, "wb")
            my_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            my_writer.writerow(header)
            #get all Course from course table except
            historical_grade__set = Stugrades.objects.all().order_by('studentid')

            #go threw each teacher and gather info
            for counter, a_hgrade in enumerate(historical_grade__set):
                print "The Counts is %s of %i" % (counter, len(historical_grade__set))
            #"!----Student_Number----!"
                student_number = a_hgrade.studentid

                my_csv_row = [
                    student_number, "!----Course Name----!", "!----Course Number----!",
                    "!----EarnedCrHrs----!", "!----Grade----!", "!----PotentialCrHrs----!", "!----Storecode----!",
                    "!----Termid----!", "!----GPA points----!", "!----GPA_AddedValue----!", "!----Percent----!",
                    "!----SchoolName----!", "!----Grade_Level----!", "!----Credit Type----!", "!----Teacher Name----!",
                    "!----Schoolid----!", "!----ExcludeFromGPA----!", "!----ExcludeFromClassRank----!",
                    "!----ExcludeFromHonorRoll----!", "!----ExcludeFromTranscripts----!", "!----Replaced_Grade----!"

                ]

                my_writer.writerow(my_csv_row)
                print(datetime.now()-startTime)
