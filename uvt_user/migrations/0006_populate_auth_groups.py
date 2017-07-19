from django.db import migrations
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission

AUTODIDACT_GROUPS = [
    ([
        'change_step',
        'add_rightanswer',
        'change_rightanswer',
        'delete_rightanswer',
        'add_wronganswer',
        'change_wronganswer',
        'delete_wronganswer',
        'add_clarification',
        'change_clarification',
        'delete_clarification',
    ],
     '1. Editor: Edit individual steps, answers, and clarifications'
    ),
    ([
        'add_step',
        'change_step',
        'delete_step',
        'add_assignment',
        'change_assignment',
        'delete_assignment'
    ],
     '2. Creator: Add and remove steps and assignments'
    ),
    ([
        'add_session',
        'change_session',
        'delete_session',
        'add_download',
        'change_download',
        'delete_download'
        'add_presentation',
        'change_presentation',
        'delete_presentation'
    ],
     '3. Master: Edit, add and remove complete sessions'
    ),
]

AUTH_GROUPS = [
    ([
        'change_permission',
    ],
     '4. Administrator: Manage staff members'
    ),
]

def add_groups(apps, schema_editor):
    cts = ContentType.objects.filter(app_label='autodidact')
    for g in AUTODIDACT_GROUPS:
        group, created = Group.objects.get_or_create(name=g[1])
        if created:
            perms = Permission.objects.filter(content_type__in=cts, codename__in=g[0])
            group.permissions.add(*perms)

    cts = ContentType.objects.filter(app_label='auth')
    for g in AUTH_GROUPS:
        group, created = Group.objects.get_or_create(name=g[1])
        if created:
            perms = Permission.objects.filter(content_type__in=cts, codename__in=g[0])
            group.permissions.add(*perms)

class Migration(migrations.Migration):

    dependencies = [
        ('uvt_user', '0005_repopulate_user_fields'),
    ]

    operations = [
        migrations.RunPython(add_groups, migrations.RunPython.noop),
    ]
