from optparse import make_option
from django.core.management.base import BaseCommand
from ...helpers import get_full_address, write_error, find_title
from master_schedule.models import Masterschoolschedule, Course, Teacherschedule, Hrsbio, Roomcatalog, \
                                   Schoolcycle, Schoolperiods, Gradelevel, Terms
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
            outfile = open(csv_output_file, "wb")
            my_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            my_writer.writerow(header)
            #get all Course from course table except
            master_sch_set = Masterschoolschedule.objects.filter(calendaryearseq=16)

            #go threw each teacher and gather info
            for counter, a_master_sch_item in enumerate(master_sch_set):
                room = ""
                teacher_number = ""
                teacher_name = ""
                print "The Counts is %s of %i" % (counter, len(master_sch_set))
            #"!---Course Number---!"
                course_seq = a_master_sch_item.schoolcourseseq.courseseq
                try:
                    ms_course = Course.objects.get(courseseq=course_seq)
                    course_number = ms_course.coursetitle
                    course_name = ms_course.coursename
                except Course.DoesNotExist:
                    err_code = "This schoolcourseseq  %s with schoolcourseseq %s does not match have a course " \
                               "in the course tablet" % \
                               (a_master_sch_item.schoolcourseseq, a_master_sch_item.schoolcourseseq)
                    write_error(err_code, a_master_sch_item.scheduleseq)
            #"!----Section Number----!
                section_number = a_master_sch_item.coursesectionseq.coursesecdesc
            #"!----TermID----!

            #"!----Teacher Number----!", "!----Teacher Name----!"
                try:
                    teacher = Teacherschedule.objects.get(scheduleseq=a_master_sch_item.scheduleseq)
                    teacher_name = "%s %s " % (
                        teacher.teacherseq.personseq.firstname, teacher.teacherseq.personseq.lastname
                    )
                    try:
                        teacher_number  = Hrsbio.objects.get(personseq=teacher.teacherseq.personseq).altempid
                    except Hrsbio.DoesNotExist:
                        write_error(error_file, "Hrsbio:teacher_altempid", teacher.teacherseq)
                except Teacherschedule.DoesNotExist:
                    err_code = "Teacherschedule does not have a %s" % a_master_sch_item.scheduleseq
                    write_error(error_file, err_code, a_master_sch_item.scheduleseq)
                except Teacherschedule.MultipleObjectsReturned:
                    err_code = "MultipleObjectsReturned for %s scheduleseq in Teacherschedule" % \
                               a_master_sch_item.scheduleseq
                    write_error(error_file, err_code, a_master_sch_item.scheduleseq)
            #"!----Room----!
                try:
                    room = Roomcatalog.objects.get(roomcatalogseq=a_master_sch_item.roomcatalogseq).roomcode
                except Roomcatalog.DoesNotExist:
                    err_code = "Had no rooms for scheduleseq = %s" % a_master_sch_item.scheduleseq
                    write_error(err_code, a_master_sch_item.roomcatalogseq)
                except Roomcatalog.MultipleObjectsReturned:
                    err_code = "This scheduleseq = %s returned multiple entries for rooms" % \
                               a_master_sch_item.scheduleseq
                    write_error(error_file, err_code, a_master_sch_item.roomcatalogseq)

            #"!----Expression ----!" (period and day)
                master_sch__day = Schoolcycle.objects.get(
                    schoolcycleseq=a_master_sch_item.schoolcycleseq
                ).daytitleabbr

                master_sch__period  = Schoolperiods.objects.get(
                    schoolperiodsseq=a_master_sch_item.schoolperiodsseq
                ).periodtitleabbr
                expression = "%s(%s)" % (master_sch__period, master_sch__day)
            # "!----SchoolID----!
                school_id = a_master_sch_item.schoolprofileseq.schoolcode
                school_id = "205%s" % school_id

            #"!---ExcludeFromClassRank---!"
                exclude_from_rank = 0
            #"!---ExcludeFromGPA---!"
                exclude_from_gpa =0
            #"!---ExcludeFromHonorRoll---!"
                exclude_from_honorroll = 0
            #"!---ExcludeFromStoredGrades---!"
                exclude_from_stored_grades = 0
            #"!----MaxEnrollment----!"
                max_entrollment = a_master_sch_item.coursesectionseq.maxseats
            #"!----grade_level----!
                try:
                    grade_lvl = Gradelevel.objects.get(gradelevelseq=a_master_sch_item.gradelevelseq).gradelevel
                except Gradelevel.DoesNotExist:
                    err_code = "scheduleseq %s does not have a entry in Gradelevel for gradelevleseq %s" % \
                               (a_master_sch_item.scheduleseq, a_master_sch_item.gradelevelseq)
                    write_error(error_file,err_code, a_master_sch_item.scheduleseq)
            #"!----TermID----!"
                termid = ""
                num_terms  = a_master_sch_item.schoolcourseseq.numofterms
                print school_id
                if school_id == "2056112":
                    if num_terms == 4:
                        termid = "2300"
                    elif num_terms == "1":
                        termid = "It was num of terms =1"
                    elif num_terms == "2":
                        if a_master_sch_item.schooltermseq.termstartdate == 2013-8-13:
                            termid = "2301"
                        elif a_master_sch_item.schooltermseq.termstartdate == 2014-1-26:
                            termid = "2302"

                elif school_id in ("2055212", "2055112"):
                    a_termseq = a_master_sch_item.schooltermseq.termseq
                    try:
                        term_code = Terms.objects.get(termseq=a_termseq).termcode
                    except Terms.DoesNotExist:
                        err_code = "this item has no term entry"
                        write_error(error_file, err_code, a_master_sch_item.scheduleseq)
                    if term_code == "Q1":
                        termid = "2303"
                    elif term_code == "Q2":
                        termid = "2304"
                    elif term_code == "Q3":
                        termid = "2305"
                    elif term_code == "Q4":
                        termid = "2306"
                my_csv_row = [
                    course_number, course_name, section_number, termid,
                    teacher_number, teacher_name, room, expression,
                    "!----Attendance_Type_Code----!", "Att_ModeMeeting", school_id,
                    exclude_from_rank, exclude_from_gpa, exclude_from_honorroll,
                    exclude_from_stored_grades, max_entrollment, grade_lvl, a_master_sch_item.scheduleseq
                ]

                my_writer.writerow(my_csv_row)
                print(datetime.now()-startTime)
            print(datetime.now()-startTime)