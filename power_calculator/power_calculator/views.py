from django.http import HttpResponse
from django.shortcuts import render,redirect
from sites.models import Site
import re
from django.shortcuts import render, redirect
from sites.models import Site

def home_view(request):
    sites = Site.objects.all()
    is_exists = False
    is_valid = True

    if request.method == "POST":

        action = request.POST.get("action")

        if action == "add":
            new_site_code = request.POST.get("new_site_code", "")

            # normalize input (uppercase + strip spaces)
            new_site_code = new_site_code.strip().upper()

            # 3 letters followed by 1 number
            pattern = r"^[A-Z]{3}[1-9]$"

            if not re.match(pattern, new_site_code):
                is_valid = False

            elif Site.objects.filter(site_code=new_site_code).exists():
                is_exists = True

            else:
                # create site only if valid
                Site.objects.create(site_code=new_site_code)
                return redirect("home")  # or refresh page

        elif action == "go":
            site_code = request.POST.get("site")
            if site_code:
                return redirect("display_power_strips", site_code=site_code)

    context = {
        "sites": sites,
        "is_exists": is_exists,
        "is_valid": is_valid,
    }

    return render(request, "home.html", context)
