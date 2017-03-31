from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    try:
        User.objects.get(id = request.session['id'])
    except:
        return redirect(reverse('login:home'))
    return render(request, 'compendium/tester.html')
