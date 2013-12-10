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
            student_list_file  = open(student_list, 'rU')
            student_csv_read = csv.reader(student_list_file, delimiter=',', quotechar='"')
            startTime = datetime.now()
            my_format = "%m%d%y%H%M%S"
            error_file = 'historical_grades_error_%s.csv' % datetime.now().strftime(my_format)
            my_format2 = "%m_%d_%y_%H%M"
            # set CVS out file files
            csv_output_file = 'csv_output/grades/csv_historical_grades_%s.csv' % datetime.now().strftime(my_format2)
            csv_header = 'csv_input/csv_grades_header.txt'
            #use header_file to fill in csv header from csv_header
            header_file = open(csv_header, 'r')
            csv_header = csv.reader(header_file, delimiter=',', quotechar='"')
            header = csv_header.next()
            header_file.close()
            #open csv output file
            outfile = open(csv_output_file, "wb")
            my_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            my_writer.writerow(header)
            #get all Course from course table excep
            for row in student_csv_read:
                student_list_id = row[0]
                print student_list_id
                try:
                    historical_grade__set = Transcript.objects.filter(
                        studentid=student_list_id[2:]).exclude(schoolprofileseq=0).order_by('studentid'
                        )
                    #go threw each teacher and gather info
                    for counter, a_hgrade in enumerate(historical_grade__set):
                        
                    #"!----Student_Number----!"
                        student_number = a_hgrade.studentid
                    #"!----Course Name----!"
                        course_name = a_hgrade.coursename
                    #!----Course Number----!
                        course_num = a_hgrade.coursetitle
                    #"!----EarnedCrHrs----!", "!----PotentialCrHrs----!""!----Credit Type----!"
                        try:
                            transcript_cridts_item = Transcriptcredit.objects.get(transcriptseq=a_hgrade.transcriptseq)
                            earned_credits = transcript_cridts_item.credits
                            potential_crhrs = transcript_cridts_item.attemptedcredits
                            credit_type = transcript_cridts_item.departmentseq.deptcode
                        except Transcriptcredit.DoesNotExist:
                            err_code = "Item transsciptrsseq = %s does not have a transcriptcredit table entry" % \
                                       a_hgrade.transcriptseq
                            write_error(error_file, err_code, a_hgrade.transcriptseq)
                        except Transcriptcredit.MultipleObjectsReturned:
                            err_code = "This item %s hase multible entries in transcriptcredit"
                            write_error(error_file,err_code,a_hgrade.transcriptseq)

                    #"!----Grade----!"
                        grade = a_hgrade.gradecode
                    #"!----Storecode----!"

                    #"!----SchoolName----!"
                        school_name = a_hgrade.schoolname
                    #"!----Grade_Level----!"
                        try:
                            grade_level = Gradelevel.objects.get(gradelevelseq=a_hgrade.gradelevelseq).gradelevel
                        except Gradelevel.DoesNotExist:
                            err_code = "Gradelevel seq %s not in gradelevel table" % a_hgrade.gradelevelseq
                            write_error(error_file, err_code, a_hgrade.transcriptseq)
                    #"!----Schoolid----!"
                        try:
                            t_school = Schoolprofile.objects.get(schoolprofileseq=a_hgrade.schoolprofileseq)
                            school_id = "205%s" % t_school
                        except Schoolprofile.DoesNotExist:
                            err_code = "School Profile for seq %s does not exist" % a_hgrade.schoolprofileseq
                            write_error(error_file, err_code, a_hgrade.transcriptseq)
                        try:
                            schoolcourse_item = Schoolcourse.objects.get(schoolcourseseq=a_hgrade.schoolcourseseq)
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
                        except Schoolcourse.DoesNotExist:
                            err_code = "No School Course for %s" % a_hgrade.schoolcourseseq
                            write_error(error_file, err_code, a_hgrade.transcriptseq)
                        my_csv_row = [
                            student_list_id, course_name, course_num,
                            earned_credits, grade, potential_crhrs, "!----Storecode----!",
                            "!----Termid----!", "!----GPA points----!", "!----GPA_AddedValue----!", "!----Percent----!",
                            school_name, grade_level, credit_type, "!----Teacher Name----!",
                            school_id, exclude_from_gpa, exclude_from_rank,
                            exclude_from_honorroll, exclude_from_stored_grades, "!----Replaced_Grade----!"

                        ]

                        my_writer.writerow(my_csv_row)
                except Transcript.DoesNotExist:
                     print "CRAPP"