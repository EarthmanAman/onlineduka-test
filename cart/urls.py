from django.contrib import admin
from django.urls import path

from . views import (
	createCartProd,
	updateCartProd,
	deleteCartProd,

	checkout,
	orders,
	cart,
	cartDetail,
	completedOrders,
	)

app_name = "cart"

urlpatterns = [
    path('create/<slug:prodSlug>/', createCartProd, name="createCartProd"),
    path('update/<int:cartProdId>/cartprod/', updateCartProd, name="updateCartProd"),
    path('delete/<int:cartProdId>/cartprod/', deleteCartProd, name="deleteCartProd"),

    path('checkout/', checkout, name="checkout"),
    path('orders/', orders, name="orders"),
    path('complete-orders/', completedOrders, name="completedOrders"),
    path('', cart, name="cart"),

    path('<int:cartId>/', cartDetail, name="cartDetail"),
]
