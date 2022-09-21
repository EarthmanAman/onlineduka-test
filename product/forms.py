from django import forms
from . models import (
	Category,
	SubCategory,
	Prod,
	ProdMedia,
	)

class CreateCategoryForm(forms.ModelForm):

	class Meta:
		model = Category
		fields = [
			'name',
			'pic'
		]

class CreateSubCategoryForm(forms.ModelForm):
	
	class Meta:
		model = SubCategory
		fields = [
			'category',
			'name',
			'pic'
		]


class CreateProdForm(forms.ModelForm):
	
	class Meta:
		model = Prod
		fields = [
			'subCategory',
			'name',
			'desc',
			'detail',
			'status',
			'origPrice',
			'price',
			'hotDeal',
			'special',
			'keywords'
		]

		widgets = {
			"subCategory": forms.Select(attrs={"class":"form-control"}),
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "status":forms.TextInput(attrs={"class":"form-control"}),
            "origPrice":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "hotDeal": forms.CheckboxInput(attrs={"class":"form-control"}),
            "special": forms.CheckboxInput(attrs={"class":"form-control"}),
		}

class CreateProdMediaForm(forms.ModelForm):
	
	class Meta:
		model = ProdMedia
		fields = [
			# 'prod',
			'pic',
		]
