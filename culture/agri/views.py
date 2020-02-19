from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    catego = Categories.objects.filter(statut=True)[:2]
    categos = Categories.objects.filter(statut=True)[2:]
    categoe = Categories.objects.filter(statut=True)
    product = Produit.objects.filter(statut=True)
    print(catego)
    data = {
        'catego': catego,
        'categoe': categoe,
        'categos': categos,
        'product': product,
    }
    return render(request, 'pages/index.html', data)

def element(request, id):
    elements = Produit.objects.filter(categorie__id= id)
    # element = Produit.objects.all()
    # element_list = Produit.objects.filter(statut=True)
    paginator = Paginator(elements, 4) # Show 25 elements per page

    page = request.GET.get('page')
    elements = paginator.get_page(page)
    data = {
        'elements': elements,
    }
    return render(request, 'pages/element.html', {'elements': elements}, data)

def about(request):
    return render(request, 'pages/about.html')

def cart(request):
    return render(request, 'pages/cart.html')

def checkout(request):
    return render(request, 'pages/checkout.html')

def product(request, id):
    product = Produit.objects.get(id=id)
    products = Produit.objects.filter(statut=True)
    # paginator = Paginator(products, 4) # Show 25 products per page

    # page = request.GET.get('page')
    # products = paginator.get_page(page)
    data = {
        'product': product,
        'products': products,
    }
    return render(request, 'pages/prodsingle.html', data)

def shop(request, id):
    elements = Produit.objects.filter(categorie__id= id)
    catego = Categories.objects.filter(statut=True)
    paginator = Paginator(elements, 4) # Show 25 elements per page

    page = request.GET.get('page')
    elements = paginator.get_page(page)
    data = {
        'elements': elements,
        'catego': catego,
    }
    return render(request, 'pages/shop.html', {'elements': elements}, data)

def wishlist(request):
    return render(request, 'pages/wishlist.html')




def register(request):
    if request.method == "POST" :
        success = False
        username = request.POST.get('username')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        print(nom, prenom, email, contact)
        
        if password == repassword : 
            user = User(
                username=username,
                first_name=prenom,
                last_name=nom,
                email=email,
            )
            try :
                user.save()
                print(user)
                user.profileUser.image=image
                user.profileUser.contact=contact
                user.profileUser.email=email
                user.profileUser.save()
                user.password=password
                user.set_password(user.password)
                user.save()
                # prof = Profile(nom=nom, prenom=prenom, email=email, image=image, contact=contact)
                # prof.save()
                print('************************* succes ***********************************')
                success = True
                response = "votre inscription a ete effectuée avec succes"
                return redirect('connexion')
            except:
                success = False
                response = " error, veillez verifier votre connexion "
                
    return render(request, 'pages/register.html')



def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('******************************************************', username, password )
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active :
            login(request, user)
            return redirect('home')
        else:
            return redirect('connexion')
    return render(request, 'pages/login.html')


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))
