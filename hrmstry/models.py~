from django.db import models

# Create your models here.

class employee(models.Model):
	usr_id=models.AutoField(primary_key=True)
	passwd=models.CharField(max_length=30)
	f_name=models.CharField(max_length=20)
	l_name=models.CharField(max_length=20)
	email=models.URLField(unique=True)
	desg=models.CharField(max_length=25)
	salary=models.BigIntegerField()
	doj=models.DateField(null=True)
	gender=models.CharField(max_length=6,null=True)
	marr_status=models.CharField(max_length=20,null=True)
	dob=models.DateField(null=True)
	contact=models.CharField(max_length=20,null=True)
	address=models.CharField(max_length=100,null=True)
	metro=models.IntegerField(null=True)
	is_admin=models.IntegerField()

	def __unicode__(self):
        	return u'%s %s %s' % (self.usr_id,self.f_name, self.l_name)

class total_leaves(models.Model):
	rh_l=models.IntegerField()
	prsnl_l=models.IntegerField()
	csul_l=models.IntegerField()
	mrrg_l=models.IntegerField()
	bvrmnt_l=models.IntegerField()
	comp_l=models.IntegerField()

	def __unicode__(self):
		return u'%s %s %s %s %s %s' % (self.rh_l,self.prsnl_l,self.csul_l,self.mrrg_l,self.bvrmnt_l,self.comp_l)

class employee_leave(models.Model):
	usr_id=models.IntegerField(primary_key=True)
	rhl=models.DecimalField(max_digits=10,decimal_places=6)
	rh_available=models.IntegerField()
	rh_add=models.DecimalField(max_digits=10,decimal_places=6)
	prsnl=models.DecimalField(max_digits=10,decimal_places=6)
	prsnl_available=models.IntegerField()
	prsnl_add=models.DecimalField(max_digits=10,decimal_places=6)
	csul=models.DecimalField(max_digits=10,decimal_places=6)
	csul_available=models.IntegerField()
	csul_add=models.DecimalField(max_digits=10,decimal_places=6)
	mrrgl=models.DecimalField(max_digits=10,decimal_places=6)
	mrrg_available=models.IntegerField()
	mrrg_add=models.DecimalField(max_digits=10,decimal_places=6)
	bvrmntl=models.DecimalField(max_digits=10,decimal_places=6)
	bvrmnt_available=models.IntegerField()
	bvrmnt_add=models.DecimalField(max_digits=10,decimal_places=6)
	compl=models.DecimalField(max_digits=10,decimal_places=6)
	comp_available=models.IntegerField()
	comp_add=models.DecimalField(max_digits=10,decimal_places=6)
	emp_added=models.DateField(auto_now_add=True)

	def __unicode__(self):
		return u'%s %s %s %s %s %s %s' % (self.usr_id,self.rhl,self.prsnl,self.csul,self.mrrgl,self.bvrmntl,self.compl)

class leaves(models.Model):
	usr_id=models.IntegerField()
	leavetype=models.CharField(max_length=20)
	frmdate=models.CharField(max_length=20)
	todate=models.CharField(max_length=20)
	status=models.IntegerField()
	desc=models.CharField(max_length=255)

	def __unicode__(self):
		return u'%s %s %s %s %s' % (self.usr_id,self.leavetype,self.frmdate,self.todate,self.status)

class emp_projects(models.Model):
	pid=models.AutoField(primary_key=True)
	title=models.CharField(max_length=100)
	tech=models.CharField(max_length=100)
	desc=models.CharField(max_length=255)
	sdate=models.DateField()
	edate=models.DateField()
	mem_num=models.IntegerField()
	clientid=models.URLField()
	cdate=models.DateTimeField()

	def __unicode__(self):
		return u'%s %s %s %s %s %s' % (self.pid,self.title,self.sdate,self.edate,self.mem_num,self.cdate)

class project_member(models.Model):
	uid=models.AutoField(primary_key=True)
	pid=models.IntegerField()
	pname=models.CharField(max_length=100)
	mem_id=models.IntegerField()
	member_name=models.CharField(max_length=100)

	def __unicode__(self):
		return u'%s %s' % (self.pid,self.member_name)

class announcement(models.Model):
	msg=models.CharField(max_length=255)
	cdate=models.DateTimeField()

	def __unicode__(self):
		return u'%s %s' % (self.msg,self.cdate)

class emp_payroll(models.Model):
	eid=models.IntegerField()
	basic=models.IntegerField()
	hra=models.IntegerField()
	convynce=models.IntegerField()
	med=models.IntegerField()
	bonus=models.IntegerField()
	issued=models.IntegerField()
	for_mnth=models.IntegerField()
	for_year=models.IntegerField()
	issue_date=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s %s %s' % (self.eid,self.for_mnth,self.issue_date)

class emp_contacts(models.Model):
	eid=models.IntegerField()
	name=models.CharField(max_length=100)
	phone=models.CharField(max_length=20)
	address=models.CharField(max_length=255)
	addedon=models.DateField(auto_now_add=True)

	def __unicode__(self):
		return u'%s %s %s' % (self.eid,self.name,self.addedon)

class Document(models.Model):
	eid=models.IntegerField()
	doctype=models.CharField(max_length=20)
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	desc=models.CharField(max_length=255)

	def __unicode__(self):
		return u'%s %s' % (self.eid,self.doctype)

