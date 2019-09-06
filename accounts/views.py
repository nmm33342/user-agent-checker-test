# views.py
from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm, EditProfileForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST, response.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "registration/registration.html", {"form":form})

def edit_profile(response):
    if not response.user.is_anonymous:
        if response.method == "POST":
            form = EditProfileForm(response.POST, response.FILES, instance=response.user)
            if form.is_valid():
                form.save()
                return redirect("/")
        else:
            form = EditProfileForm(response.POST, response.FILES, instance=response.user)
        return render(response, "registration/edit_profile.html", {"form":form})
    return HttpResponse("Unathorized", status=401)