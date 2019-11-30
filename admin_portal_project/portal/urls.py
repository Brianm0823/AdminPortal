from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='portal-home'),
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='portal/logout.html'), name='logout'),
    path('helpdesk/', views.helpdesk, name='helpdesk'),
    path('financereports/', views.financereports, name='financereports'),
    path('accountspayable/', views.accountspayable, name='accountspayable'),
    path('accountsrecieveable/', views.accountsrecievable, name='accountsrecievable'),
    path('tax/', views.tax, name='tax'),
    path('salesreport/', views.salesreport, name='salesreport'),
    path('salesleads/', views.salesleads, name='salesleads'),
    path('salesdemo/', views.salesdemo, name='salesdemo'),
    path('newhire/', views.newhire, name='newhire'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('benefits/', views.benefits, name='benefits'),
    path('payroll/', views.payroll, name='payroll'),
    path('terminations/', views.terminations, name='terminations'),
    path('hrreports/', views.hrreports, name='hrreports'),
    path('appmonitoring/', views.appmonitoring, name='appmonitoring'),
    path('techsupport/', views.techsupport, name='techsupport'),
    path('appdev/', views.appdev, name='appdev'),
    path('appadmin/', views.appadmin, name='appadmin'),
    path('releasemanagement/', views.releasemanagement, name='releasemanagement'),

]