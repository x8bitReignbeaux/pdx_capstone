from django.shortcuts import render

# Create your views here.
def profile_grid(request):
    return render(request, 'profile_grid/grid.html')