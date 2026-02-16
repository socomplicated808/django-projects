from users.models import UserProfile
from sites.models import Site


def user_can_access_site(user, site_code):
    # Admins can access everything
    if user.is_superuser or user.is_staff:
        return True

    site_code = site_code.upper()

    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        return False

    return profile.sites.filter(site_code=site_code).exists()
