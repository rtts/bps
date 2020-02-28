from __future__ import unicode_literals
import sys
import random
import string
import unicodedata
from django.utils import timezone
from django.core.files.base import ContentFile

HUMAN_FRIENDLY_CHARS = '234679ABCDEFGHJKLMNPRSTUVWXYZabcdefghijkmnpqrstuvwxyz'

def calculate_progress(user, assignments):
    '''Calculate and returns a list of percentages, indicating the user's
    progress in the corresponding assignment. As a side effect, it
    adds a 'progress' attribute to assignment objects and a
    'completedstep' attribute to step objects.

    '''
    progresses = []
    completed = user.completed.select_related('step')

    for ass in assignments:
        if not ass.active:
            continue
        step_count = 0
        completed_count = 0
        for step in ass.steps.all():
            step_count += 1
            for com in completed:
                if step == com.step:
                    if com.passed:
                        completed_count += 1
                    step.completedstep = com
                    step.given_values = com.answer.split('\x1e')
                    break
        ass.progress = int(100 * completed_count/step_count) if step_count else 0
        progresses.append(ass.progress)

    return progresses

def random_string(length):
    '''Generates a random string of human friendly characters

    '''
    return ''.join(random.choice(HUMAN_FRIENDLY_CHARS) for x in range(length))

def clean(dirty_filename):
    '''Cleans dirty filenames

    '''
    valid_chars = '-_.() %s%s' % (string.ascii_letters, string.digits)

    # Replace accented characters with unaccented ones
    normalized_filename = unicodedata.normalize('NFKD', dirty_filename)

    # Strip out all characters that are not in @valid_chars
    cleaned_filename = ''.join([c for c in normalized_filename if c in valid_chars])

    return cleaned_filename

