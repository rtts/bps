# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from uvt_user.utils import search_ldap, LDAPError

def repopulate_user_fields(apps, schema_editor):
    '''
    Repopulate regular user fields with data from Uvt Users.
    '''
    UvtUser = apps.get_model("uvt_user", "UvtUser")

    for uvt_user in UvtUser.objects.all():
        try:
            (
                uvt_user.first_name,
                uvt_user.last_name,
                uvt_user.full_name,
                uvt_user.ANR,
                uvt_user.emplId,
                uvt_user.email
            ) = search_ldap(uvt_user.user.username)
            uvt_user.save()

            uvt_user.user.first_name = uvt_user.first_name
            uvt_user.user.last_name = uvt_user.last_name
            uvt_user.user.email = uvt_user.email
            uvt_user.user.save()
            print('.', end='', flush=True)

        except LDAPError:
            # These x'es are probably unenrolled students
            print('x', end='', flush=True)

def noop(*args):
    return None

class Migration(migrations.Migration):

    dependencies = [
        ('uvt_user', '0004_auto_20170103_1439'),
    ]

    operations = [
        migrations.RunPython(repopulate_user_fields, noop),
    ]
