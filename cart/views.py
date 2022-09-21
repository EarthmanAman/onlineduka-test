from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from accounts.models import (
	Customer, 
	Agent,
	)
from product.models import Prod
from . forms import CreateCartProdForm
from . models import Cart, CartProd, AgentEarn

"""
Cart product section
"""

def createCartProd(request, prodSlug):
	cartId = request.session.get('cart', None)
	try:
		cart = Cart.objects.get(id=cartId)
		
	except:
		cart = Cart.objects.create(customer=None)
		request.session['cart'] = cart.id

	quantity = request.GET.get('quantity', 1)
	prod = get_object_or_404(Prod, slug=prodSlug)
	try:
		prodIn = cart.cartprod_set.get(prod=prod)
		prodIn.total = prod.price * (int(quantity) + int(prodIn.quantity))
		prodIn.quantity += int(quantity)
		prodIn.save()
		total = prodIn.total
	except:
		total = prod.price * int(quantity)
		cartProd = CartProd(prod=prod, cart=cart, quantity=int(quantity), total=total)
		cartProd.save()
	if cart.cartprod_set.count() == 1:
		cart.total = total
		cart.save()
		if request.is_ajax():
			json_data = {
				"count":cart.cartprod_set.count(),
				"total":cart.total
			}
			print(cart.cartprod_set.count())
			return JsonResponse(json_data)
		return redirect('cart:cart')
	cart.total = float(cart.total) + float(total)
	cart.save()
	url = request.META.get('HTTP_REFERER')
	if request.is_ajax():
		json_data = {
			"count":cart.cartprod_set.count(),
			"total":cart.total
		}
		print(cart.cartprod_set.count())
		return JsonResponse(json_data)

	return redirect(url)


def updateCartProd(request, cartProdId):
	template_name = "./form/updateCartProd.html"
	cartProd = get_object_or_404(CartProd, pk=cartProdId)
	if request.method == "POST":
		form = CreateCartProdForm(request.POST, instance=cartProd)
		if form.is_valid():
			form.save()
			return redirect('cart:cart')
	else:
		form = CreateCartProdForm(instance=cartProd)
	context = {'form':form}
	return render(request, template_name, context)


def deleteCartProd(request, cartProdId):
	# if request.method == "POST":
	# cartProdId = request.POST.get('cartProdId')
	cartProd = get_object_or_404(CartProd, pk=cartProdId)
	cart = cartProd.cart
	cart.total -= cartProd.total
	cartProd.delete()
	if cart.cartprod_set.count() == 0:
		cart.total = 0
	cart.save()
	url = request.META.get('HTTP_REFERER')
	return redirect(url)


def checkout(request, cartId):
	template_name = './checkout.html'
	cart = get_object_or_404(Cart, pk=cartId)
	wrongPromo = False
	if request.method == "POST":
		name = request.POST.get('name')
		location = request.POST.get('location')
		phoneNumber = request.POST.get('phoneNumber')
		promoCode = request.POST.get('promoCode', None)
		try:
			agent = Agent.objects.get(promoCode=promoCode)
		except:
			wrongPromo = True 
			agent = None
		if not wrongPromo:
			customer = Customer(name=name, phoneNumber=phoneNumber)
			cart.location = location
			cart.agent = agent.agentearn_set.last()
			customer.save()
			cart.customer = customer
			cart.isOrdered = True
			cart.save()
			request.session['cart'] = None
	context = {'cart':cart, 'wrongPromo':wrongPromo}
	return render(request, template_name, context)

@login_required
def orders(request):
	if request.user.is_superuser:
		template_name = './orders.html'
		order = None
		orderId = request.GET.get('orderId')
		if orderId:
			order = get_object_or_404(Cart, pk=orderId)

		if request.method == "POST":
			cartId = int(request.POST.get('cartId'))
			cart = get_object_or_404(Cart, pk=cartId)
			cart.isComplete = True
			cart.save()

		carts = Cart.objects.filter(isOrdered=True).filter(isComplete=False).order_by('-pk')
		context = {'carts':carts, 'order':order}
		return render(request, template_name, context)
	else:
		return redirect('product:noPerm')

@login_required
def completedOrders(request):
	if request.user.is_superuser:
		template_name = './completedOrders.html'
		order = None
		orderId = request.GET.get('orderId')
		if orderId:
			order = get_object_or_404(Cart, pk=orderId)

		if request.method == "POST":
			cartId = int(request.POST.get('cartId'))
			cart = get_object_or_404(Cart, pk=cartId)
			cart.isComplete = False
			cart.save()

		orders = Cart.objects.filter(isComplete = True).order_by('-pk')
		context = {'orders':orders, 'order':order}
		return render(request, template_name, context)
	else:
		return redirect('product:noPerm')

def cart(request):
	template_name = './cart.html'
	cart = get_object_or_404(Cart, pk=request.session['cart'])
	wrongPromo = False
	ordered = False


	if request.method == "POST":
		name = request.POST.get('name')
		location = request.POST.get('location')
		phoneNumber = request.POST.get('phoneNumber')
		promoCode = request.POST.get('promoCode', None)

		try:
			agent = Agent.objects.get(promoCode=promoCode)
		except:
			if promoCode != "":
				wrongPromo = True 
			agent = None
		if not wrongPromo:
			customer = Customer(name=name, phoneNumber=phoneNumber)
			
			cart.location = location
			try:
				cart.agent = agent.agentearn_set.last()
			except:
				None
			customer.save()
			cart.customer = customer
			cart.isOrdered = True
			cart.save()
			ordered = True

			request.session['cart'] = None
	context = {'wrongPromo':wrongPromo, 'ordered':ordered}
	return render(request, template_name, context)


@login_required
def cartDetail(request, cartId):
	if request.user.is_superuser:
		template_name = './cartDetail.html'
		cart = get_object_or_404(Cart, pk=cartId)
		context = {'cart': cart}
		return render(request, template_name, context)
	else:
		return redirect('product:noPerm')
