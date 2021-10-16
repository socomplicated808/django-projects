from django.db import models
from django.db.models.deletion import CASCADE
import os

# Create your models here.
class Cluster(models.Model):

	STATUS = (
		('N','Not Started'),
		('I','In Porgress'),
		('C','Closed'),
	)

	TYPE = (
		('R','RDC'),
		('C','CDC'),
		('G','GC'),
	)

	cluster_code = models.CharField(max_length=250)
	cluster_status = models.CharField(max_length=20,choices=STATUS)
	cluster_type = models.CharField(max_length=20,choices=TYPE)
	jira_link = models.CharField(max_length=250)

	def __str__(self):
		return self.cluster_code


class Post(models.Model):

	name = models.CharField(max_length=250)
	time = models.CharField(max_length=20)
	cluster_log = models.TextField(null=True,blank=True)
	cluster_code = models.ForeignKey(Cluster,on_delete=CASCADE)	
	files = models.FileField(upload_to='files/',null=True,blank=True)

	def __str__(self):
		return str(self.cluster_code) + " " + str(self.time)

	def filename(self):
		return os.path.basename(self.files.name)

	class Meta:
		ordering = ['-id']


class CR(models.Model):
	STATUS = (
		('S','Security'),
		('X','SXC'),
		('L','Infra Leader'),
		('N','Not Started'),
		('I','In Progress'),
		('F','Finished'),
		('C','Closed'),
	)

	cr_number = models.CharField(max_length=250)
	start_date = models.CharField(max_length=10,default='YYYY-MM-DD')
	start_time = models.CharField(max_length=5,default='HH:MM')
	end_date = models.CharField(max_length=10,default='YYYY-MM-DD')
	end_time = models.CharField(max_length=5,default='HH:MM')
	status = models.CharField(max_length=20,choices=STATUS)

	def __str__(self):
		return self.cr_number