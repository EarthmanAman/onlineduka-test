from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify

from . models import (
	Category,
	SubCategory,
	Prod,
	ProdMedia,
	RequestProd,
	)

from . forms import (
	CreateCategoryForm,
	CreateSubCategoryForm,
	CreateProdForm,
	CreateProdMediaForm,
	)
"""

"""


# def categoryProds(param=None):
# 	if param

def index(request):
	template_name = './main/index.html'
	specials = Prod.objects.filter(special=True)
	subCategories = SubCategory.objects.all()
	hotDeals = Prod.objects.filter(hotDeal=True)
	newArrivals = Prod.objects.all().order_by('-pk')[:8]
	topSellings = Prod.objects.all()[:20]
	prods = Prod.objects.all()[:12]
	context = {
		'subCategories':subCategories, 
		'hotDeals':hotDeals, 
		'specials':specials, 
		'prods':prods,
		'newArrivals':newArrivals,
		'topSellings':topSellings,
		} 
	return render(request, template_name, context)

def shop(request, subCategorySlug):
	template_name = './main/shop.html'
	category = request.GET.get('category')
	cat = False
	if category:
		#category = get_object_or_404(Category, name=name)
		prods = Prod.objects.filter(subCategory__category__name=category)
		cat = True
	else:
		subCategory = get_object_or_404(SubCategory, slug=subCategorySlug)
		prods = subCategory.prod_set.all().order_by('-pk')
	# subCategories = subCategory.category.subcategory_set.exclude(slug=subCategorySlug)
	hotDeals = Prod.objects.filter(hotDeal=True)
	context = {'prods':prods, 'hotDeals':hotDeals, 'cat':cat}
	return render(request, template_name, context)

@login_required
def prods(request):
	template_name = './main/prods.html'
	prods = Prod.objects.all().order_by('-pk')[:20]
	search = request.GET.get('subCategory')
	subCategories = SubCategory.objects.all()
	if search:
		subCategory = get_object_or_404(SubCategory, slug=search)
		prods = Prod.objects.filter(subCategory=subCategory)
	context = {'prods':prods, 'subCategories':subCategories}
	return render(request, template_name, context)

def prodDetail(request, prodSlug):
	template_name = './main/prodDetail.html'
	prod = get_object_or_404(Prod, slug=prodSlug)
	relatedProds = prod.subCategory.prod_set.all()
	context = {'prod':prod, 'relatedProds':relatedProds}
	return render(request, template_name, context)

def search(request):
	template_name = './main/search.html'
	param = request.GET.get('search')
	noResult = False
	send = False
	prods = Prod.objects.all()
	pop = False
	filterSet = []
	if param:
		#Giving preferences to names first

		filterSet.extend(prods.filter(
			Q(name__icontains=param)
			).distinct()
			)
		filterSet.extend(prods.filter(
			Q(keywords__icontains=param)|
			Q(subCategory__name__icontains=param)|
			Q(subCategory__category__name__icontains=param)
			).distinct()
			)

	if len(filterSet) == 0:
		noResult = False
		pop = True

	if request.method == "POST":
		prodName = request.POST.get('product')
		phoneNumber = request.POST.get('phoneNumber')
		requestProd = RequestProd(name=prodName)
		if phoneNumber:
			requestProd.phoneNumber = int(phoneNumber)
		requestProd.save()
		noResult = False
		send = True

	context = {'prods':filterSet, 'noResult':noResult, 'send':send, 'pop':pop}
	return render(request, template_name, context)
"""
Category section
"""
#Will display together with Subcategories
@login_required
def categories(request):
	if request.user.is_superuser:
		template_name = './categories.html'
		categories = Category.objects.all()
		context = {'categories':categories}
		return render(request, template_name, context)
	else:
		return redirect('product:noPerm')

@login_required
def createCategory(request):
	if request.user.is_superuser:
		template_name = './form/createCategory.html'
		if request.method == "POST":
			form = CreateCategoryForm(request.POST)
			if form.is_valid():
				newForm = form.save(commit=False)
				newForm.slug = slugify(newForm.name)
				newForm.save()
				return redirect("product:categories")
		else:
			form = CreateCategoryForm()

		context = {"form":form}
		return render(request, template_name, context)
	else:
		return redirect('product:noPerm')

@login_required
def updateCategory(request, categorySlug):
	if request.user.is_superuser:
		template_name = './form/updateCategory.html'
		category = get_object_or_404(Category, slug=categorySlug)
		if request.method == "POST":
			form = CreateCategoryForm(request.POST, request.FILES, instance=category)
			if form.is_valid():
				newForm = form.save()
				newForm.slug = slugify(newForm.name)
				newForm.save()
				return redirect('product:categories')
		else:
			form = CreateCategoryForm(instance=category)
		context = {'form':form}
		return render(request, template_name, context)
	else:
		return redirect('product:noPerm')

@login_required
def deleteCategory(request, categorySlug):
	if request.user.is_superuser:
		category = get_object_or_404(Category, slug=categorySlug)
		category.delete()
		return redirect('product:categories')
	else:
		return redirect('product:noPerm')


"""
Subcategory section
"""
@login_required

@login_required
def createSubCategory(request):
	if request.user.is_superuser:
		template_name = './form/createSubCategory.html'
		if request.method == "POST":
			form = CreateSubCategoryForm(request.POST, request.FILES)
			if form.is_valid():
				newForm = form.save(commit=False)
				newForm.slug = slugify(newForm.name)
				newForm.save()
				return redirect('product:categories')
		else:
			form = CreateSubCategoryForm()
		context = {"form":form}
		return render(request, template_name, context)
	else:
		return redirect('product:noPerm')

