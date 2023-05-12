from django.shortcuts import render
from .models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    return render(request, "profiles/profiles.html", context={"profiles": profiles})


def profiles_detail(request, username):
    profile = Profile.objects.get(username=username)
    return render(
        request, "profiles/profiles-detail.html", context={"profile": profile}
    )
