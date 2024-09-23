from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('cart/add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'), 
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
