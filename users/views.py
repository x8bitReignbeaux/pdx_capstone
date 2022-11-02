from django.views.generic import CreateView
from django.urls import reverse_lazy
from .admin import UserCreationForm

# Create your views here.
class RegisterView(CreateView): 
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'