from cart.models import Cart
from . models import Category

def cartIn(request):
	try:
		card_id = request.session.get("cart", None)
		cart = Cart.objects.get(pk=card_id)
	except:
		cart = []
	return {'cartIn': cart}
    
def cats(request):
	cats = Category.objects.all()
	return {'cats':cats}

def pop(request):
	pop = False
	return {'pop':pop}