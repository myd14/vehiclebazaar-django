from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.car_list, name='car_list'),
    path('cars/add/', views.car_create, name='car_create'),
    path('site-ads/', views.site_ads, name='site_ads'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),
    path('cars/<int:pk>/edit/', views.car_update, name='car_update'),
    path('cars/<int:pk>/delete/', views.car_delete, name='car_delete'),
    path('cars/<int:pk>/archive/', views.archive_car, name='archive_car'),
    path('cars/<int:pk>/activate/', views.activate_car, name='activate_car'),
    path('cars/<int:pk>/message/', views.send_message, name='send_message'),
    path('cars/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('register/', views.register, name='register'),
    path('signout/', views.signout_view, name='signout'),
]