from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')

def helpdesk(request):
    return HttpResponse('<hi>Help Desk<hi>')

def financereports(request):
    return HttpResponse('<hi>Finance Reports<hi>')

def accountspayable(request):
    return HttpResponse('<hi>Accounts Payable<hi>')

def accountsrecievable(request):
    return HttpResponse('<hi>Accounts Receivable<hi>')

def tax(request):
    return HttpResponse('<hi>Tax<hi>')

def salesreport(request):
    return HttpResponse('<hi>Sales Report<hi>')

def salesleads(request):
    return HttpResponse('<hi>Sales Leads<hi>')

def salesdemo(request):
    return HttpResponse('<hi>Sales Demo<hi>')

def newhire(request):
    return HttpResponse('<hi>New Hire<hi>')

def onboarding(request):
    return HttpResponse('<hi>On boarding<hi>')

def benefits(request):
    return HttpResponse('<hi>Benefits<hi>')

def payroll(request):
    return HttpResponse('<hi>Payroll<hi>')

def terminations(request):
    return HttpResponse('<hi>Terminations<hi>')

def hrreports(request):
    return HttpResponse('<hi>Hr Reports<hi>')

def appmonitoring(request):
    return HttpResponse('<hi>App monitoring<hi>')

def techsupport(request):
    return HttpResponse('<hi>Tech Support<hi>')

def appdev(request):
    return HttpResponse('<hi>App Development<hi>')

def appadmin(request):
    return HttpResponse('<hi>App admin<hi>')

def releasemanagement(request):
    return HttpResponse('<hi>Release Management<hi>')








