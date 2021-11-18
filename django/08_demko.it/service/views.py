from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def index(request):
    return render(request, 'service/index.html', {})


def notify(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

    # mail for me
        html_content = render_to_string("service/notify_for_me.html",{
            'subject': subject, 'message': message, 'name': name, 
            'email': email, 'phone': phone})
        text_content = strip_tags(html_content)

        mail = EmailMultiAlternatives(
                #subject
                subject,
                #content
                text_content,
                #from 
                'serwis@demko.it',
                #to
                ['linux@nook17.pl']
                )
        mail.attach_alternative(html_content, "text/html")
        mail.send()

    # mail for client
        html_content = render_to_string("service/notify_for_client.html",{
            'subject': subject, 'name': name})
        text_content = strip_tags(html_content)

        mail = EmailMultiAlternatives(
                #subject
                subject,
                #content
                text_content,
                #from
                'serwis@demko.it',
                #to
                [email]
                )
        mail.attach_alternative(html_content, "text/html")
        mail.send()
    return render(request, 'service/index.html', {})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

    # mail for me
        html_content = render_to_string("service/contact_for_me.html",{
            'subject': subject, 'message': message, 'name': name, 'email': email})
        text_content = strip_tags(html_content)

        mail = EmailMultiAlternatives(
                #subject
                subject,
                #content
                text_content,
                #from 
                'serwis@demko.it',
                #to
                ['linux@nook17.pl']
                )
        mail.attach_alternative(html_content, "text/html")
        mail.send()

    # mail for client
        html_content = render_to_string("service/contact_for_client.html",{
            'subject': subject, 'name': name})
        text_content = strip_tags(html_content)

        mail = EmailMultiAlternatives(
                #subject
                subject,
                #content
                text_content,
                #from
                'serwis@demko.it',
                #to
                [email]
                )
        mail.attach_alternative(html_content, "text/html")
        mail.send()
    return render(request, 'service/index.html', {})

