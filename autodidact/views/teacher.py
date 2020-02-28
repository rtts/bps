from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.contrib.admin.views.decorators import staff_member_required

from autodidact.models import Session, Assignment, Step
from autodidact.views.decorators import needs_course, needs_session, needs_assignment

@staff_member_required
@needs_course
@needs_session
def print_session(request, course, session):
    assignments = session.assignments.filter(active=True).prefetch_related('steps')
    return render(request, 'autodidact/print_session.html', {
        'course': course,
        'session': session,
        'assignments': assignments,
    })

@staff_member_required
@permission_required(['autodidact.add_session'])
@needs_course
def add_session(request, course):
    '''This allows teachers to add new sessions, without being bothered
    to choose a course when using the regular admin:add view

    '''
    session = Session(course=course, active=False)
    session.save()
    return redirect(session)

@staff_member_required
@permission_required(['autodidact.add_assignment'])
@needs_course
@needs_session
def add_assignment(request, course, session):
    '''This allows teachers to add new assignments, without being bothered
    to choose a session when using the regular admin:add view

    '''
    assignment = Assignment(session=session)
    assignment.save()
    return redirect(assignment)

@staff_member_required
@permission_required(['autodidact.add_step', 'autodidact.change_step'])
@needs_course
@needs_session
@needs_assignment
def add_step(request, course, session, assignment):
    '''This allows teachers to add new steps, without being bothered
    to choose a assignment when using the regular admin:add view

    '''
    step = Step(assignment=assignment)
    step.save()
    return HttpResponseRedirect(reverse('admin:autodidact_step_change', args=[step.pk]))
