__author__ = 'gerardwhittey'
from fabric.api import local, cd


def con_students(my_task):
    code_dir = '/vagrant/'
    with cd(code_dir):
        local("./manage.py " + my_task + "  -a output")

