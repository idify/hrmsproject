# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse
from hrmstry.models import employee
from hrmstry.models import leaves
from hrmstry.models import employee_leave
from hrmstry.models import total_leaves
from hrmstry.models import announcement
from hrmstry.models import emp_projects
from hrmstry.models import project_member
from hrmstry.models import emp_payroll
from hrmstry.models import emp_contacts
from hrmstry.models import Document
from hrmstry.forms import DocumentForm
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth import logout
import string
import random
import datetime
from os.path import basename
from urlparse import urlsplit

def id_generator(size=8,chars=string.ascii_lowercase+string.ascii_uppercase+string.digits):
	return ''.join(random.choice(chars) for x in range(size))

def home(request):
	c={}
	c.update(csrf(request))
	return render_to_response('index.html',c,context_instance=RequestContext(request))

def login(request):
	try:
		one=request.POST['uid']
		two=request.POST['pwd']
		p1=employee.objects.get(email=one,passwd=two)
	except employee.DoesNotExist:
		c={'msg':'Invalid Username/Password.'}
		c.update(csrf(request))
		return render_to_response('index.html',c,context_instance=RequestContext(request))
	else:
		if p1.is_admin==1:
			return adminlogin(request,p1)		
		else:
			return usrlogin(request,p1)

def adminlogin(request,usr):
	request.session['member_id']=usr.usr_id
	return adminlogindone(request)

def adminlogindone(request):
	uid=request.session['member_id']
	obj=employee.objects.get(usr_id=uid)
	if obj.gender=='female':
		user_name='Ms. '+obj.f_name+' '+obj.l_name
	else:
		user_name='Mr. '+obj.f_name+' '+obj.l_name
	return render_to_response('admin_profile.html',{'obj':obj,'name':user_name},context_instance=RequestContext(request))

def adminprofile(request):
	a=''
	uid=request.session['member_id']
	usr=employee.objects.get(usr_id=request.session['member_id'])
	if usr.gender=='female':
		admin_name='Ms. '+usr.f_name+' '+usr.l_name
	else:
		admin_name='Mr. '+usr.f_name+' '+usr.l_name
	return render_to_response('loggedin.html',{'msg':a,'urid':uid,'name':admin_name,'fname':usr.f_name,'lname':usr.l_name,'emailid':usr.email,'doj':usr.doj,'cont':usr.contact,'add':usr.address},context_instance=RequestContext(request))

def usrlogin(request,usr):
	request.session['member_id']=usr.usr_id
	return usrprofile(request)

def usrprofile(request):
	uid=request.session['member_id']
	usr=employee.objects.get(usr_id=uid)
	if usr.gender=='female':
		user_name='Ms. '+usr.f_name+' '+usr.l_name
	else:
		user_name='Mr. '+usr.f_name+' '+usr.l_name
	return render_to_response('usrlogin.html',{'name':user_name,'obj':usr},context_instance=RequestContext(request))

def logoutusr(request):
	try:
		del request.session['member_id']
	except KeyError:
		return render_to_response('index.html',{'msg':'You have been logged out'},context_instance=RequestContext(request))
	return render_to_response('index.html',{'msg':'Logged out Successfully.'},context_instance=RequestContext(request))

def usr_edit(request):
	eid=request.session['member_id']
	obj=employee.objects.get(usr_id=eid)
	return render_to_response('edituser.html',{'obj':obj},context_instance=RequestContext(request))

def usrupdate(request):
	original_id=request.session['member_id']
	fn=request.GET['fname']
	ln=request.GET['lname']
	mar=request.GET['mstatus']
	cntct=request.GET['contact']
	ad=request.GET['address']
	record=employee.objects.get(usr_id=original_id)
	record.f_name=fn
	record.l_name=ln
	record.marr_status=mar
	record.contact=cntct
	record.address=ad
	record.save()
	a='Your profile has been Updated'
	obj1=employee.objects.get(usr_id=original_id)
	return render_to_response('edituser.html',{'obj':obj1,'msg':a},context_instance=RequestContext(request))

def empchangepwd(request):
	c={}
	c.update(csrf(request))
	return render_to_response('empchangepwd.html',c,context_instance=RequestContext(request))

def changepwd(request):
	c={}
	c.update(csrf(request))
	return render_to_response('changepwd.html',c,context_instance=RequestContext(request))

