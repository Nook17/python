from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return render(request, 'challenges/index.html')

# def january(request):
#     return render(request, 'challenges/january.html')

# def february(request):
#     return render(request, 'challenges/february.html')

def nook_func(request, nook_arg):
    if nook_arg == january:
        set_path = 'challenges/january.html'
    elif nook_arg == february:
        set_path = 'challenges/february.html'
    elif nook_arg == march:
        set_path = 'challenges/march'
    else:
        return HttpResponseNotFound(request, 404)
    return render(request, set_path)
        