@login_required
def updateSubCategory(request, subCategorySlug):
	if request.user.is_superuser:
		template_name = './form/updateSubCategory.html'
		subCategory = get_object_or_404(Subcategory, slug=subCategorySlug)
		if request.method == "POST":
			form = CreateSubCategoryForm(request.POST, request.FILES, instance=subCategory)
			if form.is_valid():
				newForm = form.save(commit=False)
				newForm.slug = slugify(newForm.name)
				newForm.save()
				return redirect('product:categories')
		else:
			form = CreateSubCategoryForm(instance=subCategory)
		context = {'form':form}
		return render(request, template_name, context)
	else:
		return redirect('product:noPerm')

@login_required
def deleteSubCategory(request, subCategorySlug):
	if request.user.is_superuser:
		subCategory = get_object_or_404(Subcategory, slug=subCategorySlug)
		subCategory.delete()
		return redirect('product:categories')
	else:
		return redirect("product:noPerm")

"""
Product section
"""

@login_required
def createProd(request):
	if request.user.is_superuser:
		template_name = './form/createProd.html'
		success = False
		if request.method == "POST":
			form = CreateProdForm(request.POST)
			pic1 = request.FILES.get('pic1', None)
			pic2 = request.FILES.get('pic2', None)
			pic3 = request.FILES.get('pic3', None)
			if form.is_valid():
				newForm = form.save(commit=False)
				last = Prod.objects.last()
				slug = "{0} {1}".format(newForm.name, last.id)
				newForm.slug = slugify(slug)
				try:
					origPrice = form.cleaned_data['origPrice']
					price = form.cleaned_data['price']
					newForm.discount = (origPrice - price)/origPrice *100
				except:
					None
				newForm.save()
				if pic1:
					media1 = ProdMedia(prod=newForm, pic=pic1)
					media1.save()

				if pic2:
					media2 = ProdMedia(prod=newForm, pic=pic2)
					media2.save()

				if pic3:
					media3 = ProdMedia(prod=newForm, pic=pic3)
					media3.save()
				success = True
		else:
			form = CreateProdForm()

		context = {"form":form, 'success':success}
		return render(request, template_name, context)
	else:
		return redirect('product:noPerm')

@login_required
def updateProd(request, prodSlug):
	if request.user.is_superuser:
		template_name = './form/updateProd.html'
		prod = get_object_or_404(Prod, slug=prodSlug)
		success = False
		if request.method == "POST":
			form = CreateProdForm(request.POST, instance=prod)
			pic1 = request.FILES.get('pic1', None)
			pic2 = request.FILES.get('pic2', None)
			pic3 = request.FILES.get('pic3', None)
			if form.is_valid():
				newForm = form.save(commit=False)
				last = Prod.objects.last()
				slug = "{0} {1}".format(newForm.name, last.id)
				newForm.slug = slugify(slug)
				try:
					origPrice = form.cleaned_data['origPrice']
					price = form.cleaned_data['price']
					newForm.discount = (origPrice - price)/origPrice *100
				except:
					None
				newForm.save()
				if pic1:
					try:
						media1 = ProdMedia.objects.get(pk=1)
						media1.pic = pic1
					except:
						media1 = ProdMedia(prod=newForm, pic=pic1)
					media1.save()

				if pic2:
					try:
						media2 = ProdMedia.objects.get(pk=2)
						media2.pic = pic2
					except:
						media2 = ProdMedia(prod=newForm, pic=pic2)
					media2.save()
				if pic3:
					try:
						media3 = ProdMedia.objects.get(pk=3)
						media3.pic = pic3
					except:
						media3 = ProdMedia(prod=newForm, pic=pic3)
					media3.save()
				success = True
		else:
			form = CreateProdForm(instance=prod)

		context = {"form":form, 'success':success}
		return render(request, template_name, context)
	else:
		return redirect('product:noPerm')

@login_required
def deleteProd(request, prodSlug):
	if request.user.is_superuser:
		prod = get_object_or_404(Prod, slug=prodSlug)
		prod.delete()
		return redirect('product:prods')
	else:
		return redirect('product:noPerm')
"""
Prduct Media section
Does not have update if you want just delete the file and add another
"""

@login_required
def createProdMedia(request):
	if request.user.is_superuser:
		template_name = './form/createProdMediaCategory.html'
		if request.method == "POST":
			form = CreateProdMediaForm(request.FILES)
			if form.is_valid():
				form.save()
		else:
			form = CreateProdMediaForm()

		context = {"form":form}
		return render(request, template_name, context)
	else:
		return redirect('product:noPerm')

@login_required
def deleteProdMedia(request, prodMediaSlug):
	if request.user.is_superuser:
		prodMedia = get_object_or_404(ProdMedia, slug=prodMediaSlug)
		prodMedia.delete()
		return redirect('product:products')
	else:
		return redirect('product:noPerm')


def noPerm(request):
	template_name = './errors/noPerm.html'
	return render(request, template_name)

@login_required
def requestProd(request):
	template_name = './main/requestProd.html'
	requestProds = RequestProd.objects.all()
	
	if request.method == "POST":
		requestProdId = int(request.POST.get('id'))
		requestP = get_object_or_404(RequestProd, pk=requestProdId)
		requestP.delete()

	context= {'requestProds':requestProds}
	return render(request, template_name, context)