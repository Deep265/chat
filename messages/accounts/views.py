from django.shortcuts import render
from django.views.generic import CreateView
from .models import Users
from .forms import UsersFroms
# Create your views here.
class SignUp(CreateView):
    model = Users
    template_name = 'accounts/signup.html'
    form_class = UsersFroms
