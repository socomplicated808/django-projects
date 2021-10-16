from django.urls import path
from .views import CreateCluster, GcList,ViewPost,CreateNewPost,RdcList,EditPost,CrList,CreateCr,EditCr

urlpatterns = [
	path('GC-list/',GcList,name='gc-list'),
	path('RDC-list/',RdcList,name='rdc-list'),
	path('CR-list/',CrList,name='cr-list'),
	path('newcr/',CreateCr,name='new-cr'),
	path('newccluster/',CreateCluster,name='new-cluster'),
	path('<str:cluster_code>/',ViewPost,name='view-post'),
	path('<str:cluster_code>/newpost/',CreateNewPost,name='new-post'),
	path('edit_post/<str:pk>/',EditPost,name='edit-post'),
	path('edit_cr/<str:pk>/',EditCr,name='edit-cr'),

]