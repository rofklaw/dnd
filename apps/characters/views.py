from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..logreg.models import User
from .models import Character, Attribute


# Create your views here.
def profile(request):
    try:
        User.objects.get(id = request.session['id'])
    except:
        return redirect(reverse('login:home'))
    context = {
    "user": User.objects.get(id=request.session['id']),
    "Attributes":Attribute.objects.filter(character__user__id=request.session['id'])
    }
    count = {
    "zero": 0,
    "one": 1
    }
    return render(request, 'characters/profile.html', context, count)

def create(request):
    try:
        User.objects.get(id = request.session['id'])
    except:
        return redirect(reverse('login:home'))
    Character.objects.addCharacter(request.POST.copy(), request.session['id'])
    character = Character.objects.get(name=request.POST['name'])
    request.session['character'] = character.name
    return redirect(reverse("characters:charCreate"))

def createAttb(request):
    try:
        User.objects.get(id = request.session['id'])
    except:
        return redirect(reverse('login:home'))
    data = {'STR': request.POST['STR'], 'DEX': request.POST['DEX'], 'CON': request.POST['CON'], 'INT': request.POST['INT'], 'WIS': request.POST['WIS'], 'CHA': request.POST['CHA']}
    Attribute.objects.addAttribute(data, request.session['character'])
    return redirect(reverse("characters:profile"))

def charCreate(request):
    try:
        User.objects.get(id = request.session['id'])
    except:
        return redirect(reverse('login:home'))
    return render(request, 'characters/charCreate.html')
