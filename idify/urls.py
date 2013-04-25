from django.conf.urls import patterns, include, url
from hrmstry import views
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
url(r'^$',views.home),
url(r'^login$',views.login),
url(r'^adduser$',views.addusr),
url(r'^useradded$',views.useradd),
url(r'^allusers$',views.all_users_list),
url(r'^userupdate$',views.usrupdate),
url(r'^edituser$',views.usr_edit),
url(r'^empchangepwd$',views.empchangepwd),
url(r'^changepwd$',views.changepwd),
url(r'^pwdprocess$',views.pwdprocess),
url(r'^adminprofile$',views.adminprofile),
url(r'^userprofile$',views.usrprofile),
url(r'^applyforleave$',views.apply_leave),
url(r'^leaveapplied$',views.process_leave),
url(r'^leavesummary$',views.leave_summary),
url(r'^userleave$',views.my_leave),
url(r'^leavedetails$',views.leave_details),
url(r'^admnleavesummary$',views.admnleavesummary),
url(r'^usrs_leaves$',views.admin_usrs_leaves),
url(r'^userleavedetails$',views.userleavedetails),
url(r'^usrleavedetails$',views.admn_usrleave_details),
url(r'^approve$',views.approve),
url(r'^process_approve$',views.processapprove),
url(r'^create_announcement$',views.create_announcement),
url(r'^announcements$',views.watch_announcement),
url(r'^view_announcements$',views.admin_announcement),
url(r'^process_announcement$',views.process_announcement),
url(r'^createproject$',views.createproject),
url(r'^process_project$',views.process_project),
url(r'^allproject$',views.all_project),
url(r'^projectdetails$',views.project_details),
url(r'^myprojects$',views.myprojects),
url(r'^myprojectdetails$',views.myprojectdetails),
url(r'^salary_slip$',views.salaryslip),
url(r'^generate_slip$',views.generate_slip),
url(r'^addcontact$',views.add_contact),
url(r'^process_contact$',views.processcontact),
url(r'^mycontacts$',views.mycontacts),
url(r'^allcontacts$',views.admin_allcontacts),
url(r'^view_contact$',views.view_emp_contact),
url(r'^deletecontact$',views.deletecontact),
url(r'^emp_payroll$',views.adminpayroll),
url(r'^emppayroll_details$',views.emp_payroll_details),
url(r'^payrolldetails$',views.payrolldetails),
url(r'^processsalary$',views.process_salaryslip),
url(r'^logout$',views.logoutusr),
url(r'^upload$',views.upload_doc),
url(r'^savedoc$',views.savedoc),
url(r'^mydocs$',views.mydoc),
url(r'^alldocs$',views.alldocs),
url(r'^viewdocs$',views.viewdocs),

    # Examples:
    # url(r'^$', 'idify.views.home', name='home'),
    # url(r'^idify/', include('idify.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns +=patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