def pwdprocess(request):
	usrid=request.session['member_id']
	oldpwd=request.POST['opwd']
	obj=employee.objects.get(usr_id=usrid)
	if (obj.passwd)==oldpwd:
		obj.passwd=request.POST['pwd1']
		obj.save()
		msg='Password has been changed Successfully'
	else:
		msg='Incorrect Old Password'
	if usrid==1:
		return render_to_response('changepwd.html',{'msg':msg},context_instance=RequestContext(request))
	else:
		return render_to_response('empchangepwd.html',{'msg':msg},context_instance=RequestContext(request))

#	Admin wants to add an employee.

def addusr(request):
	eid=request.session['member_id']
	if eid==1:
		return render_to_response('adduser.html',{'msg':''},context_instance=RequestContext(request))
	else:
		return HttpResponse('Only Admin can view this page.')

def useradd(request):
	a='User has been added successfully.'
	paswd=id_generator()
	fname=request.GET['fname']
	lname=request.GET['lname']
	mailid=request.GET['mail']
	desgn=request.GET['desg']
	s=request.GET['sal']
	dtoj=request.GET['doj']	
	cntct=request.GET['contact']
	p1=employee.objects.create(passwd=paswd,f_name=fname,l_name=lname,email=mailid,desg=desgn,salary=s,doj=dtoj,contact=cntct,is_admin=0)
	p2=employee_leave.objects.create(usr_id=p1.usr_id,rhl=0,rh_available=3,rh_add=0,prsnl=0,prsnl_available=3,prsnl_add=0,csul=0,csul_available=10,csul_add=0,mrrgl=0,mrrg_available=15,mrrg_add=0,bvrmntl=0,bvrmnt_available=3,bvrmnt_add=0,compl=0,comp_available=6,comp_add=0)
	sub='Welcome to IDiFY Solutions'
	msg='Welcome to IDiFY Solutions. You have been registered to IDiFY Solutions.\nYou login credentials are:\n\nID:'+mailid+'\nPassword:'+paswd+'\n\nRegards,\nIDiFY Solutions'
	frm='sturload@gmail.com'
	send_mail(sub,msg,frm,[mailid],fail_silently=False)
	return render_to_response('adduser.html',{'msg':a},context_instance=RequestContext(request))

#	Admin can view all employees list.

def all_users_list(request):
	eid=request.session['member_id']
	if eid==1:
		try:
			obj=employee.objects.get(~Q(usr_id=1))
		except employee.DoesNotExist:
			return render_to_response('users_list.html',{'msg':'No Employees'},context_instance=RequestContext(request))
		else:
			return render_to_response('users_list.html',{'obj':employee.objects.filter(~Q(usr_id=1))},context_instance=RequestContext(request))
	else:
		return HttpResponse('Only Admin can view this page.')

#	Employee can Apply for leave.

def apply_leave(request):
	return render_to_response('apply_leave.html',context_instance=RequestContext(request))

def process_leave(request):
	usrid=request.session['member_id']
	obj=employee_leave.objects.get(usr_id=usrid)
	useraddedon=obj.emp_added
	now=datetime.datetime.now()
	months=now.month-useraddedon.month

#    Updating every month leaves in the database for employee.

	if months>0:
		for x in range(0,months):
			rhadd=rhadd+3.0/10
			prsnladd=prsnladd+3.0/10
			csualadd=csuladd+10/10
			mrrgadd=mrrgadd+15.0/10
			bvrmntadd=bvrmntadd+3.0/10
			compadd=compadd+6.0/10
		employee.objects.filter(usr_id=usrid).update(rh_add=rh_add+rhadd,prsnl_add=prsnl_add+prsnladd,csul_add=csul_add+csuladd,mrrg_add=mrrg_add+mrrgadd,bvrmnt_add=bvrmnt_add+bvrmntadd,comp_add=comp_add+compadd,emp_added=now.date())

#    Updating every year available leaves+additional leaves(every month) in the database for employee.

	if now.year>useraddedon.year:
		rh=obj.rh_add+3
		prsnl=onj.prsnl_add+3
		csul=csul_add+10
		mrrg=mrrg_add+15
		bvrmnt=bvrmnt_add+3
		comp=comp_add+6
		employee_leave.objects.filter(usr_id=usrid).update(rh_available=rh,prsnl_available=prsnl,csul_available=csul,mrrg_available=mrrg,bvrmnt_available=bvrmnt,comp_available=comp)

#    Retrieving employee leaves.

	usr_rhl=obj.rhl
	usr_prsnl=obj.prsnl
	usr_csul=obj.csul
	usr_mrrgl=obj.mrrgl
	usr_bvrmntl=obj.bvrmntl
	usr_compl=obj.compl

