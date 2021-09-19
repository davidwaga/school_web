from django.contrib import admin
# Register your models here.
from classroom.models import *
admin.site.register(Student)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(TakenQuiz)
admin.site.register(Subject)
admin.site.register(Teacher)
from django import forms
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','is_verified')
    list_max_show_all = 10
    #list_editable = ('is_verified',)
    change_list_template = 'admin/school_web/classroom/change_book.html'
    class Meda:
        js = ('/static/admin/school_web/classroom/checkbox.js')

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        
        response.context_data['books_list'] = list(
            qs
            .values('name','is_verified').all()
        )

        return response

    def save_model(self, request, obj, form, change):
        obj.is_verified = False
        super().save_model(request, obj, form, change)

admin.site.register(Book,BookAdmin)