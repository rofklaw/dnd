from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User, Admin

def index(request):
    return render(request, 'logreg/index.html')

def register(request):
    user = User.objects.regvalidator(request.POST['fname'], request.POST['lname'], request.POST['email'], request.POST['password'], request.POST['confirm'])
    if user['errors'] != []:
        for errors in user['errors']:
            messages.add_message(request, messages.ERROR, errors)
        return redirect(reverse('login:home'))
    prehash = User.objects.bcryptor(request.POST['password'])
    pwhash = prehash['pwhash']
    User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['email'], pwhash = pwhash)
    request.session['first_name'] = request.POST['fname']
    namer = User.objects.get(email = request.POST['email'])
    if namer.id == 1:
        Admin.objects.create(users = namer, privilege_level = 1)
    request.session['id'] = namer.id
    request.session['first_name'] = namer.first_name
    return redirect(reverse('characters:profile'))

def login(request):
    user = User.objects.logvalidator(request.POST['email'], request.POST['password'])
    if user['errors'] != []:
        for errors in user['errors']:
            messages.add_message(request, messages.ERROR, errors)
        return redirect(reverse('login:home'))
    namer = User.objects.get(email = request.POST['email'])
    request.session['id'] = namer.id
    request.session['first_name'] = namer.first_name
    return redirect(reverse('characters:profile'))