#    Retrieving current request to check.

	ltype=request.POST['type']
	frmdate=request.POST['frmdate']
	todate=request.POST['todate']
	descrptn=request.POST['desc']
	frmdateyear=int(frmdate[0:4])
	frmdatemnth=int(frmdate[5:7])
	frmdateday=int(frmdate[8:10])
	todateyear=int(todate[0:4])
	todatemnth=int(todate[5:7])
	todateday=int(todate[8:10])
	mnthdiff=todatemnth-frmdatemnth
	if mnthdiff>=0:
		daydiff=todateday-frmdateday+1
		if ltype=='RH':
			if daydiff>3:
				msg='RH Leaves cannot be greater than 3.'
			else:
				taken=usr_rhl
				if (taken+daydiff)>3:
					msg='You dont have sufficient RH leaves.'
				else:
					totalupdate=taken+daydiff
					employee_leave.objects.filter(usr_id=usrid).update(rhl=totalupdate)
					leaves.objects.create(usr_id=usrid,leavetype=ltype,status=1,frmdate=frmdate,todate=todate,desc=descrptn)
					msg='RH Leave apply Successful.'
		elif ltype=='Personal':
			if daydiff>3:
				msg='Personal Leaves cannot be greater than 3.'
			else:
				taken=usr_prsnl
				if (taken+daydiff)>3:
					msg='You dont have sufficient Personal leaves.'
				else:
					totalupdate=taken+daydiff
					employee_leave.objects.filter(usr_id=usrid).update(prsnl=totalupdate)
					leaves.objects.create(usr_id=usrid,leavetype=ltype,status=1,frmdate=frmdate,todate=todate,desc=descrptn)
					msg='Personal Leave apply Successful.'
		elif ltype=='Casual':
			if daydiff>10:
				msg='Casual Leaves cannot be greator than 10'
			else:
				taken=usr_csul
				if(taken+daydiff)>10:
					msg='You dont have sufficient Casual leaves.'
				else:
					totalupdate=taken+daydiff
					employee_leave.objects.filter(usr_id=usrid).update(csul=totalupdate)
					leaves.objects.create(usr_id=usrid,leavetype=ltype,status=1,frmdate=frmdate,todate=todate,desc=descrptn)
					msg='Casual Leave apply successful.'
		elif ltype=='Marriage':
			if daydiff>15:
				msg='Marriage Leaves cannot be greator than 15'
			else:
				taken=usr_mrrgl
				if(taken+daydiff)>15:
					msg='You dont have sufficient Marriage leaves.'
				else:
					totalupdate=taken+daydiff
					employee_leave.objects.filter(usr_id=usrid).update(mrrgl=totalupdate)
					leaves.objects.create(usr_id=usrid,leavetype=ltype,status=1,frmdate=frmdate,todate=todate,desc=descrptn)
					msg='Marriage Leave apply successful.'
		elif ltype=='Bevearment':
			if daydiff>3:
				msg='Bevearment Leaves cannot be greator than 3'
			else:
				taken=usr_bvrmntl
				if(taken+daydiff)>3:
					msg='You dont have sufficient Bevearment leaves.'
				else:
					totalupdate=taken+daydiff
					employee_leave.objects.filter(usr_id=usrid).update(bvrmntl=totalupdate)
					leaves.objects.create(usr_id=usrid,leavetype=ltype,status=1,frmdate=frmdate,todate=todate,desc=descrptn)
					msg='Bevearment Leave apply successful.'
		elif ltype=='Compulsary':
			if daydiff>6:
				msg='Compulsary Leaves cannot be greator than 6'
			else:
				taken=usr_compl
				if(taken+daydiff)>6:
					msg='You dont have sufficient Compulsary leaves.'
				else:
					totalupdate=taken+daydiff
					employee_leave.objects.filter(usr_id=usrid).update(compl=totalupdate)
					leaves.objects.create(usr_id=usrid,leavetype=ltype,status=1,frmdate=frmdate,todate=todate,desc=descrptn)
					msg='Compulsary Leave apply successful.'
	else:
		msg='You cannot apply leave for greator than 1 month'
	return render_to_response('apply_leave.html',{'msg':msg},context_instance=RequestContext(request))

#	Display Leave summary page.

def leave_summary(request):
	return render_to_response('leave_summary.html',context_instance=RequestContext(request))

def admnleavesummary(request):
	eid=request.session['member_id']
	if eid==1:
		return render_to_response('admn_leave_summary.html',context_instance=RequestContext(request))
	else:
		return HttpResponse('Only Admin can view this page.')

#	Employee wants to view his/her leave status.

