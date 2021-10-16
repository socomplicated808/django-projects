from django.shortcuts import render,redirect
from .models import Cluster,Post,CR
from .forms import PostForm,CrForm,ClusterForm

# Create your views here.
# def Home(request):
# 	return render(request,'GC-list.html')

def CrList(request):
	crs = CR.objects.all()
	context = {'crs':crs}

	return render(request,'CR-list.html',context)


def CreateCr(request):
	form = CrForm()

	context = {'form':form}

	if request.method == 'POST':
		form = CrForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('cr-list')

	return render(request,'new-cr.html',context)


def EditCr(request,pk):
	cr = CR.objects.get(id=pk)
	form = CrForm(instance=cr)
	context = {'form':form}

	if request.method == 'POST':
		form = CrForm(request.POST,instance=cr)
		if form.is_valid():
			form.save()

			return redirect('cr-list')

	return render(request,'edit-cr.html',context)


def GcList(request):
	gcs = Cluster.objects.all()
	context = {'gcs':gcs}

	return render(request,'GC-list.html',context)


def RdcList(request):
	rdcs = Cluster.objects.all()
	context = {'rdcs':rdcs}

	return render(request,'RDC-list.html',context)


def ViewPost(request,cluster_code):
	cluster_code = Cluster.objects.get(cluster_code=cluster_code)
	posts = cluster_code.post_set.all()

	context = {'cluster_code':cluster_code,'posts':posts}

	return render(request,'view-post.html',context)


def CreateNewPost(request,cluster_code):
	form = PostForm()
	
	if request.method == 'POST':
		form = PostForm(request.POST,request.FILES)
		if form.is_valid():
			add_cluster_code_to_form = form.save(commit=False)
			add_cluster_code_to_form.cluster_code = Cluster.objects.get(cluster_code=cluster_code)
			add_cluster_code_to_form.save()
			return redirect('view-post',cluster_code)

	context = {'form':form}

	return render(request,'new-post.html',context)


def EditPost(request,pk):
	post = Post.objects.get(id=pk)
	form = PostForm(instance=post)

	context = {'form':form}

	if request.method == 'POST':
		form = PostForm(request.POST,instance=post)
		if form.is_valid():
			form.save()
			return redirect('view-post',post.cluster_code)

	return render(request,'edit-post.html',context)


def CreateCluster(request):
	form = ClusterForm()
	context = {'form':form}

	if request.method == 'POST':
		form = ClusterForm(request.POST)
		if form.is_valid():
			form.save()
			if form.cleaned_data.get('cluster_type') == 'R':
				return redirect('rdc-list')
			elif form.cleaned_data.get('custer_type') == 'G':
				return redirect('gc-list')
			return redirect('home')

	return render(request,'new-cluster.html',context)