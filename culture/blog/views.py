from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
import json
from datetime import datetime, timedelta, timezone, tzinfo



# Create your views here.
def blog(request):
    return render(request, 'pages/blog.html')


def single(request):
    return render(request, 'pages/single.html')



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