def my_leave(request):
	usrid=request.session['member_id']
	try:
		obj=employee_leave.objects.get(usr_id=usrid)
	except employee_leave.DoesNotExist:
		usr_rhl=0
		usr_prsnl=0
		usr_csul=0
		usr_mrrgl=0
		usr_bvrmntl=0
		usr_compl=0
	else:
		usr_rhl=obj.rhl
		usr_prsnl=obj.prsnl
		usr_csul=obj.csul
		usr_mrrgl=obj.mrrgl
		usr_bvrmntl=obj.bvrmntl
		usr_compl=obj.compl
	return render_to_response('myleave.html',{'rhl':usr_rhl,'prsnl':usr_prsnl,'csul':usr_csul,'mrrgl':usr_mrrgl,'bvrmntl':usr_bvrmntl,'compl':usr_compl},context_instance=RequestContext(request))

def leave_details(request):
	lt1=request.GET['val']
	lt=int(lt1)
	usrid=request.session['member_id']
	obj=employee_leave.objects.get(usr_id=usrid)
	usr_rhl=obj.rhl
	usr_prsnl=obj.prsnl
	usr_csul=obj.csul
	usr_mrrgl=obj.mrrgl
	usr_bvrmntl=obj.bvrmntl
	usr_compl=obj.compl
	if lt==1:
		if usr_rhl==0:
			msg='You have not taken any RH Leaves'
			return render_to_response('leavedetails.html',{'msg':msg},context_instance=RequestContext(request))
		else:
			return render_to_response('leavedetails.html',{'obj':leaves.objects.filter(usr_id=usrid,leavetype='RH')},context_instance=RequestContext(request))
	elif lt==2:
		if usr_prsnl==0:
			msg='You have not taken any Personal Leaves'
			return render_to_response('leavedetails.html',{'msg':msg},context_instance=RequestContext(request))
		else:
			return render_to_response('leavedetails.html',{'obj':leaves.objects.filter(usr_id=usrid,leavetype='Personal'),'val':lt},context_instance=RequestContext(request))
	elif lt==3:
		if usr_csul==0:
			msg='You have not taken any Casual Leaves'
			return render_to_response('leavedetails.html',{'msg':msg},context_instance=RequestContext(request))
		else:
			return render_to_response('leavedetails.html',{'obj':leaves.objects.filter(usr_id=usrid,leavetype='Casual')},context_instance=RequestContext(request))
	elif lt==4:
		if usr_mrrgl==0:
			msg='You have not taken any Marriage Leaves'
			return render_to_response('leavedetails.html',{'msg':msg},context_instance=RequestContext(request))
		else:
			return render_to_response('leavedetails.html',{'obj':leaves.objects.filter(usr_id=usrid,leavetype='Marriage')},context_instance=RequestContext(request))
	elif lt==5:
		if usr_bvrmntl==0:
			msg='You have not taken any Bevearment Leaves'
			return render_to_response('leavedetails.html',{'msg':msg},context_instance=RequestContext(request))
		else:
			return render_to_response('leavedetails.html',{'obj':leaves.objects.filter(usr_id=usrid,leavetype='Bevearment')},context_instance=RequestContext(request))
	elif lt==6:
		if usr_bvrmntl==0:
			msg='You have not taken any Compulsary Leaves'
			return render_to_response('leavedetails.html',{'msg':msg},context_instance=RequestContext(request))
		else:
			return render_to_response('leavedetails.html',{'obj':leaves.objects.filter(usr_id=usrid,leavetype='Compulsary')},context_instance=RequestContext(request))
	else:
		return render_to_response('leavedetails.html',{'msg':lt},context_instance=RequestContext(request))

def admin_usrs_leaves(request):
	eid=request.session['member_id']
	if eid==1:
		return render_to_response('leave_usrs_list.html',{'obj':employee.objects.filter(~Q(usr_id = 1))},context_instance=RequestContext(request))
	else:
		return HttpResponse('Only Admin can view this page.')

#	Admin wants to see employees leave details

def admn_usrleave_details(request):
	eid=request.session['member_id']
	if eid==1:
		usr=request.GET['usrid']
		return render_to_response('usrleaves.html',{'obj1':employee.objects.get(usr_id=usr),'obj2':employee_leave.objects.get(usr_id=usr)},context_instance=RequestContext(request))
	else:
		return HttpResponse('Only Admin can view this page.')

