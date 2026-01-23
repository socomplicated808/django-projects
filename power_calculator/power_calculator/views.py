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

        # GO button
        if action == "go":
            site_code = request.POST.get("site")
            if site_code:
                return redirect("display_power_strips", site_code=site_code)

        # ADD button
        elif action == "add":
            new_site = request.POST.get("new_site_code")

            if not new_site:
                is_valid = False
            else:
                new_site = new_site.replace(" ", "").upper()

                if Site.objects.filter(site_code=new_site).exists():
                    is_exists = True
                else:
                    Site.objects.create(site_code=new_site)
                    return redirect("display_power_strips", site_code=new_site)

    return render(
        request,
        "home.html",
        {
            "sites": sites,
            "is_exists": is_exists,
            "is_valid": is_valid,
        },
    )
