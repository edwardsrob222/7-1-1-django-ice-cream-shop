from django.urls import path

from . import views

app_name = 'ice_cream'

urlpatterns = [
    path('daily/', views.daily, name='daily'),
    path('weekly/', views.weekly, name='weekly'),
    path('seasonal/', views.seasonal, name='seasonal'),
    path('featured/', views.featured, name='featured'),
]
