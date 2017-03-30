from __future__ import unicode_literals
from ..logreg.models import User
from django.db import models
import math

class charManager(models.Manager):
    def addCharacter(self, data, id):
        user = User.objects.get(id=id)
        character = self.create(user=user, name=data['name'], level=data['level'], experience=data['exp'], my_class=data['class'], race=data['race'], background=data['background'], alignment=data['alignment'])


class Character(models.Model):
    user = models.ForeignKey(User, related_name="my_characters")
    name = models.CharField(max_length = 100)
    level = models.IntegerField()
    experience = models.IntegerField()
    my_class = models.CharField(max_length = 50)
    race = models.CharField(max_length = 50)
    background = models.CharField(max_length = 50)
    alignment = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = charManager()

class attrManager(models.Manager):
    def addAttribute(self, data, name):
        character = Character.objects.get(name=name)
        modList = {}
        for attr in data:
            mod = -5
            mod += int(data[attr])/2
            modList[attr] = mod
        atrributes = Attribute.objects.create(character=character, strength=data['STR'], strModifier=modList['STR'], dexterity=data['DEX'], dexModifier=modList['DEX'], constitution=data['CON'], conModifier=modList['CON'],
        intelligence=data['INT'], intModifier=modList['INT'], wisdom=data['WIS'], wisModifier=modList['WIS'], charisma=data['CHA'], chaModifier=modList['CHA'])


class Attribute(models.Model):
    character = models.ForeignKey(Character, related_name="attributes")
    strength = models.IntegerField()
    strModifier = models.IntegerField()
    dexterity = models.IntegerField()
    dexModifier = models.IntegerField()
    constitution = models.IntegerField()
    conModifier = models.IntegerField()
    intelligence = models.IntegerField()
    intModifier = models.IntegerField()
    wisdom = models.IntegerField()
    wisModifier = models.IntegerField()
    charisma = models.IntegerField()
    chaModifier = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = attrManager()

class Equipment(models.Model):
    character = models.ForeignKey(Character, related_name="my_equipment")
    equipment = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
