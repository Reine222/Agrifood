from django.shortcuts import render

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
    return render(request, 'pages/register.html')


def sendRegister(request):
    postdata = json.loads(request.body.decode('utf-8'))
    username = postdata['username']
    nom = postdata['nom']
    email = postdata['email']
    prenom = postdata['prenom']
    message = postdata['message']
    contact = postdata['contact']
    print(nom, prenom, email, message, contact)
    
    if password == repeat_pass:
            user = User(
                username=username,
                first_name=nom,
                last_name=prenom,
                email=email,
                
            )
            try:
                user.save()
                user.profile.contact=contact
                user.profile.image=image
                user.profile.save()
                user.password = password
                user.set_password(user.password)
                user.save()
                print('success')
                succes = True
                reponse = 'Votre inscription a bien été enregisté '
                return redirect('login')
            except:
                print('error')
                succes = False
                reponse = "Un probleme survennu lors de l'enregistrement"
                
            
            datas = {
                'succes':succes,
                'reponse':reponse,
            }
    return JsonResponse(datas, safe=False)



def connexion(request):
    return render(request, 'pages/login.html')

def connect(request):
    postdata = json.loads(request.body.decode('utf-8'))
    username = postdata['username']
    password = postdata['password']
    print(username,password)
    print(user)
    if user is not None and user.is_active:
        try : 
            print("user is login")
            login(request, user)
            return redirect('blog')
        except :
            print("user is not login")
            return redirect('connexion')
    return JsonResponse(datas, safe=False)



def deconection(request):
    logout(request)
    return redirect('connexion')