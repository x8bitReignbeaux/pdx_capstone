from django.shortcuts import render
from users.models import UserProfile

# Create your views here.
def profile_grid(request):
    user_list = UserProfile.objects.all()
    context = {
        'user_list': user_list
    }
    return render(request, 'profile_grid/grid.html', context=context)

def profile(request): 
    
    return render(request, 'profile_grid/profile.html')