def userleavedetails(request):
	usrid=request.GET['id']
	lt=int(request.GET['type'])
	obj1=employee_leave.objects.get(usr_id=usrid)
	usr_rhl=obj1.rhl
	usr_prsnl=obj1.prsnl
	usr_csul=obj1.csul
	usr_mrrgl=obj1.mrrgl
	usr_bvrmntl=obj1.bvrmntl
	usr_compl=obj1.compl
	if lt==1:
		if usr_rhl==0:
			msg='No RH Leaves taken.'
			return render_to_response('userleavedetails.html',{'msg':msg,'obj1':employee.objects.get(usr_id=usrid)},context_instance=RequestContext(request))
		else:
			return render_to_response('userleavedetails.html',{'obj':leaves.objects.filter(usr_id=usrid,leavetype='RH'),'obj1':employee.objects.get(usr_id=usrid)},context_instance=RequestContext(request))
	elif lt==2:
		if usr_prsnl==0:
			msg='No Personal Leaves taken.'
			return render_to_response('userleavedetails.html',{'msg':msg,'obj1':employee.objects.get(usr_id=usrid)},context_instance=RequestContext(request))
		else:
			return render_to_response('userleavedetails.html',{'obj':leaves.objects.filter(usr_id=usrid,leavetype='Personal'),'obj1':employee.objects.get(usr_id=usrid)},context_instance=RequestContext(request))
	elif lt==3:
		if usr_csul==0:
			msg='No Casual Leaves taken.'
			return render_to_response('userleavedetails.html',{'msg':msg,'obj1':employee.objects.get(usr_id=usrid)},context_instance=RequestContext(request))
		else:
			return render_to_response('userleavedetails.html',{'obj':leaves.objects.filter(usr_id=usrid,leavetype='Casual'),'obj1':employee.objects.get(usr_id=usrid)},context_instance=RequestContext(request))
	elif lt==4:
		if usr_mrrgl==0:
			msg='No Marriage Leaves taken.'
			return render_to_response('userleavedetails.html',{'msg':msg,'obj1':employee.objects.get(usr_id=usrid)},context_instance=RequestContext(request))
		else:
			return render_to_response('userleavedetails.html',{'obj':leaves.objects.filter(usr_id=usrid,leavetype='Marriage'),'obj1':employee.objects.get(usr_id=usrid)},context_instance=RequestContext(request))
	elif lt==5:
		if usr_bvrmntl==0:
			msg='No Bevearment Leaves taken.'
			return render_to_response('userleavedetails.html',{'msg':msg,'obj1':employee.objects.get(usr_id=usrid)},context_instance=RequestContext(request))
		else:
			return render_to_response('userleavedetails.html',{'obj':leaves.objects.filter(usr_id=usrid,leavetype='Bevearment'),'obj1':employee.objects.get(usr_id=usrid)},context_instance=RequestContext(request))
	elif lt==6:
		if usr_bvrmntl==0:
			msg='No Compulsary Leaves taken.'
			return render_to_response('userleavedetails.html',{'msg':msg,'obj1':employee.objects.get(usr_id=usrid)},context_instance=RequestContext(request))
		else:
			return render_to_response('userleavedetails.html',{'obj':leaves.objects.filter(usr_id=usrid,leavetype='Compulsary'),'obj1':employee.objects.get(usr_id=usrid)},context_instance=RequestContext(request))
	else:
		return render_to_response('userleavedetails.html',{'msg':lt,'obj1':employee.objects.get(usr_id=usrid)},context_instance=RequestContext(request))

#	Admin approves employees leaves

def approve(request):
	eid=request.session['member_id']
	if eid==1:
		try:
			obj=leaves.objects.get(status=1)
		except leaves.DoesNotExist:
			msg='No pending leaves.'
			return render_to_response('approve.html',{'msg':msg},context_instance=RequestContext(request))
		else:
			return render_to_response('approve.html',{'obj':leaves.objects.filter(status=1)},context_instance=RequestContext(request))
	else:
		return HttpResponse('Only Admin can view this page.')

def processapprove(request):
	eid=request.session['member_id']
	if eid==1:
		leaves.objects.filter(id=request.GET['id']).update(status=request.GET['val'])
		try:
			obj=leaves.objects.get(status=1)
		except leaves.DoesNotExist:
			msg='No pending leaves.'
			return render_to_response('approve.html',{'msg':msg},context_instance=RequestContext(request))
		else:
			return render_to_response('approve.html',{'obj':leaves.objects.filter(status=1)},context_instance=RequestContext(request))
	else:
		return HttpResponse('Only Admin can view this page.')

#	Admin wants to create a project

