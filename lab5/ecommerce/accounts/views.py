from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from products.models import *
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.
def myLogin(request):
  context = {'form':authenticate()}
  return render(request, template_name='registration/login.html', context= context)

def myProfile(request):
  # request.session.clear()
  return redirect(reverse('products'))


class registerationForm(CreateView):
  model=User
  template_name='registration/register.html'
  form_class=UserCreationForm
  context_object_name='from'
  success_url=reverse_lazy("login")
