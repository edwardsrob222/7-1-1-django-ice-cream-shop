from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
# Create your views here.



from .models import IceCream


# class IndexView(LoginRequiredMixin, generic.ListView):
#     template_name = 'ice_cream/index.html'
#
#     def get_queryset(self):
#         if 'selection' in self.kwargs:
#             return IceCream.objects.filter(available = self.kwargs['selection'].upper())
#         return IceCream.objects.all()
#
# class CreateView(UserPassesTestMixin, generic.CreateView):
#     model = IceCream
#     template_name = 'ice_cream/ice_cream_new.html'
#     fields = '__all__'
#
#     def test_func(self):
#         return self.request.user.is_superuser
#
#     def handle_no_permission(self):
#         return redirect('ice_cream:index')

# @user_passes_test(is_superuser_check)
def delete_view(request, pk):
    ice_cream = get_object_or_404(IceCream, pk=pk)
    ice_cream.delete()
    return HttpResponseRedirect(reverse_lazy('ice_cream:all'))

def increment_likes(request, pk):
    ice_cream = get_object_or_404(IceCream, pk=pk)
    ice_cream.likes += 1
    ice_cream.save()
    return HttpResponseRedirect(reverse('ice_cream:all'))

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

class AddIceCream(generic.CreateView):
    model = IceCream
    fields = '__all__'
    # fields = ['flavor', 'base', 'featured']
    template_name = 'ice_cream/ice_cream_form.html'



#pk is primary key
# def like(request, pk):
#     ice_cream = get_object_or_404(IceCream, pk=pk)
#     ice_cream.likes += 1
#     ice_cream.save()
#     return HttpResponseRedirect(reverse('ice_cream:index'))
