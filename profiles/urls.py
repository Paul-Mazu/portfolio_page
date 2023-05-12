from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.profiles, name="profiles"),
    path("<str:username>", views.profiles_detail, name="profiles-detail"),
]
