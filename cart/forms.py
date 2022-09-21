from django import forms
from . models import (
	Cart,
	CartProd
	)


class CreateCartProdForm(forms.ModelForm):

	class Meta:
		model = CartProd
		fields = [
			'prod',
			'quantity',
		]