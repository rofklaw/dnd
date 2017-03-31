from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from ..logreg.models import User, Admin
from .forms import ProductForm
from .models import Product, Cart

import stripe
stripe.api_key = "sk_test_kqjvn71sExbxXooSaRrcSYrg"



def index(request):
<<<<<<< HEAD
    pass
    # products = Product.objects.all()
    # for product in products:
    #     print product.name
    #     print product.picture
    # data = {
    # 'privilege': 0,
    # 'merch': products
    # }
    # try:
    #     # user = User.objects.get(id = request.session['id'])
    #     admincheck = Admin.objects.get(users__id = request.session['id'])
    #     data['privilege'] = admincheck.privilege_level
    #     print "tried"
    # except:
    #     pass
    # print data['privilege']
    # print request.session['id']
    #
    # return render(request, 'store/index.html', data)

=======
>>>>>>> 750e508706ff24652942588bca32b171c5787094
    cart_id = request.session['id']
    products = Product.objects.all()
    for product in products:
        print product.name
        print product.picture
    data = {
    'privilege': 0,
    'merch': products,
    'id': cart_id
    }
    try:
        user = User.objects.get(id = request.session['id'])
        admincheck = Admin.objects.get(users__id = request.session['id'])
        data['privilege'] = admincheck.privilege_level
        print "tried"
    except:
        pass
    print data['privilege']
    print request.session['id']

    return render(request, 'store/index.html', data)
<<<<<<< HEAD
=======

>>>>>>> 750e508706ff24652942588bca32b171c5787094
def curate(request):
    form = ProductForm()
    context = {
    'newproduct': form
    }
    return render(request, 'store/curate.html', context)

def create_merch(request):
<<<<<<< HEAD
    pass
    # try:
    #     admincheck = Admin.objects.get(users__id = request.session['id'])
    # except:
    #     return redirect(reverse('store:index'))
    # Product.objects.create(name = request.POST['name'], description = request.POST['description'], picture = request.FILES['picture'], price = request.POST['price'], admin = admincheck)
    # return redirect(reverse('store:index'))
=======
>>>>>>> 750e508706ff24652942588bca32b171c5787094
    try:
        admincheck = Admin.objects.get(users__id = request.session['id'])
    except:
        return redirect(reverse('store:index'))
    Product.objects.create(name = request.POST['name'], description = request.POST['description'], picture = request.FILES['picture'], price = request.POST['price'], admin = admincheck)
    return redirect(reverse('store:index'))

def add_to_cart(request, id):
    try:
        cart = Cart.objects.get(user__id = request.session['id'])
        print 'got cart'
    except:
        user = User.objects.get(id = request.session['id'])
        cart = Cart.objects.create(user = user)
    product = Product.objects.get(id = id)
    print cart.id
    request.session['cart_id'] = cart.id
    print product.name
    print product.id
    cart.products.add(product)
    print request.session['id']
    print cart
    return redirect(reverse('store:show_cart'))

def remove_from_cart(request, id):
    Cart.objects.get(products__id = id).delete()
    return redirect(reverse('store:show_cart'))

def show_cart(request):
    cart = Product.objects.filter(cart__id = request.session['cart_id'])
    print Cart.products.filter(user__id = request.session['id'])
    total = Cart.objects.total(request.session['cart_id'])
    stripe_total = total * 100
    counter = 0
    for product in cart:
        print product.name
        counter += 1
    print counter
    cart_info = {
        'cart': cart,
        'total': total,
        'stripe_total': stripe_total

    }
    return render(request, 'store/show_cart.html', cart_info)

def pay(request):
    total = Cart.objects.total(request.session['cart_id'])
    stripe_total = int(total * 100)
    token = request.POST['stripeToken']
    charge = stripe.Charge.create(
        amount=stripe_total,
        currency="usd",
        description="Example charge",
        source=token,
    )
    Cart.objects.filter(user_id = request.session['id']).delete()
    return redirect(reverse('store:index'))
