from optparse import make_option
from django.core.management.base import BaseCommand
from ...helpers import get_full_address, write_error
from stu_app.models import Student, Stuethnicx, Addressperson, Phoneperson, Entrywithdrawl, Guardianstudent, \
    Entrywithdrawlcodes, Stuschoolenroll
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
            course_set = Course.objects.all()
            #go threw each teacher and gather info
            for counter, a_course in enumerate(course_set):
