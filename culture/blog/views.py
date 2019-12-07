from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
import json
from agri.models import Profile
from .models import *
from datetime import datetime, timedelta, timezone, tzinfo



# Create your views here.
def blog(request):
    categories = Categorie.objects.filter(statut=True)
    articles = Article.objects.filter(statut=True)
    commentaires = Commentaire.objects.filter(statut=True)
    tag = Tag.objects.filter(statut=True)
    data = {
        'categories': categories,
        'articles': articles,
        'commentaires': commentaires,
        'tag': tag,
    }
    return render(request, 'pages/blog.html',data)


def single(request, id):
    # print(pk)
    article = Article.objects.filter(statut=True)
    arti = Article.objects.get(id=id)
    commentaires = Commentaire.objects.filter(article__id=id)
    art = Article.objects.filter()
    tag = Tag.objects.filter(statut=True)
    catego = Categorie.objects.filter(statut=True)
    data = {
        'article': article,
        'arti': arti,
        'art': art,
        'tag': tag,
        'catego': catego,
        'commentaires': commentaires,
    }
    return render(request, 'pages/single.html',data)

def sendcomment(request):
    if request.method == "POST" :
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        web = request.POST.get('web')
        message = request.POST.get('message')
        print('********************************', nom, email, web, message  ,'***************************************')
        if nom is not None and email is not None and web is not None and message is not None :
            comment = Comment(nom=nom, email=email, web=web, message=message)
            comment.save()
        else:
            print('******************************** message non envoyé ***************************************')
    else:
        return redirect('blog')
    return redirect(reverse(single))

# def register(request):
#     if request.method == "POST" :
#         success = False
#         username = request.POST.get('username')
#         nom = request.POST.get('nom')
#         prenom = request.POST.get('prenom')
#         email = request.POST.get('email')
#         image = request.FILES.get('image')
#         contact = request.POST.get('contact')
#         print(nom, prenom, email, message, contact)
        
#         if password == repassword : 
#             user = User(
#                 username = username,
#                 first_name = prenom,
#                 last_name = nom,
#                 email = email,
#             )
#             try :
#                 user.save()
#                 print(user)
#                 user.profile.image = image
#                 user.profile.contact = contact
#                 user.profile.save()
#                 user.password = password
#                 user.set_password(user.password)
#                 user.save()
#                 print('************************* succes ***********************************')
#                 success = True
#                 response = "votre inscription a ete effectuée avec succes"
#                 return redirect('connexion')
#             except:
#                 success = False
#                 response = " error, veillez verifier votre connexion "
                
#             data = {
#                 'succes':succes,
#                 'reponse':reponse,
#             }
#     return render(request, 'pages/register.html', data)



# def connexion(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authentificate(username = username, password = password)
#         if user :
#             login(request, user)
#             print(user)
#             return redirect('blog')
#     return render(request, 'pages/login.html')


# def deconnexion(request):
#     logout(request)
#     return redirect(reverse(connexion))
