from __future__ import unicode_literals

from django.db import models
import bcrypt

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class RegistrationManager(models.Manager):
    def regvalidator(self, first_name, last_name, email, password, confirm):
        errors = []
        if len(first_name) < 1 or not first_name.isalpha():
            errors.append("first name cannot be blank and may only be letters")
        if len(last_name) < 1 or not first_name.isalpha():
            errors.append("last name cannot be blank and may only be letters")
        if len(email) < 1:
            errors.append("email cannot be blank")
        if not EMAIL_REGEX.match(email):
            errors.append("must enter a valid email")
        if len(password) < 8:
            errors.append("password must be at least 8 characters long")
        if password != confirm:
            errors.append("passwords do not match")
        return {'errors': errors}
    def bcryptor(self, password):
        hashword = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return {'pwhash': hashword}
    def logvalidator(self, email, password):
        errors = []
        # test = User.objects.filter(email = email )
        # print test['email']

        print email
        print password
        try:
            user = self.get(email = email)
            print user

            if bcrypt.hashpw(password.encode('utf8'), user.pwhash.encode('utf8')) == user.pwhash.encode('utf8'):
                return {'user': user, 'errors': errors}
            errors.append("Incorrect password")
        except:
            errors.append("unrecognized email address")
        return {'errors': errors}
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    pwhash = models.CharField(max_length = 255)
    creted_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = RegistrationManager()

class Admin(models.Model):
    users = models.OneToOneField(User)
    privilege_level = models.IntegerField()
