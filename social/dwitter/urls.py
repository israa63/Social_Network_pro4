# dwitter/urls.py
from django.urls import path,include
from .views import dashboard
from .views import dashboard, profile_list,profile,dwitter,register

app_name = "dwitter"
urlpatterns = [
path("", dwitter, name="dwitter"),
path("profile_list/", profile_list, name="profile_list"),
path("profile/<int:pk>", profile, name="profile"),
#path("sucsess/",dashboard, name="sucsess"),

path("dashboard/",dashboard, name="dashboard"),
path("accounts/", include("django.contrib.auth.urls")),
path("register/", register, name="register"),

]