from django.shortcuts import render

# Create your views here.

def index(request):
    name = {
        'title': 'ИП Воробьев В.А.'
    }
    return render(request, 'main/index.html', name)

def catalog(request):
    return render(request, 'main/catalog.html')

def contact(request):
    return render(request, 'main/contact.html')