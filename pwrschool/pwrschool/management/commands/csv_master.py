from optparse import make_option
from django.core.management.base import BaseCommand
from ...helpers import write_error
from pwrschool.models import Pwrschmaster
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
        if action :
            startTime = datetime.now()
            my_format = "%m%d%y%H%M%S"
            error_file = 'master_sch_error_%s.csv' % datetime.now().strftime(my_format)
            my_format2 = "%m_%d_%y_%H%M"
            # set CVS out file files
            my_termid = action
            csv_output_file = 'csv_output/master_sch/%s_pwrmaster_sch_%s.csv' % (my_termid, datetime.now().strftime(my_format2))
            csv_header = 'csv_input/master_sch_header.txt'
            #use header_file to fill in csv header from csv_header
            header_file = open(csv_header, 'r')
            csv_header = csv.reader(header_file, delimiter=',', quotechar='"')
            header = csv_header.next()
            header_file.close()
            #open csv_output_file
            outfile = open(csv_output_file, "wb")
            my_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            my_writer.writerow(header)
            #get allCourse from course table except
            section_set = Pwrschmaster.objects.distinct('section_number')[:1]
            course_set = Pwrschmaster.objects.distinct('course_number')
            full_set = Pwrschmaster.objects.all()
            #go threw each teacher and gather info
            for a_section in section_set:
                for a_course in course_set:
                    print "section  =%s Course=%s" % (a_section.section_number, a_course.course_number)
                    my_expression = ''
                    new_set = Pwrschmaster.objects.all().filter(
                        course_number=a_course.course_number,
                        section_number=a_section.section_number,
                        termid=my_termid
                    ).order_by('period')
                    if new_set:
                        if new_set.count() <= 3:
                            for i, a_item in enumerate(new_set):
                                if i > 0:
                                    my_expression += ',' + a_item.day
                                else:
                                    my_expression = '%s' % a_item.day
                            total_expression = '%s(%s)' % (new_set[0].period, my_expression)
                        elif new_set.count() > 3:
                            dict_periods = new_set.distinct('period')
                            if new_set.filter(period=dict_periods[0].period).count() == 3:
                                total_expression = '%s(%s,%s,%s)' % (new_set[0].period, new_set[0].day, new_set[1].day, new_set[2].day)
                                total_expression += '%s(%s)' % (new_set[3].period, new_set[3].day)
                            else:
                                total_expression = '%s(%s)' % (new_set[0].period, new_set[0].day)
                                total_expression += '%s(%s,%s,%s)' % (new_set[1].period, new_set[1].day, new_set[2].day, new_set[3].day)

                    if new_set:
                        tmp_item = new_set[0]
                        my_csv_row = [
                            tmp_item.id, tmp_item.course_number, tmp_item.day, tmp_item.period, tmp_item.course_name, tmp_item.section_number, tmp_item.termid,
                            tmp_item.teacher_number, tmp_item.teacher_name, tmp_item.room, total_expression,
                            "!----Attendance_Type_Code----!", "Att_ModeMeeting", tmp_item.schoolid,
                            tmp_item.excludefromclassrank, tmp_item.excludefromgpa, tmp_item.excludefromhonorroll,
                            tmp_item.excludefromstoredgrades, tmp_item.maxenrollment,tmp_item.masterseq
                        ]
                        my_writer.writerow(my_csv_row)
                    else:
                        print "NO"
