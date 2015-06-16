#-*- coding: utf-8 -*-
from django.shortcuts import render
from form  import ConnexionForm, UserRegisterForm ,CompanyRegisterForm
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import redirect
from django.http import HttpResponse,HttpRequest
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import string 
import random
from django.contrib.auth.models import User
from models import Profile,Phone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from serializers import PhoneSerializer ,AddressSerializer ,ProfileSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework import permissions



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



#sign in view
def signin(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user) 
                username=user.username
                return redirect(user_space,username) # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'sign-in.html', locals())
#subscribe view
def subscribe(request):
    if request.method == "POST":
       username=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
       password=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
       user = User(username=username,password=password)
       user.set_password(password)
       user.save()
       profile=Profile(user=user)
       profile.save()
       phone=Phone(number_phone=request.POST.get("number_phone"),country_code=request.POST.get("country_code"),owner=profile)
       phone.save()
       user_login= authenticate(username=username, password=password)
       login(request, user_login) 
    return redirect(user_space,user.username)

#sign up view
def signup(request):
	
    form1 = UserRegisterForm()
    form2=CompanyRegisterForm()
    return render(request, 'sign-up.html', locals())

#redirection towards user space
@login_required
def user_space(request,username):     
    return render(request,'base.html') 

#sign out view
def signout(request):
    logout(request)
    return redirect(reverse(signin))


@api_view(['GET'])
def user_list(request):
    profiles=Profile.objects.all()
    serializer=ProfileSerializer(profiles,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def  user_get(request):
    
    try:
        profile = Profile.objects.get(user_id=request.user.id)
        
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=ProfileSerializer(profile)
   
    return Response(serializer.data)