from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render,redirect
from sites.models import Site
import re
from django.shortcuts import render, redirect
from sites.models import Site

@login_required(login_url="/login/")
def home_view(request):
    sites = Site.objects.values_list("site_code",flat=True).order_by("site_code")
    is_exists = False
    is_valid = True

    if request.method == "POST":

        action = request.POST.get("action")

        if action == "add":
            new_site_code = request.POST.get("new_site_code", "")

            # normalize input (uppercase + strip spaces and tabs)
            new_site_code = new_site_code.strip().replace(" ","").replace("\t","").upper()

            # 3 letters followed by 1 number
            pattern = r"^[A-Z]{3}[1-9]$"

            if not re.match(pattern, new_site_code):
                is_valid = False

            elif Site.objects.filter(site_code=new_site_code).exists():
                is_exists = True

            else:
                # create site only if valid
                Site.objects.create(site_code=new_site_code)
                return redirect(f"sites/{new_site_code.upper()}")  # or refresh page

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


class RoleBasedLoginView(LoginView):
    template_name = "login.html"

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        # Admin users → Django admin
        if user.is_superuser or user.is_staff:
            return redirect("/admin/")

        # Engineers → redirect to selected site if exists
        site_code = self.request.session.get("selected_site")
        if site_code:
            return redirect(f"/sites/{site_code}/")

        # fallback
        return redirect("/")