from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# --------------------------------------------------------------
# HTML email
# --------------------------------------------------------------
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

    # mail for me
        html_content = render_to_string("contact/email_for_me.html",{
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
        html_content = render_to_string("contact/email_for_client.html",{
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
    return render(request, 'contact/index.html', {})

# --------------------------------------------------------------
# no HTML email
# --------------------------------------------------------------
# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         data = {
#                 'name': name,
#                 'email': email,
#                 'subject': subject,
#                 'message': message
#                 }

#         msg = '''
#         New message: {}

#         From: {}
#         '''.format(data['message'], data['email'])

#         send_mail(data['subject'], msg, '', ['linux@nook17.pl'])
#     return render(request, 'contact/index.html', {})
