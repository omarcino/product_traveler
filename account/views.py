from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

from django.contrib.auth.decorators import login_required


### Create your views here.
@login_required
def dashboard(request):
    return render(request, 'live/index.html')






            

