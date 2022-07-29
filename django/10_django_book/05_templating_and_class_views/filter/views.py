from django.shortcuts import render


def index(request):
    names = 'Arek,Nook,Kojo,Kama'
    context = {'names': names}
    return render(request, 'index.html', context)


def tags(request):
    username = 'Nook'
    books = {'Great Django': 'Ben Thomas', 'Python for beginners': 'Alex Hanks'}
    context = {'username': username, 'books': books}
    return render(request, 'simple_tag.html', context)
