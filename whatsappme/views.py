#-*- coding: utf-8 -*-

from django.shortcuts import render
# from user_manager.models import Tab ,Application,Page,Footer 
from django.contrib.auth.decorators import login_required
# from forms import  ConnexionForm 
from django.shortcuts import render
# from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import redirect
from django.http import HttpResponse,HttpRequest
from django.core.urlresolvers import reverse
from django.template import Context
from django.template.loader import get_template
from user_manager.form import UserRegisterForm


def Home(request):
    form2=UserRegisterForm()
    return render(request,'home.html',locals()) 