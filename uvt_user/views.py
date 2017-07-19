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
def manage_student(request):
    if request.method == 'POST':
        form = LookupStudentForm(request.POST)
        if form.is_valid():
            students = form.lookup()
            return render(request, 'uvt_user/students.html', {
                'students': students,
            })
    else:
        form = LookupStudentForm()

    return render(request, 'uvt_user/manage_student.html', {
        'form': form,
    })

@staff_member_required
def manage_employee(request):
    if request.method == 'POST':
        form = LookupEmployeeForm(request.POST)
        if form.is_valid():
            employees = form.lookup()
            return render(request, 'uvt_user/employees.html', {
                'employees': employees,
            })
    else:
        form = LookupEmployeeForm()

    return render(request, 'uvt_user/manage_employee.html', {
        'form': form,
    })

@staff_member_required
def student_details(request, username):
    student = get_object_or_404(get_user_model(), username=username)
    return render(request, 'uvt_user/student.html', {
        'student': student,
    })

@staff_member_required
def employee_details(request, username):
    employee = get_object_or_404(get_user_model(), username=username)

    if request.method == 'POST':
        form = ModifyEmployeeForm(request.POST)
        if form.is_valid():
            form.save(employee)
            return redirect('employee_details', username)
    else:
        form = ModifyEmployeeForm(initial={
            'is_staff': employee.is_staff,
            'groups': employee.groups.all()
        })

    return render(request, 'uvt_user/employee.html', {
        'form': form,
        'employee': employee,
    })
