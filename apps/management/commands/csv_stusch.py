from optparse import make_option
from django.core.management.base import BaseCommand
from ...helpers import get_full_address, write_error, find_title
from student_sch.models import Stuschedule, Schoolterm
from master_schedule.models import Masterschoolschedule, Course,  Schoolprofile

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
            error_file = 'student_sch_error_%s.csv' % datetime.now().strftime(my_format)
            my_format2 = "%m_%d_%y_%H%M"
            # set CVS out file files
            csv_output_file = 'csv_output/student_sch/csv_student_sch_%s.csv' % datetime.now().strftime(my_format2)
            csv_header = 'csv_input/student_sch_header.txt'
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
            student_sch_set = Stuschedule.objects.filter(schooltermseq__range=(93, 105))
            print student_sch_set.count()
            #go threw each teacher and gather info
            for counter, a_student_sch_item in enumerate(student_sch_set):
                print "The Counts is %s of %i" % (counter, len(student_sch_set))
            #"!----SStudent_Number----!
                student_number = a_student_sch_item.studentid.studentid
            #setting up to grab from   Masterschoolschedule table using  a_student_sch_item.scheduleseq
                try:
                    mastersch_item = Masterschoolschedule.objects.get(scheduleseq=a_student_sch_item.scheduleseq)
            # "!----Section_Number----!
                    section_number = mastersch_item.coursesectionseq.coursesecdesc
            #"!----Course_Number----!"#
                    course_seq = mastersch_item.schoolcourseseq.courseseq
                    try:
                        course_number = Course.objects.get(courseseq=course_seq).coursetitle
                    except Course.DoesNotExist:
                        err_code =  "No Course found for courseq = %s for schoolcourseq = %s" % (
                            course_seq, mastersch_item.schoolcourseseq
                        )
                        write_error(error_file, err_code , a_student_sch_item.scheduleseq)
                except Masterschoolschedule.DoesNotExist:
                    err_code = "Item has not entry in Masterschoolschedule for %s" % a_student_sch_item.scheduleseq
                    write_error(error_file, err_code, a_student_sch_item.studentid)

            # "!----Dateenrolled----!""!----DateLeft----!"
                date_enrolled = a_student_sch_item.schooltermseq.termstartdate
                date_left = a_student_sch_item.schooltermseq.termenddate
            #
            # "!----SchoolID----!"
                school_seq = a_student_sch_item.schooltermseq.schoolprofileseq
                try:
                    school_id = Schoolprofile.objects.get(schoolprofileseq=school_seq).schoolcode
                    school_id = "205%s" % (school_id)
                except Schoolprofile.DoesNotExist:
                    err_code = "Schoolprifle not found for %s" % school_seq
                    write_error(error_file, err_code, a_student_sch_item.scheduleseq)
                my_csv_row = [
                    student_number, course_number, section_number,
                    date_enrolled, date_left, "!----Term_Number----!", school_id

                ]
                my_writer.writerow(my_csv_row)
                print(datetime.now()-startTime)
            print(datetime.now()-startTime)