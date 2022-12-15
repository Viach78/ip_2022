from django.shortcuts import render
from .models import Panely_pvh, Ugolky, Complect_pvh
from django.views.generic import DetailView



def panely(request):
    return render(request, 'panely/panely_pvh.html')

class PanelyDetailView(DetailView):
    model = Panely_pvh
    template_name = 'panely/panely_detail.html'
    context_object_name = 'panely_pvh'


def pvh_bel(request):
    data = Panely_pvh.objects.all()
    return render(request, 'panely/pvh_bel.html', {'data': data})

def ugly(request):
    data_1 = Ugolky.objects.all()
    return render(request, 'panely/ugol.html', {'data_1': data_1})

class UgolkyDetailView(DetailView):
    model = Ugolky
    template_name = 'panely/ugol_detail.html'
    context_object_name = 'ugolky'

def complect_pvh(request):
    data_2 = Complect_pvh.objects.all()
    return render(request, 'panely/complect_pvh.html', {'data_2': data_2})

class ComplectDetailView(DetailView):
    model = Complect_pvh
    template_name = 'panely/complect_pvh_detail.html'
    context_object_name = 'complect_pvh'
