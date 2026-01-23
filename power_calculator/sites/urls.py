from django.urls import path
from . import views



urlpatterns = [
    path('<str:site_code>',views.display_power_strips,name='display_power_strips'),
    path('edit-child/<str:site_code>/<int:child_id>/', views.edit_child, name='edit_child'),
]
