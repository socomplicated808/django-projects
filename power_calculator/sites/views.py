from django.shortcuts import render
from powerstrips.models import Parent,Child
from .models import Site
from django.shortcuts import render, get_object_or_404, redirect
from powerstrips.models import Child
from devices.models import Device
# from powerstrips.forms import ChildForm

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Site
from powerstrips.models import Parent, Child
from devices.models import Device, DeviceTemplate

from devices.models import Device
from django.shortcuts import render, get_object_or_404
from .models import Site

def display_power_strips(request, site_code):
    site = get_object_or_404(Site, site_code=site_code.upper())
    parents = site.parent_power_strip.all()

    selected_parent = None
    selected_parent_name = request.GET.get("parent")

    for parent in parents:
        enriched_children = []

        for child in parent.child_strips.all():
            # Build 6 fixed slots
            slots = {i: None for i in range(1, 7)}

            for device in child.devices.all():
                slots[device.slot] = device

            child.slots = slots
            child.total_power_value = sum(
                d.template.power for d in slots.values() if d
            )

            enriched_children.append(child)

        parent.enriched_child_strips = enriched_children

        # ✅ ONLY set selected_parent if explicitly clicked
        if selected_parent_name and parent.name == selected_parent_name:
            selected_parent = parent

    context = {
        "site_code": site_code,
        "parents": parents,
        "selected_parent": selected_parent,  # ← may be None
        "slot_range": range(1, 7),
    }

    return render(request, "sites/power_distribution.html", context)


def edit_child(request, site_code, child_id):
    child = get_object_or_404(Child, id=child_id)

    # All available device templates (catalog)
    templates = DeviceTemplate.objects.all()

    # Devices currently plugged into this child strip
    devices = child.devices.all()

    # Build slot map (1–6)
    slots = {i: None for i in range(1, 7)}
    for device in devices:
        slots[device.slot] = device

    if request.method == "POST":
        # Clear existing devices for this child
        child.devices.all().delete()

        # Recreate devices based on submitted slots
        for slot in range(1, 7):
            template_id = request.POST.get(f"slot_{slot}")
            if template_id:
                template = get_object_or_404(DeviceTemplate, id=template_id)
                Device.objects.create(
                    child_strip=child,
                    template=template,
                    slot=slot
                )

        return redirect("display_power_strips", site_code=site_code)

    context = {
        "site_code": site_code,
        "child": child,
        "templates": templates,
        "slots": slots,
        "slot_range": range(1, 7),
    }

    return render(request, "sites/edit_child.html", context)