from django import forms
from django.db import transaction
from django.conf import settings
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
from .models import UvtUser

class LookupUserForm(forms.Form):
    first_name = forms.CharField(label='First name', required=False, max_length=255)
    last_name = forms.CharField(label='Last name', required=False, max_length=255)
    emplId = forms.CharField(label=mark_safe('<small><code>EmplId</code></small>'), required=False, max_length=255)
    ANR = forms.CharField(label=mark_safe('<small><code>ANR</code></small>'), required=False, max_length=255)
    email = forms.CharField(label='Email address', required=False, max_length=255)
    staff = forms.BooleanField(label='Staff users only', required=False)

    def lookup(self):
        users = UvtUser.objects.filter(
            first_name__icontains=self.cleaned_data['first_name'],
            last_name__icontains=self.cleaned_data['last_name'],
            emplId__icontains=self.cleaned_data['emplId'],
            ANR__icontains=self.cleaned_data['ANR'],
            email__icontains=self.cleaned_data['email'],
        ).order_by('last_name')
        if self.cleaned_data['staff']:
            users = users.filter(user__is_staff=True)
        return users

class ModifyUserForm(forms.Form):
    is_staff = forms.BooleanField(label='Is staff member', required=False)
    groups = forms.ModelMultipleChoiceField(label='Access Levels', queryset=Group.objects.order_by('name'), widget=forms.CheckboxSelectMultiple)

    def save(self, user):
        user.is_staff = self.cleaned_data['is_staff']
        user.save()

        with transaction.atomic():
            user.groups.clear()
            user.groups.add(*self.cleaned_data['groups'])
