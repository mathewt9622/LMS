from django.contrib import admin




from .models import  Student, Faculty, Course, Department, Assignment, Announcement

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Assignment)
admin.site.register(Announcement)



