from optparse import make_option
from django.core.management.base import BaseCommand
from ...helpers import get_full_address, write_error, find_title
from courses_app.models import  Course, Courseschooltype, Coursesection, Coursetype, \
    Scale, Schoolcourse, Schoolcoursedept, Schoolcoursescale
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
        # this will run the code to process the teacher tab from powerschool
        if action == 'output':
            startTime = datetime.now()
            my_format = "%m%d%y%H%M%S"
            error_file = 'courses_error_%s.csv' % datetime.now().strftime(my_format)
            my_format2 = "%m_%d_%y_%H%M"
            # set CVS out file files
            csv_output_file = 'csv_output/courses/csv_courses_%s.csv' % datetime.now().strftime(my_format2)
            csv_header = 'csv_input/csv_courses_header.txt'
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
            course_set = Course.objects.all()

            #go threw each teacher and gather info
            for counter, a_course in enumerate(course_set):
                print "The Counts is %s of %i" % (counter, len(course_set))
                #"!---Course Number---!"
                course_numbers = a_course.coursetitle
                #"!---Course Name---!"
                course_name = a_course.coursename
                #"!---Credit Hours---!" and
                print a_course.courseseq
                course_credit_hours = ""
                course_grade_scale = ""
                exclude_from_rank = ""
                a_2014_entry= "Yes"
                try:
                    schoolcourse_item = Schoolcourse.objects.get(courseseq=a_course.courseseq, calendaryearseq=16)
                #"!---ExcludeFromClassRank---!"                #"!---ExcludeFromGPA---!"
                    exclude_from = schoolcourse_item.gparank
                    if exclude_from == 0:
                        exclude_from_rank = 1
                        exclude_from_gpa = 1
                    elif exclude_from == 1:
                        exclude_from_gpa = 0
                        exclude_from_rank = 0
                #"!---ExcludeFromGPA---!"

                #"!---ExcludeFromHonorRoll---!"
                    exclude_from_honorroll = schoolcourse_item.honortypeseq
                    if exclude_from_honorroll == 2:
                       exclude_from_honorroll = 0
                    elif exclude_from_honorroll == 3:
                       exclude_from_honorroll = 1

                #"!---ExcludeFromStoredGrades---!"
                    exclude_from_stored_grades = schoolcourse_item.printontranscript
                    if exclude_from_stored_grades == 0:
                        exclude_from_stored_grades = 1
                    elif exclude_from_stored_grades == 1:
                        exclude_from_stored_grades = 0
                    try:
                        schoolcoursedpt_item = Schoolcoursedept.objects.get(
                            schoolcourseseq=schoolcourse_item.schoolcourseseq
                        )
                        course_credit_hours = schoolcoursedpt_item.credits
                    #"!---Sched_Department---!"
                        sched_dept = schoolcoursedpt_item.departmentseq.deptcode
                    except Schoolcoursedept.MultipleObjectsReturned:
                        write_error(error_file, "This item has multiable entries in Schoolcoursedept ", schoolcourse_item.schoolcourseseq)
                    except Schoolcoursedept.DoesNotExist:
                        err_message = "This item schoolcourseseq = %s courseq = %s has no entries in Schoolcoursedept " % (
                            schoolcourse_item.schoolcourseseq, a_course.courseseq
                        )
                        write_error(error_file, err_message, schoolcourse_item.schoolcourseseq)
                    #try:
                    #    course_grade_scale = Schoolcoursescale.objects.get(
                    #        schoolcourseseq=schoolcourse_item.schoolcourseseq
                    #    ).scaleseq
                    #except Schoolcoursescale.DoesNotExist:
                    #    err_message = "courseseq=%s Has No entries for this course in Schoolcoursescale for %s " % (
                    #    a_course.courseseq, schoolcourse_item.schoolcourseseq)
                    #write_error(error_file, err_message, a_course.courseseq)
                except Schoolcoursescale.MultipleObjectsReturned:
                    err_message = "courseseq=%s Has  Multiable for this course in Schoolcoursescale for %s " % (
                        a_course.courseseq, schoolcourse_item.schoolcourseseq)
                    write_error(error_file, err_message, a_course.courseseq)
                except Schoolcourse.DoesNotExist:
                    err_message = "courseseq=%s Has No entries for this course in for cal year seq 16" % a_course.courseseq
                    write_error(error_file, err_message, a_course.courseseq)
                    a_2014_entry = "No"
                except Schoolcourse.MultipleObjectsReturned:
                    err_message = "Course seq=%s has more than one entry in schoolcourse for cal year seq 16" % a_course.courseseq
                    write_error(error_file, err_message, a_course.courseseq)
                    a_2014_entry = "Multi"



                my_csv_row = [
                    course_numbers, course_name, course_credit_hours,
                    course_credit_hours, "!---CreditType---!", "!---GradeScaleID---!",
                    exclude_from_rank, exclude_from_gpa, exclude_from_honorroll,
                   exclude_from_stored_grades, "!---alt_course_number---!", 25,
                    sched_dept, a_2014_entry
                ]

                my_writer.writerow(my_csv_row)