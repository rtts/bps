import random
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from autodidact import gift
from autodidact.utils import calculate_progress
from autodidact.models import Tag, CompletedStep
from autodidact.views.decorators import needs_course, needs_session, needs_assignment, needs_step

@login_required
def tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    return render(request, 'autodidact/tag.html', {
        'tag': tag,
    })

@login_required
@needs_course
def course(request, course):
    '''Serves the course overview page
    '''
    return render(request, 'autodidact/course.html', {
        'course': course,
    })

@login_required
@needs_course
@needs_session
def session(request, course, session):
    '''Serves the session overview page
    '''
    assignments = session.assignments.prefetch_related('steps')
    calculate_progress(request.user, assignments)

    return render(request, 'autodidact/session.html', {
        'course': course,
        'session': session,
        'assignments': assignments,
    })

@login_required
@needs_course
@needs_session
@needs_assignment
@needs_step
def assignment(request, course, session, assignment, step):
    '''This view shows the current step of an assignment. Submitted
    answers will always be saved and, if needed, checked for
    correctness.

    '''
    if request.method == 'POST':
        step.given_values = request.POST.getlist('answer')
        concatenated_values = '\x1e'.join(step.given_values)
        if step.completedstep:
            step.completedstep.answer = concatenated_values
        else:
            step.completedstep = CompletedStep(step=step, whom=request.user, answer=concatenated_values)
        if step.graded:
            if step.multiple_choice and step.multiple_answers:
                step.completedstep.passed = gift.all_correct(step.given_values, step.right_values)
            else:
                step.completedstep.passed = gift.any_correct(step.given_values, step.right_values)
        else:
            step.completedstep.passed = True
        step.completedstep.save()

        if 'previous' in request.POST:
            new_step = assignment.steps.filter(number__lt=step.number).last()
        elif 'step' in request.POST:
            new_step = assignment.steps.filter(number=request.POST['step']).first()
        elif 'next' in request.POST:
            new_step = assignment.steps.filter(number__gt=step.number).first()
        else:
            new_step = None

        if 'next' in request.POST and not step.completedstep.passed:
            step.please_try_again = True
        elif new_step:
            new_step.fullscreen = step.fullscreen
            return redirect(new_step)
        else:
            return redirect(session)

    steps = list(assignment.steps.all())
    answered_steps = [c.step for c in request.user.completed.filter(passed=True, step__assignment=assignment).select_related('step')]
    for s in steps:
        s.passed = s in answered_steps
    step.is_first = step == steps[0]
    step.is_last = step == steps[-1]
    step.answers = step.right_values + step.wrong_values
    random.shuffle(step.answers)
    try:
        # Move these answers to the front if they exist
        for val in ['Yes', 'yes', 'True', 'true']:
            step.answers.remove(val)
            step.answers.insert(0, val)
    except ValueError:
        pass

    return render(request, 'autodidact/assignment.html', {
        'course': course,
        'session': session,
        'assignment': assignment,
        'step': step,
        'steps': steps,
    })
