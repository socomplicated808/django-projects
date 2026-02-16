from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from powerstrips.models import Child
from devices.models import Device
from sites.models import Site
from users.utils import user_can_access_site

@login_required
def edit_child(request, site_code, child_id):
    # Get site from URL
    site = get_object_or_404(Site, site_code=site_code)

    # HARD permission check (user must be assigned this site)
    if not user_can_access_site(request.user, site_code):
        messages.error(request, "You do not have permission to edit this site.")
        return redirect("display_power_strips", site_code=site_code)

    # CRITICAL SECURITY: Child must belong to this site
    child = get_object_or_404(Child, id=child_id, site=site)

    # Get all device templates (or filter if needed)
    templates = Device.objects.filter(is_template=True)

    # Build slot data (1–6)
    slot_range = range(1, 7)
    devices_by_slot = {d.slot: d for d in child.devices.all()}

    if request.method == "POST":
        # Remove old devices for this child
        child.devices.all().delete()

        # Create new devices per slot
        for slot in slot_range:
            template_id = request.POST.get(f"slot_{slot}")
            if template_id:
                template = get_object_or_404(Device, id=template_id)

                # Clone template into real device
                Device.objects.create(
                    model=template.model,
                    power=template.power,
                    slot=slot,
                    child=child,
                )

        messages.success(request, "Devices updated successfully.")
        return redirect("display_power_strips", site_code=site_code)

    return render(request, "sites/edit_child.html", {
        "site_code": site_code,
        "child": child,
        "templates": templates,
        "slot_range": slot_range,
        "devices_by_slot": devices_by_slot,
    })