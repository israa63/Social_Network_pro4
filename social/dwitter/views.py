# dwitter/views.py
from django.shortcuts import render,redirect
from .forms import DweetForm
from .models import Profile
from django import forms
from django.http import HttpResponseRedirect


def dashboard(request):
    # dwitter/views.py
    form = DweetForm(request.POST or None)
    if request.method == "POST": #1
        #form = DweetForm(request.POST) #2
        if form.is_valid(): #3
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
        #return redirect('/sucsess/') # 4 
            return redirect('dwitter:dashboard')     
    
    return render(request, "dwitter/dashboard.html", {"form": form})

    
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})  

def profile(request, pk):
     #if user not have profile, creat outumaticly profile.But we use create user create profile ouumatic
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
            current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile}) 



          