def createproject(request):
	eid=request.session['member_id']
	if eid==1:
		c={'obj':employee.objects.filter(~Q(usr_id = 1))}
		c.update(csrf(request))
		return render_to_response('createproject.html',c,context_instance=RequestContext(request))
	else:
		return HttpResponse('Only Admin can view this page.')

def process_project(request):
	prjct_title=request.POST['title']
	tech=request.POST['tech']
	desc=request.POST['desc']
	s_date=request.POST['sdate']
	e_date=request.POST['edate']
	total_members=request.POST['hide']
	client_id=request.POST['cid']
	now=datetime.datetime.now()
	obj1=emp_projects.objects.create(title=prjct_title,tech=tech,desc=desc,sdate=s_date,edate=e_date,mem_num=total_members,clientid=client_id,cdate=now)
	pid=obj1.pid
	names=request.POST['name_hide']
	c=''
	b=names.find(';')
	if(b<0):
		x=names.find('.')
		eid=names[:x]
		ename=names[x+2:]
		project_member.objects.create(pid=pid,pname=prjct_title,mem_id=eid,member_name=ename)
	else:
		while(names.find(';')>0):
			b=names.find(';')
			emp_name=names[:b]
			x=emp_name.find('.')
			emp_id=emp_name[:x]
			emp_name=emp_name[x+1:]
			project_member.objects.create(pid=pid,pname=prjct_title,mem_id=emp_id,member_name=emp_name)
			names=names[b+1:]
		x=names.find('.')
		eid=names[:x]
		names=names[x+2:]
		project_member.objects.create(pid=pid,pname=prjct_title,mem_id=eid,member_name=names)
	return render_to_response('createproject.html',{'msg':'Project has been created successfully','obj':employee.objects.filter(~Q(usr_id = 1))},context_instance=RequestContext(request))

#	Admin wants to see list of all projects

def all_project(request):
	try:
		obj=emp_projects.objects.all()
	except emp_projects.DoesNotExist:
		msg='No Projects'
		return render_to_response('allprojects.html',{'msg':msg},context_instance=RequestContext(request))
	else:
		return render_to_response('allprojects.html',{'obj':obj},context_instance=RequestContext(request))

def project_details(request):
	pid=request.GET['pid']
	return render_to_response('project_details.html',{'obj1':emp_projects.objects.get(pid=pid),'obj2':project_member.objects.filter(pid=pid)},context_instance=RequestContext(request))

#	Employee wants to see his/her assigned projects

def myprojects(request):
	eid=request.session['member_id']
	return render_to_response('myprojects.html',{'obj':project_member.objects.filter(mem_id=eid)},context_instance=RequestContext(request))

def myprojectdetails(request):
	pid=request.GET['pid']
	return render_to_response('project.html',{'obj':emp_projects.objects.get(pid=pid),'obj2':project_member.objects.filter(pid=pid)},context_instance=RequestContext(request))

#	Admin creates an announcement

def create_announcement(request):
	eid=request.session['member_id']
	if eid==1:
		c={}
		c.update(csrf(request))
		return render_to_response('announcement.html',c,context_instance=RequestContext(request))
	else:
		return HttpResponse('Only Admin can view this page.')

def process_announcement(request):
	obj=employee.objects.filter(~Q(usr_id = 1))
	frm='sturload@gmail.com'
	sub='IDiFY Solutions :: Announcement'
	msg=request.POST['msg']
	for a in obj:
		send_mail(sub,msg,frm,[a.email],fail_silently=False)
	msg='Announcement has been posted successfully'
	now=datetime.datetime.now()
	announcement.objects.create(msg=request.POST['msg'],cdate=now)
	return render_to_response('announcement.html',{'msg':msg},context_instance=RequestContext(request))

#	Employee wants to see all announcements

def watch_announcement(request):
	try:
		obj=announcement.objects.get(id=1)
	except announcement.DoesNotExist:
		return render_to_response('view_announcement.html',{'msg':'No Announcements'},context_instance=RequestContext(request))
	except announcement.MultipleObjectsReturned:
		return render_to_response('view_announcement.html',{'obj':announcement.objects.order_by('cdate').reverse()},context_instance=RequestContext(request))
	else:
		return render_to_response('view_announcement.html',{'obj':announcement.objects.order_by('cdate').reverse()},context_instance=RequestContext(request))

#	Admin wants to see all announcements

def admin_announcement(request):
	try:
		obj=announcement.objects.get(id=1)
	except announcement.DoesNotExist:
		return render_to_response('admin_announcement.html',{'msg':'No Announcements'},context_instance=RequestContext(request))
	except announcement.MultipleObjectsReturned:
		return render_to_response('admin_announcement.html',{'obj':announcement.objects.order_by('cdate').reverse()},context_instance=RequestContext(request))
	else:
		return render_to_response('admin_announcement.html',{'obj':announcement.objects.order_by('cdate').reverse()},context_instance=RequestContext(request))

