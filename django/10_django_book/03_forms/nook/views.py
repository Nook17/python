from django.shortcuts import render, redirect
from .forms import NookForm, NookForm3


def index(request):
    return render(request, 'index.html')


def form1(request):
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))
    context = {"method": request.method}
    return render(request, 'form1.html', context)


# Przesłanie formularza BEZ WALIDACJI
# def form2(request):
#     form = NookForm()               # Formularz niepowiązany. Nie przesyła danych do walidacji
#     for name in request.POST:
#         print("{}: {}".format(name, request.POST.getlist(name)))
#     context = {"form": form}
#     return render(request, 'form2.html', context)


# Przesłanie formularza Z WALIDACJĄ
def form2(request):
    if request.method == 'POST':
        form = NookForm(request.POST)   # Formularz powiązany. Przesyła dane do walidacji
    else:
        form = NookForm()
    if form.is_valid():
        # return redirect('/successSendForm2.html')
        for name, value in form.cleaned_data.items():   # cleaned_data przekształca dane z formularza w obiekty ...
            print("{}: {}".format(name, value))         # ... i przekształca je w słownik
        return render(request, 'successSendForm2.html')
    context = {"form": form}
    return render(request, 'form2.html', context)


def form3(request):
    if request.method == 'POST':
        form = NookForm3(request.POST)
    else:
        form = NookForm3()
    if form.is_valid():
        for name, value in form.cleaned_data.items():
            print("{}: {}".format(name, value))
    context = {"form": form}
    return render(request, 'form3.html', context)


def successSendForm2(request):
    return render(request, 'successSendForm2.html')

