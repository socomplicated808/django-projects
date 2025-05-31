from django.urls import path
from . import views



urlpatterns = [
    path('<str:site_code>',views.display_power_strips,name='display_power_strips'),
    # path('<str:site_code>/edit/<str:child_location>',views.edit_devices,name='edit_devices')
]