#	Employee generates salary slip.

def salaryslip(request):
	c={}
	c.update(csrf(request))
	return render_to_response('salary_slip.html',c,context_instance=RequestContext(request))

def process_salaryslip(request):
	empid=request.session['member_id']
	request_month=int(request.POST['month'])
	request_year=int(request.POST['year'])
	now=datetime.datetime.now()
	now_date=now.day
	now_month=now.month
	now_year=now.year
	if request_year<now_year or request_year>now_year:
		msg='Salary slip not generated.'
		return render_to_response('gen_salary_slip.html',{'msg':msg},context_instance=RequestContext(request))
	elif request_year==now_year and request_month>now_month:
		msg='Salary slip not generated.'
		return render_to_response('gen_salary_slip.html',{'msg':msg},context_instance=RequestContext(request))
	elif request_year==now_year and request_month<now_month:
		try:
			obj=emp_payroll.objects.get(eid=empid,for_year=request_year,for_mnth=request_month,issued=1)
		except emp_payroll.DoesNotExist:
			obj=employee.objects.get(usr_id=empid)
			salary=obj.salary
			basic=(salary*50)/100
			metro=obj.metro
			if metro==1:
				hra=(basic*50)/100
			else:
				hra=(basic*40)/100
			conv=800
			med=1250
			bonus=salary-(basic+hra+conv+med)
			obj=emp_payroll.objects.create(eid=empid,basic=basic,hra=hra,convynce=conv,med=med,bonus=bonus,issued=0,for_mnth=request_month,for_year=request_year)
			return render_to_response('gen_salary_slip.html',{'obj':obj},context_instance=RequestContext(request))
		else:
			msg='You have already generated your salary slip for this month.'
			return render_to_response('gen_salary_slip.html',{'msg':msg},context_instance=RequestContext(request))
	elif request_year==now_year and request_month==now_month:
		if now_date<3:
			msg='Salary slip not generated.'
			return render_to_response('gen_salary_slip.html',{'msg':msg},context_instance=RequestContext(request))
		else:
			try:
				emp_payroll.objects.get(eid=empid,for_mnth=request_month,for_year=request_year,issued=1)
			except emp_payroll.DoesNotExist:
				obj=employee.objects.get(usr_id=empid)
				salary=obj.salary
				basic=(salary*50)/100
				metro=obj.metro
				if metro==1:
					hra=(basic*50)/100
				else:
					hra=(basic*40)/100
				conv=800
				med=1250
				bonus=salary-(basic+hra+conv+med)
				obj=emp_payroll.objects.create(eid=empid,basic=basic,hra=hra,convynce=conv,med=med,bonus=bonus,issued=0,for_mnth=request_month,for_year=request_year)
				return render_to_response('gen_salary_slip.html',{'obj':obj},context_instance=RequestContext(request))
			else:
				msg='You have already generated your salary slip for this month.'
				return render_to_response('gen_salary_slip.html',{'msg':msg},context_instance=RequestContext(request))

def generate_slip(request):
	eid=request.session['member_id']
	obj1=employee.objects.get(usr_id=eid)
	obj2=emp_payroll.objects.get(eid=eid,issued=0)
	obj3=emp_payroll.objects.get(eid=eid,issued=0)
	obj3.issued=1
	obj3.save()
	return render_to_response('slip.html',{'obj1':obj1,'obj2':obj2})

#	Admin wants to see employee's payroll details.

def adminpayroll(request):
	return render_to_response('emppayroll.html',{'obj':employee.objects.filter(~Q(usr_id = 1))},context_instance=RequestContext(request))

def emp_payroll_details(request):
	eid=request.GET['eid']
	c={'id':eid}
	c.update(csrf(request))
	return render_to_response('selectmonth.html',c,context_instance=RequestContext(request))

def payrolldetails(request):
	eid=request.POST['id']
	mnth=int(request.POST['month'])
	year=int(request.POST['year'])
	try:
		obj2=emp_payroll.objects.get(eid=eid,for_mnth=mnth,for_year=year)
	except emp_payroll.DoesNotExist:
		return render_to_response('emp_payroll_detail.html',{'obj1':employee.objects.get(usr_id=eid),'msg':'Salary Slip not Generated','month':mnth,'year':year},context_instance=RequestContext(request))
	else:
		return render_to_response('emp_payroll_detail.html',{'obj1':employee.objects.get(usr_id=eid),'obj2':obj2,'month':mnth,'year':year},context_instance=RequestContext(request))

