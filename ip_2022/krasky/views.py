from django.shortcuts import render
from .models import Krasky_vnut, Krasky_nar, Krasky_aero, Krasky_rust
from django.views.generic import DetailView


# Create your views here.

def krasky(request):
    return render(request, 'krasky/krasky.html')

def krasky_vd(request):
    return render(request, 'krasky/krasky_vd.html')

def krasky_vnut(request):
    data = Krasky_vnut.objects.all()
    return render(request, 'krasky/krasky_vnut.html', {'data': data})

class KraskyvnutDetailView(DetailView):
    model = Krasky_vnut
    template_name = 'krasky/krasky_vnut_detail.html'
    context_object_name = 'krasky_vnut'

def krasky_nar(request):
    data_1 = Krasky_nar.objects.all()
    return render(request, 'krasky/krasky_nar.html', {'data_1': data_1})

class KraskynarDetailView(DetailView):
    model = Krasky_nar
    template_name = 'krasky/krasky_nar_detail.html'
    context_object_name = 'krasky_nar'

def krasky_pf(request):
    return render(request, 'krasky/krasky_pf.html')

def krasky_aero(request):
    data_2 = Krasky_aero.objects.all()
    return render(request, 'krasky/krasky_aero.html', {'data_2': data_2})

class KraskyaeroDetailView(DetailView):
    model = Krasky_aero
    template_name = 'krasky/krasky_aero_detail.html'
    context_object_name = 'krasky_aero'

def krasky_rust(request):
    data_3 = Krasky_rust.objects.all()
    return render(request, 'krasky/krasky_rust.html', {'data_3': data_3})

class KraskyrustDetailView(DetailView):
    model = Krasky_rust
    template_name = 'krasky/krasky_rust_detail.html'
    context_object_name = 'krasky_rust'


