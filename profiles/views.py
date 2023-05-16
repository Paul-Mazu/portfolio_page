from django.shortcuts import render
from .models import Profile
from .forms import SignUpForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


def profiles(request):
    profiles = Profile.objects.all()
    return render(request, "profiles/profiles.html", context={"profiles": profiles})


def profiles_detail(request, username):
    profile = Profile.objects.get(username=username)
    return render(
        request, "profiles/profiles-detail.html", context={"profile": profile}
    )


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("profiles:login")
    template_name = "profiles/signup.html"
