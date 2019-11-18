from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def cart(request):
    return render(request, 'pages/cart.html')

def checkout(request):
    return render(request, 'pages/checkout.html')

def product(request):
    return render(request, 'pages/prodsingle.html')

def shop(request):
    return render(request, 'pages/shop.html')

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
                user.profile.image=image
                user.profile.contact=contact
                user.profile.save()
                user.password=password
                user.set_password(user.password)
                user.save()
                # prof = Profile(nom=nom, prenom=prenom, email=email, image=image, contact=contact)
                # prof.save()
                print('************************* succes ***********************************')
                success = True
                response = "votre inscription a ete effectuée avec succes"
                return redirect('pages/login.html')
            except:
                success = False
                response = " error, veillez verifier votre connexion "
                
    return render(request, 'pages/register.html')



def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('******************************************************', username, password ,'******************************************************')
        try:
            user = authentificate(username=username, password=password)
            if user is not None and user.is_active :
                login(request, user)
                return redirect('pages/index.html')
        except:
            return redirect('connexion')
    return render(request, 'pages/login.html')


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))
