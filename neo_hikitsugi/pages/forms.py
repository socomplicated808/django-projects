from django.forms import ModelForm
from django import forms
from django.forms.widgets import ClearableFileInput
from .models import Cluster, Post,CR

class PostForm(ModelForm):

	class Meta:

		model = Post
		fields = ['name','time','cluster_log','files']
		widgets = {'files':ClearableFileInput(attrs={'multiple':True})}


class CrForm(ModelForm):

	class Meta:

		model = CR
		fields = '__all__'


class ClusterForm(ModelForm):

	class Meta:
		model = Cluster
		fields = '__all__'