from django.contrib import admin
from .models import Cluster,Post,CR

# Register your models here.
admin.site.register(Cluster)
admin.site.register(Post)
admin.site.register(CR)