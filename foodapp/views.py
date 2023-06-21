from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

# Create your views here.


def index(request):
    if request.method == "POST":
        cart_id = request.POST.get('cartid')
        cartQ = {'cartQ': cart_id}
        return render(request, 'home.html', context=contaxt)

    catid = request.GET.get('cat_id')
    catitems = Category.objects.all()
    fooditem = Fooditem.objects.filter(category=catid)

    contaxt = {'catitems': catitems, 'fooditem': fooditem}

    return render(request, 'home.html', context=contaxt)


def handleSignup(request):
    if request.method == "POST":
        username = request.POST['Rusername']
        fname = request.POST['name']
        email = request.POST['email']
        password = request.POST['Rpassword']
        cpass = request.POST['cpassword']

        if (len(username) > 10):
            return HttpResponse("Username should be less than 10 characters")
        if (password != cpass):
            return HttpResponse("Password does not match")

        main_obj = User.objects.create_user(username, email, password)
        main_obj.save()
        return redirect('home')

    else:
        return HttpResponse("404 Not Found")


def handleLogin(request):
    if request.method == "POST":
        lusername = request.POST['username']
        lpass = request.POST['password']

        user = authenticate(username=lusername, password=lpass)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Please try again")
    else:
        return HttpResponse("404 Not Found")


def handleLogout(request):
    logout(request)
    return redirect('home')


def contact(request):
    return render(request, 'contact.html')


def order(request):
    if request.method == "POST":
        food_id = request.POST.get('cartid')
        remove = request.POST.get('minus')
        cart_id = request.session.get('cart')

        if cart_id:
            print("You clicked")
            quantity = cart_id.get(food_id)
            if quantity:
                cart_id[food_id] = quantity+1
                print("Here your quantity", quantity)
                if remove <= 1:
                    cart_id.pop(food_id)
                    if quantity:
                        cart_id[food_id] = quantity - 1
                    else:
                        cart_id[food_id] = quantity + 1
                else:
                    cart_id[food_id] = 1
            else:
                cart_id = {}
                cart_id[food_id] = 1
            request.session['cart'] = cart_id
            print(request.session['cart'])

    catid = request.GET.get('cart_id')
    print("You id", catid)
    if catid:
        catitems = Fooditem.objects.filter(category=catid)
    else:
        catitems = Fooditem.objects.all()

    context = {'catitem': catitems}

    return render(request, 'order.html', context=context)


def about(request):
    return render(request, 'about.html')


def search(request):
    search = request.GET['search']
    if len(search) > 80:
        search_item = Fooditem.objects.none()

    else:
        search_item = Fooditem.objects.filter(food_name=search)
        content = Fooditem.objects.filter(food_description=search)
        allitem = search_item.union(content)
        context = {'sitem': allitem, 'query': search}

    return render(request, 'search.html', context=context)
