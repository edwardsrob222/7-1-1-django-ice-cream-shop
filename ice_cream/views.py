from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import IceCream

def daily(request):

    ice_cream_list = IceCream.objects.filter(available='DAILY')
    context = {
        'ice_cream_list': ice_cream_list,
        'heading': 'Daily ice cream flavors!'
    }
    return render(request, 'ice_cream/ice_cream.html', context)

def weekly(request):
    ice_cream_list = IceCream.objects.filter(available='WEEKLY')
    context = {
        'ice_cream_list': ice_cream_list,
        'heading': 'Weekly ice cream flavors!'
    }
    return render(request, 'ice_cream/ice_cream.html', context)

def seasonal(request):
    ice_cream_list = IceCream.objects.filter(available='SEASONAL')
    context = {
        'ice_cream_list': ice_cream_list,
        'heading': 'Seasonal ice cream flavors!'
    }
    return render(request, 'ice_cream/ice_cream.html', context)

def featured(request):
    ice_cream_list = IceCream.objects.filter(available='FEATURED')
    context = {
        'ice_cream_list': ice_cream_list,
        'heading': 'Featured ice cream flavors!'
    }
    return render(request, 'ice_cream/ice_cream.html', context)
