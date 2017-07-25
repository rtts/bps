from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.admin.views.decorators import staff_member_required

from .forms import *

@staff_member_required
def manage(request):
    return render(request, 'uvt_user/manage.html', {
    })

@staff_member_required
def lookup_user(request):
    if request.method == 'POST':
        form = LookupUserForm(request.POST)
        if form.is_valid():
            users = form.lookup()
            return render(request, 'uvt_user/users.html', {
                'users': users,
            })
    else:
        form = LookupUserForm()

    return render(request, 'uvt_user/lookup_user.html', {
        'form': form,
    })

@staff_member_required
def user_details_readonly(request, username):
    user = get_object_or_404(get_user_model(), username=username)

    form = ModifyUserForm(initial={
        'is_staff': user.is_staff,
        'groups': user.groups.all()
    })

    for key in form.fields.keys():
        form.fields[key].disabled = True

    return render(request, 'uvt_user/user.html', {
        'form': form,
        'user': user,
    })

@staff_member_required
@permission_required('auth.change_permission')
def user_details(request, username):
    user = get_object_or_404(get_user_model(), username=username)

    if request.method == 'POST':
        form = ModifyUserForm(request.POST)
        if form.is_valid():
            form.save(user)
            return redirect('user_details', username)
    else:
        form = ModifyUserForm(initial={
            'is_staff': user.is_staff,
            'groups': user.groups.all()
        })

    return render(request, 'uvt_user/user.html', {
        'form': form,
        'user': user,
    })
