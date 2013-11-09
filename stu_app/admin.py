__author__ = 'Gerard Whittey'
from django.contrib import admin
from stu_app.models import Person, Student, Addressperson, Address, Addresstype


admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Addressperson)
admin.site.register(Address)
admin.site.register(Addresstype)