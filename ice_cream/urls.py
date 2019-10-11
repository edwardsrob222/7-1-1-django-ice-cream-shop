from django.urls import path

from . import views

app_name = 'ice_cream'

urlpatterns = [
    path('daily/', views.daily, name='daily'),
    path('weekly/', views.weekly, name='weekly'),
    path('seasonal/', views.seasonal, name='seasonal'),
    path('featured/', views.featured, name='featured'),
    path('all/', views.all, name='all'),

    # path('like/', views.like, name='like'),
    # path("", views.index, name='index'),
    path('<int:pk>/delete/', views.delete_view, name='delete'),
    # path('new/', views.CreateView.as_view(), name='ice_cream_new'),
    path('<int:pk>/', views.increment_likes, name='increment_likes'),
    path('add_ice_cream/', views.AddIceCream.as_view(), name='add_ice_cream'),
]
