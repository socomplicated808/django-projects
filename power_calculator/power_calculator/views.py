from django.http import HttpResponse
from django.shortcuts import render,redirect
from sites.models import Site
import re

def home_view(request):
    sites = Site.objects.values_list('site_code',flat=True).order_by('site_code')
    context = {'sites':sites}
    is_valid = True
    is_exists = False

    if request.method == "POST":
        new_site_code = request.POST.get("new_site_code").replace(' ','').replace('\t','').upper()
        #make sure the site code follows the format NRT5(3 letters 1 Number)
        pattern = re.compile(r"[A-Z]{3}\d")
        is_valid = bool(pattern.match(new_site_code))
        context['is_valid'] = is_valid
        site = request.POST.get("site")
        if not new_site_code:
            return redirect(f'sites/{site.upper()}')

        #checking if the site is a duplicate
        for site in sites:
            if site == new_site_code:
                is_exists = True
                context['is_exists'] = is_exists
                return render(request,'home.html',context)

        if is_valid:
            Site(site_code=new_site_code).save()
            return redirect(f'sites/{new_site_code.upper()}')
    return render(request,'home.html',context)