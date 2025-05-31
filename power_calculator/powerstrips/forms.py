# from django.forms import ModelForm
# from .models import Child
# from devices.models import Device


# class ChildForm(ModelForm):
#     class Meta:
#         model = Child
#         fields = ['location','device']

# def __init__(self,*args,**kwargs):
#     child_instance = kwargs.get('instance')
#     super().__init__(*args,**kwargs)

#     if child_instance:
#         self.fields['device'].queryset = Device.objects.filter(child=child_instance)


