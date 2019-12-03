from django.shortcuts import render
from django.http import HttpResponse
from users.models import Links

def home(request):
    perms = request.user.get_group_permissions()
    group = request.user.groups.all()
    for g in group:
        print(g)
    print("permissions: ")
    for permission in perms:
        print(permission)
    data = {
        'permissions': perms,
        'groups': group,
    }
    return render(request, 'home.html', data)


def login(request):
    return render(request, 'login.html')

def helpdesk(request):
    return HttpResponse('<h1>Help Desk<h1>')

def manageuseraccounts(request):
    return HttpResponse('<h1>Manage User Accounts<h1>')

def assignroles(request):
    return HttpResponse('<h1>Assign Roles<h1>')

def financereports(request):
    return HttpResponse('<h1>Finance Reports<h1>')

def accountspayable(request):
    return HttpResponse('<h1>Accounts Payable<h1>')

def accountsrecievable(request):
    return HttpResponse('<h1>Accounts Receivable<h1>')

def tax(request):
    return HttpResponse('<h1>Tax<h1>')

def salesreport(request):
    return HttpResponse('<h1>Sales Report<h1>')

def salesleads(request):
    return HttpResponse('<h1>Sales Leads<h1>')

def salesdemo(request):
    return HttpResponse('<h1>Sales Demo<h1>')

def newhire(request):
    return HttpResponse('<h1>New Hire<h1>')

def onboarding(request):
    return HttpResponse('<h1>On boarding<h1>')

def benefits(request):
    return HttpResponse('<h1>Benefits<h1>')

def payroll(request):
    return HttpResponse('<h1>Payroll<h1>')

def terminations(request):
    return HttpResponse('<h1>Terminations<h1>')

def hrreports(request):
    return HttpResponse('<h1>Hr Reports<h1>')

def appmonitoring(request):
    return HttpResponse('<h1>App Monitoring<h1>')

def techsupport(request):
    return HttpResponse('<h1>Tech Support<h1>')

def appdev(request):
    return HttpResponse('<h1>App Development<h1>')

def appadmin(request):
    return HttpResponse('<h1>App Admin<h1>')

def releasemanagement(request):
    return HttpResponse('<h1>Release Management<h1>')








