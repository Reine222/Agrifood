from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def contact(request):
    return render(request, 'pages/contact.html')



def sendContact(request):
    postdata = json.loads(request.body.decode('utf-8'))
    nom = postdata['nom']
    email = postdata['email']
    sujet = postdata['sujet']
    message = postdata['message']
    succes = False
    try:
        contact = Contact()
        contact.nom = nom
        contact.email = email
        contact.sujet = sujet
        contact.message = message
        contact.save()
        succes = True
        reponse = 'Votre message a bien été enregisté '
    except:
        succes = False
        reponse = "Un probleme survennu lors de l'enregistrement"

    datas = {
        'succes':succes,
        'reponse':reponse,
    }
    
    return JsonResponse(datas, safe=False)