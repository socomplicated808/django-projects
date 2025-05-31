from django.shortcuts import render
from powerstrips.models import Parent,Child
from .models import Site
# from powerstrips.forms import ChildForm

# Create your views here.
def display_power_strips(request,site_code):

    site = Site.objects.get(site_code=site_code.upper())

    parents = site.parent_power_strip.all()

    # parents = Parent.objects.all()
    child_power = {}

    #calculating total power of all devices for each child strip
    for parent in parents:
        enriched_children = []
        for child in parent.child_strips.all():
            total_power = sum(device.power for device in child.device_set.all())
            child.total_power = total_power
            enriched_children.append(child)
            print(child.total_power)
        parent.enriched_child_strips = enriched_children

    # site_code = Site.objects.filter(site_code = site_code).first()
    context = {'site_code':site_code,'parents':parents,'child_power':child_power}
    print(child_power)
    return render(request,'sites/power_distribution.html',context)

#def edit_devices(request,site_code,child_location):
#    if request.method == 'GET':
#        form = ChildForm(instance=Child.objects.get(location=child_location))
#    context = {'site_code':site_code,'child_location':child_location,'form':form}
#    return render(request,'sites/edit_devices.html',context)