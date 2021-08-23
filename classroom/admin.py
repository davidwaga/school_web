from django.contrib import admin
# Register your models here.
from classroom.models import *
admin.site.register(Student)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(TakenQuiz)
admin.site.register(Subject)