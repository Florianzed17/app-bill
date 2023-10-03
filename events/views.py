import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import send_mail
from django.conf import settings



from django.shortcuts import render, redirect, get_object_or_404
from .models import event

def home(request):
    theme = request.GET.get('theme', '')
    if theme:
        events = event.objects.filter(theme=theme)
    else:
        events = event.objects.all()

    context = {'events': events}
    return render(request, 'index.html', context)

def event_list(request):
    events = event.objects.all()
    context = {'events': events}
    return render(request, 'event_list.html', context)

def event_detail(request, event_id):
    event_obj = get_object_or_404(event, id=event_id)
    context = {'event': event_obj}
    return render(request, 'event_detail.html', context)


def confirmation(request, event_id, total_billet=None):
    # Récupérer les informations de l'événement et la quantité de billets
    event_obj = get_object_or_404(event, id=event_id)
    nombre_billet = request.POST.get('nombre_billet')
    request.session['total_billet'] = nombre_billet

    # Envoyer l'e-mail de confirmation
    # subject = 'Confirmation d\'achat'
    # message = f'Vous avez acheté {total_billet} billet(s) pour l\'événement "{event_obj.nom}".'
    # from_email = settings.DEFAULT_FROM_EMAIL
    # to_email = [request.user.email]  # Modifier avec le champ d'e-mail de l'utilisateur connecté
    # send_mail(subject, message, from_email, to_email)

    context = {
        'event': event_obj,
        'total_billet': total_billet
    }
    return render(request, 'confirmation.html', context)


def achat(request, event_id):
    event_obj = get_object_or_404(event, id=event_id)

    if request.method == 'POST':
        nombre_billet = request.POST.get('ticket_quantity')

        # Vérifier si nombre_billet n'est pas None avant d'appeler isdigit()
        if nombre_billet is not None and nombre_billet.isdigit() and int(nombre_billet) > 0:
            # Effectuer le traitement de l'achat des billets
            return render(request, 'confirmation.html')

    context = {
        'event': event_obj
    }
    return render(request, 'achat.html', context)

from django.shortcuts import render

def search_results(request):
    if request.method == "GET":
        query = request.GET.get('search_query')

        # Logique de recherche et récupération des résultats
        results = event.objects.filter(nom__contains=query)  # Recherche par titre

        context = {
            'query': query,
            'results': results,
        }

        return render(request, 'search_results.html', context)