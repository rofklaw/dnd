from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..logreg.models import User, Admin
from .forms import ProductForm
from .models import Product, Cart


def index(request):
    products = Product.objects.all()
    for product in products:
        print product.name
        print product.picture
    data = {
    'privilege': 0,
    'merch': products
    }
    try:
        # user = User.objects.get(id = request.session['id'])
        admincheck = Admin.objects.get(users__id = request.session['id'])
        data['privilege'] = admincheck.privilege_level
        print "tried"
    except:
        pass
    print data['privilege']
    print request.session['id']

    return render(request, 'store/index.html', data)

def curate(request):
    form = ProductForm()
    context = {
    'newproduct': form
    }
    return render(request, 'store/curate.html', context)

def create_merch(request):
    try:
        admincheck = Admin.objects.get(users__id = request.session['id'])
    except:
        return redirect(reverse('store:index'))
    Product.objects.create(name = request.POST['name'], description = request.POST['description'], picture = request.FILES['picture'], price = request.POST['price'], admin = admincheck)
    return redirect(reverse('store:index'))
