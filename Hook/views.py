from django.shortcuts import redirect
from django.urls import reverse

def home(request): 
    return redirect(reverse('profile_grid:profile_grid'))