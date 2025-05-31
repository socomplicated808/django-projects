from django.contrib import admin
from .models import Parent,Child

# Register your models here.
admin.site.register(Child)
admin.site.register(Parent)