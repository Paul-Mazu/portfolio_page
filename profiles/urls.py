from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.profiles, name="profiles"),
    path(
        "login/",
        auth_view.LoginView.as_view(template_name="profiles/login.html"),
        name="login",
    ),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="create-profile"),
    path("<str:username>", views.profiles_detail, name="profiles-detail"),
]
