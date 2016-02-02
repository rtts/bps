from django.contrib import admin
from django.db import models
from django.forms import RadioSelect
from django.shortcuts import redirect
from .models import *
from adminsortable.admin import SortableAdmin, SortableStackedInline, SortableTabularInline

class FunkySaveAdmin(object):
    '''
    Redirects to the object on site when clicking the save button
    '''
    def response_add(self, request, obj, post_url_continue=None):
        if '_save' in request.POST:
            return redirect(obj.get_absolute_url())
        else:
            return super(FunkySaveAdmin, self).response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        if '_save' in request.POST:
            return redirect(obj.get_absolute_url())
        else:
            return super(FunkySaveAdmin, self).response_change(request, obj)

    save_on_top = True

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    pass

class InlineSessionAdmin(admin.StackedInline):
    model = Session

@admin.register(Course)
class CourseAdmin(FunkySaveAdmin, SortableAdmin):
    inlines = [InlineSessionAdmin]
    list_display = ['__str__', 'name', 'slug', 'url']
    list_filter = ['programmes']
    list_editable = ['name', 'slug']

class InlineAssignmentAdmin(SortableStackedInline):
    model = Assignment
    radio_fields = {'type': admin.HORIZONTAL}

class InlineDownloadAdmin(admin.StackedInline):
    model = Download
    extra = 1

class InlinePresentationAdmin(SortableStackedInline):
    model = Presentation
    extra = 1

@admin.register(Session)
class SessionAdmin(FunkySaveAdmin, SortableAdmin):
    inlines = [InlineDownloadAdmin, InlinePresentationAdmin, InlineAssignmentAdmin]
    list_filter = ['course']
    list_display = ['__str__', 'name', 'course', 'registration_enabled']

class InlineStepAdmin(SortableTabularInline):
    model = Step

@admin.register(Assignment)
class AssignmentAdmin(FunkySaveAdmin, SortableAdmin):
    inlines = [InlineStepAdmin]
    list_display = ['__str__', 'session', 'name', 'nr_of_steps', 'locked']
    list_filter = ['session__course', 'session']
    list_editable = ['name', 'locked']
    radio_fields = {'type': admin.HORIZONTAL}

@admin.register(Step)
class StepAdmin(FunkySaveAdmin, SortableAdmin):
    list_display = ['__str__', 'name', 'description', 'answer_required', 'assignment']
    list_editable = ['answer_required']
    list_filter = ['assignment__session']

@admin.register(CompletedStep)
class CompletedStepAdmin(admin.ModelAdmin):
    list_display = ['whom', 'step', 'date', 'answer']
    list_filter = ['step__assignment__session__course', 'whom']

@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_filter = ['session']
    list_display = ['__str__', 'session']

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_filter = ['session']
    list_display = ['__str__', 'session', 'visibility']
    radio_fields = {'visibility': admin.HORIZONTAL}

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_filter = ['session__course', 'session']
    list_display = ['number', 'session', 'ticket', 'nr_of_students']
