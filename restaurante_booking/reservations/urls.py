from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('reserve/<int:restaurant_id>/', views.make_reservation, name='make_reservation'),
    path('reservation_success/', views.reservation_success, name='reservation_success'),
]
