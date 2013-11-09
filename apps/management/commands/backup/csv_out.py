__author__ = 'Gerard Whittey'
from optparse import make_option
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--action', '-a',
                    action='store',
                    help='the action',
                    dest='action',
                    default=False),
    )
    help = 'valid actions are output which outputs to csv file\n' \
           'more actions...'

    def handle(self, **options):
        from django.template import loader, Context

        def csv_write(my_context, my_csv_output_file):
            handle1 = open(my_csv_output_file, 'w+')
            handle1.write(t.render(my_context))
            handle1.close()
        if options.get('action') == 'output':
            from stu_app.models import Student
            csv_output_file = 'csv_output/csv_student1.txt'
            student_data = Student.objects.all()
            t = loader.get_template('csv_student1_template.txt')
            c = Context({
                'student_data': student_data,
            })
            csv_write(my_context=c, my_csv_output_file=csv_output_file)
            print "OK ran student tab csv output"
        elif options.get('action') == 'teacher_app':
            print 'T'