#	Employee adds a contact.

def add_contact(request):
	return render_to_response('addcontact.html',context_instance=RequestContext(request))

def processcontact(request):
	empid=request.session['member_id']
	contact_name=request.GET['name']
	contact_no=request.GET['contact']
	contact_address=request.GET['address']
	emp_contacts.objects.create(eid=empid,name=contact_name,phone=contact_no,address=contact_address)
	return render_to_response('addcontact.html',{'msg':'Contact added successfully'},context_instance=RequestContext(request))

#	Employee lists his/her contacts.

def mycontacts(request):
	empid=request.session['member_id']
	try:
		obj=emp_contacts.objects.get(eid=empid)
	except emp_contacts.DoesNotExist:
		return render_to_response('mycontact.html',{'msg':'No Contacts'},context_instance=RequestContext(request))
	else:
		return render_to_response('mycontact.html',{'obj':emp_contacts.objects.filter(eid=empid)},context_instance=RequestContext(request))	

#	Admin wants to see all employee's contacts.

def admin_allcontacts(request):
	eid=request.session['member_id']
	if eid==1:
		return render_to_response('allcontacts.html',{'obj':employee.objects.filter(~Q(usr_id = 1))},context_instance=RequestContext(request))
	else:
		return HttpResponse('Only Admin can view this page.')

def view_emp_contact(request):
	empid=request.GET['eid']
	try:
		obj2=emp_contacts.objects.get(eid=empid)
	except emp_contacts.DoesNotExist:
		return render_to_response('empcontacts.html',{'obj1':employee.objects.get(usr_id=empid),'msg':'No saved contacts','empid':empid},context_instance=RequestContext(request))
	else:
		return render_to_response('empcontacts.html',{'obj1':employee.objects.get(usr_id=empid),'obj2':emp_contacts.objects.filter(eid=empid),'empid':empid})

#	Admin can delete a contact.

def deletecontact(request):
	eid=request.session['member_id']
	if eid==1:
		contactid=request.GET['cid']
		empid=request.GET['eid']
		obj=emp_contacts.objects.get(id=contactid)
		obj.delete()
		return render_to_response('empcontacts.html',{'obj1':employee.objects.get(usr_id=empid),'obj2':emp_contacts.objects.filter(eid=empid),'empid':empid,'msg':'Contact Deleted successfully'},context_instance=RequestContext(request))
	else:
		return HttpResponse('Only Admin can view this page.')

#	Employee can upload a document(DMS).

def upload_doc(request):
	c={}
	c.update(csrf(request))
	return render_to_response('upload.html',c,context_instance=RequestContext(request))

def savedoc(request):
	eid=request.session['member_id']
	if request.method=='POST':
	        form=DocumentForm(request.POST,request.FILES)
	        newdoc=Document(eid=eid,doctype=request.POST['type'],docfile=request.FILES['docfile'],desc=request.POST['desc'])
       		newdoc.save()
		return render_to_response('upload.html',{'msg':'Upload Successfull'},context_instance=RequestContext(request))
	else:
        	form=DocumentForm()
		return render_to_response('upload.html',{'msg':'There was a problem in uploading your file'},context_instance=RequestContext(request))

#	Employee lists his/her all uploaded documents.

def mydoc(request):
	empid=request.session['member_id']
	try:
		obj=Document.objects.get(eid=empid)
	except Document.DoesNotExist:
		return render_to_response('mydoc.html',{'msg':'No Document exists'},context_instance=RequestContext(request))
	else:
		return render_to_response('mydoc.html',{'obj':Document.objects.filter(eid=empid)},context_instance=RequestContext(request))

#	Admin can view every employee's all documents.

def alldocs(request):
	eid=request.session['member_id']
	if eid==1:
		return render_to_response('alldocs.html',{'obj':employee.objects.filter(~Q(usr_id = 1))},context_instance=RequestContext(request))
	else:
		return HttpResponse('Only Admin can view this page.')

def viewdocs(request):
	empid=request.GET['id']
	try:
		obj=Document.objects.get(eid=empid)
	except Document.DoesNotExist:
		return render_to_response('viewdocs.html',{'msg':'No Document exists','obj1':employee.objects.get(usr_id=empid)},context_instance=RequestContext(request))
	else:
		return render_to_response('viewdocs.html',{'obj':Document.objects.filter(eid=empid),'obj1':employee.objects.get(usr_id=empid)},context_instance=RequestContext(request))

