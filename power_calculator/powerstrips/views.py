from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from powerstrips.models import Child
from devices.models import Device

def edit_child(request, site_code, child_id):
    child = get_object_or_404(Child, id=child_id)
    all_devices = Device.objects.all()
    current_devices = child.device_set.all()

    if request.method == 'POST':
        # Clear existing devices
        current_devices.delete()

        # Assign new devices
        device_ids = request.POST.getlist('devices')
        for device_id in device_ids:
            device = get_object_or_404(Device, id=device_id)
            # Duplicate device under this child
            Device.objects.create(
                model=device.model,
                power=device.power,
                child=child
            )
        return redirect('power_distribution')  # Adjust this to your actual page name

    return render(request, 'edit_child.html', {
        'site_code': site_code,
        'child': child,
        'all_devices': all_devices,
        'current_devices': current_devices
    })
