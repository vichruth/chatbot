from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm 
from django.contrib.auth.decorators import login_required
import requests


def hello_world(request):
    return HttpResponse("Hello, world!")

def index(request):
    return HttpResponse('Hi, Vichruth M')

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")      # or wherever
    else:
        form = SignUpForm()

    return render(request, "app/signup.html", {"form": form})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
@login_required
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('chat_with_ai')  # change 'home' to your desired URL name
    else:
        form = AuthenticationForm()
    
    return render(request, 'app/login.html', {'form': form})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')  # or 'index'

import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def chat_with_ai(request):
    hi=''
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            response = requests.post("http://localhost:11434/api/generate", json={
                "model": "qwen:4b",
                "prompt": prompt,
                "stream": False
            })
            reply=response.json()
            hi = reply.get('response', 'No response from AI')
    
    return render(request, 'app/home.html', {'response': hi})
