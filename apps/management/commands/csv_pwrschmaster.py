from optparse import make_option
from django.core.management.base import BaseCommand
from ...helpers import get_full_address, write_error, find_title
from master_schedule.models import Pwrschmaster
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
            error_file = 'master_sch_error_%s.csv' % datetime.now().strftime(my_format)
            my_format2 = "%m_%d_%y_%H%M"
            # set CVS out file files
            csv_output_file = 'csv_output/master_sch/csv_master_sch_%s.csv' % datetime.now().strftime(my_format2)
            csv_header = 'csv_input/master_sch_header.txt'
            #use header_file to fill in csv header from csv_header
            header_file = open(csv_header, 'r')
            csv_header = csv.reader(header_file, delimiter=',', quotechar='"')
            header = csv_header.next()
            header_file.close()
            #open csv outpu file
            #outfile = open(csv_output_file, "wb")
            #my_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            #my_writer.writerow(header)
            #get all Course from course table except
            pwrmaster_sch_set = Pwrschmaster.objects.all().values_list('course_number', flat=True).distinct()
            #go threw each teacher and gather info
            for counter, a_master_sch_item in enumerate(pwrmaster_sch_set):
                print a_master_sch_item
                new_set = Pwrschmaster.objects.filter(course_number=a_master_sch_item).values_list('period', flat=True).distinct()
                for item in new_set:
                    print item
                print "The Counts is %s of %i" % (counter, len(pwrmaster_sch_set))