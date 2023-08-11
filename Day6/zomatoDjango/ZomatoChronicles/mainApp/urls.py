from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/add/', views.add_menu_item, name='add_menu_item'),
    path('menu/update_availability/<int:item_id>/', views.update_availability, name='update_availability'),
    path('menu/delete_dish/<int:item_id>/', views.delete_dish, name='delete_dish'),
     path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'), 
]
