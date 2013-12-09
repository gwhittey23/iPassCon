from optparse import make_option
import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from ...helpers import write_error
from historical_grades.models import Transcript, Transcriptcredit, Gradelevel, Schoolprofile, Schoolcourse
from stu_app.models import Student


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
            student_list = 'csv_input/student_list.txt'
            student_list_file  = open(student_list, 'r')
            student_csv_read = csv.reader(student_list_file, delimiter=',', quotechar='"')
            for row in student_csv_read:
                student_list_id = row[0]
                print student_list_id

