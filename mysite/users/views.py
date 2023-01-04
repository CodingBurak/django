from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

def register(request):
  form = RegisterForm()
  if request.method == "POST":
     form = RegisterForm(request.POST)
     if form.is_valid():
       form.save()
       username = form.cleaned_data.get("username")
       password = form.cleaned_data.get("password")
       messages.success(request, "Welcome {} , dont loose your pw {} and thanks for registering".format(username, password))
       return redirect("login")
  return render(request, "users/register.html", {"form":form})