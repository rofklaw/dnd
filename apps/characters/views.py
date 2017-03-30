from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..logreg.models import User
from .models import Character, Attribute


# Create your views here.
def profile(request):
    context = {
    "user": User.objects.get(id=request.session['id']),
    "Attributes":Attribute.objects.filter(character__user__id=request.session['id'])
    }
    return render(request, 'characters/profile.html', context)

def create(request):
    Character.objects.addCharacter(request.POST.copy(), request.session['id'])
    character = Character.objects.get(name=request.POST['name'])
    request.session['character'] = character.name
    return redirect(reverse("characters:charCreate"))

def createAttb(request):
    data = {'STR': request.POST['STR'], 'DEX': request.POST['DEX'], 'CON': request.POST['CON'], 'INT': request.POST['INT'], 'WIS': request.POST['WIS'], 'CHA': request.POST['CHA']}
    Attribute.objects.addAttribute(data, request.session['character'])
    return redirect(reverse("characters:profile"))

def charCreate(request):
    return render(request, 'characters/charCreate.html')
