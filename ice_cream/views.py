from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import IceCream

def daily(request):

    ice_cream_list = IceCream.objects.filter(available='Daily')
    context = {
        'ice_cream_list': ice_cream_list,
        'heading': 'Daily ice cream flavors!'
    }
    return render(request, 'ice_cream/ice_cream_list.html', context)

def weekly(request):
    ice_cream_list = IceCream.objects.filter(available='Weekly')
    context = {
        'ice_cream_list': ice_cream_list,
        'heading': 'Weekly ice cream flavors!'
    }
    return render(request, 'ice_cream/ice_cream_list.html', context)

def seasonal(request):
    ice_cream_list = IceCream.objects.filter(available='Seasonal')
    context = {
        'ice_cream_list': ice_cream_list,
        'heading': 'Seasonal ice cream flavors!'
    }
    return render(request, 'ice_cream/ice_cream_list.html', context)

def featured(request):
    ice_cream_list = IceCream.objects.filter(available='Featured')
    context = {
        'ice_cream_list': ice_cream_list,
        'heading': 'Featured ice cream flavors!'
    }
    return render(request, 'ice_cream/ice_cream_list.html', context)

def all(request):
    ice_cream_list = IceCream.objects.all()
    context = {
        'ice_cream_list': ice_cream_list,
        'heading': 'All ice cream flavors!'
    }
    return render(request, 'ice_cream/ice_cream_list.html', context)
#pk is primary key
# def like(request, pk):
#     ice_cream = get_object_or_404(IceCream, pk=pk)
#     ice_cream.likes += 1
#     ice_cream.save()
#     return HttpResponseRedirect(reverse('ice_cream:index'))
