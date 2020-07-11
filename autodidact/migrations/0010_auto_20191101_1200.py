from __future__ import unicode_literals
from django.db import migrations
from django.utils.text import slugify

def provide_slug_for_programs(apps, schema_editor):
    Programme = apps.get_model('autodidact', 'Programme')
    for program in Programme.objects.all():
        program.slug = slugify(program.name)
        program.save()

class Migration(migrations.Migration):

    dependencies = [
        ('autodidact', '0009_auto_20191101_1144'),
    ]

    operations = [
        migrations.RunPython(provide_slug_for_programs, migrations.RunPython.noop),
    ]
