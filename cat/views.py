
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Menu,Event,Vendor,Package #Customer
#from .models import menu,account,transaction



def signup(request):
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        user = User()
        user.username = username
        user.email = email
        user.password=password
        user.confirm=confirm
        #user.enc_password=hashlib.sha256(str.encode(password)).hexdigest
        #user.enc_confirm=hashlib.sha256(str.encode(confirm))
        if user.password == user.confirm:
            try:
                user.set_password(user.password)
                user.save()
            except Exception as e:
                messages.error(request, "User already exists.")
                return redirect('signup')
            return redirect('user_login')

    return render(request, 'signup.html')

def user_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            request.session.username = user.username
            return redirect('index')

    return render(request, 'login.html')

def vendor_login(request):
    if request.POST:
         vendor_name = request.POST.get('username')
         vendor_password=request.POST.get('password')

         vendor = authenticate(request, username=vendor_name, password=vendor_password)

         if vendor is not None:
            login(request,vendor)
            request.session.username = vendor.username
            return redirect('index')

     return render(request, 'login.html')

def index(request):
    return render(request, 'home.html')

def get_menu(request):
    if request.POST:

        m = Menu(user_name=request.POST.get('name'),
                 user_email=request.POST.get('email'),
                 price=request.POST.get('price'),
                 menu=request.POST.get('menu'))

        m.save()

    return render(request, 'menu.html')

def get_menu_list(request):
    context = {}
    menus = Menu.objects.all()

    context['menulist'] = [{'user_name': i.user_name,
                            'user_email': i.user_email,
                            'price': i.price,
                            'menu': i.menu,
                            } for i in menus]
    return render(request, 'menulist.html', context=context)


#def menulist(request):

    #return render(request, 'pages/menulist.html')

    #return render(request, 'pages/menulist.html')
def book_event(request):
    context = {'user_name': request.user.username}
    if request.POST:
        h = Event()
        h.user_name = request.POST.get('user_name', None)
        h.event_type = request.POST.get('event', None)
        h.capacity= request.POST.get('capacity', None)
        h.save()
        return render(request, 'index.html',context={'msg': 'Event book successfully'})

    return render(request, 'book_event.html', context=context)


def user_logout(request):
    try:
        del request.session['username']
    except:
        pass
    logout(request)
    return redirect('user_login')

def profile(request):

    context = {}
    context['profile'] = User.objects.get(username=request.user.username)
    return render(request, 'profile.html', context=context)

def settings(request):
    context = {}
    context['profile'] = User.objects.get(username=request.user.username)
    return render(request, 'settings.html', context=context)

def vendor(request):
    if request.POST:

        v = Vendor(vendor_name=request.POST.get('name'),
                   vendor_email=request.POST.get('email'),
                   address=request.POST.get('address'),
                   mobileno=request.POST.get('mobileno'))

        v.save()

    return render(request, 'vendor.html')


def package(request):
        if request.POST:

            p= Package(package_name=request.POST.get('name'),
                       price=request.POST.get('price'),
                       disc=request.POST.get('disc'))


            p.save()

        return render(request, 'package.html')

def customer(request):
        if request.POST:

            c= Customer(name=request.POST.get('name'),
                       email=request.POST.get('email'),
                       price=request.POST.get('price'),
                       suggesst=request.POST.get('suggesst'))


            c.save()

        return render(request, 'customer.html')
# Create your views here.
