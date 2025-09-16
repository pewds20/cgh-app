from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# simple function to render home.html
def home_view(request):
    return render(request, "home.html")

def referral_view(request):
    return render(request, "referral.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('referral/', referral_view, name='referral'),
]
