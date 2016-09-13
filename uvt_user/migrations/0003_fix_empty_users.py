# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth.models import User
from uvt_user.utils import search_ldap, LDAPError, strip_initials

def fix_empty_users(apps, schema_editor):
    '''
    Find users without first names and try to repopulate them with LDAP data.
    '''

    UvtUser = apps.get_model("uvt_user", "UvtUser")

    for uvt_user in UvtUser.objects.filter(first_name=''):
        try:
            (
                uvt_user.first_name,
                uvt_user.full_name,
                uvt_user.ANR,
                uvt_user.email
            ) = search_ldap(uvt_user.user.username)
            uvt_user.save()

            uvt_user.user.first_name = uvt_user.first_name
            uvt_user.user.last_name = strip_initials(uvt_user.full_name)
            uvt_user.user.email = uvt_user.email
            uvt_user.user.save()

        except LDAPError:
            pass

def noop(*args):
    return None

class Migration(migrations.Migration):

    dependencies = [
        ('uvt_user', '0002_populate_user_fields'),
    ]

    operations = [
        migrations.RunPython(fix_empty_users, noop),
    ]
