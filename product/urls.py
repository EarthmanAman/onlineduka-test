from django.contrib import admin
from django.urls import path

from . views import (
	index,
	shop,
	prodDetail,
	requestProd,
	search,
	prods,

	createCategory,
	createSubCategory,
	createProd,
	createProdMedia,

	updateCategory,
	updateSubCategory,
	updateProd,

	deleteCategory,
	deleteSubCategory,
	deleteProd,
	deleteProdMedia,

	categories,
	noPerm,
	)

app_name = "product"

urlpatterns = [
	path('', index, name="index"),
	path('shop/<slug:subCategorySlug>/', shop, name="shop"),
	path('<slug:prodSlug>/', prodDetail, name="prod"),
	path('all/prods/', prods, name="prods"),
	path('search/product/', search, name="search"),
	path('all/requested_prods/', requestProd, name="requestProd"),

    path('create/category/', createCategory, name="createCategory"),
    path('create/subcategory/', createSubCategory, name="createSubCategory"),
    path('create/prod/', createProd, name="createProd"),
    path('create/prodmedia/', createProdMedia, name="createProdMedia"),

    path('update/<slug:categorySlug>/category/', updateCategory, name='updateCategory'),
    path('update/<slug:subCategorySlug>/subcategory/', updateSubCategory, name='updateSubCategory'),
    path('update/<slug:prodSlug>/prod/', updateProd, name='updateProd'),

    path('delete/<slug:categorySlug>/category/', deleteCategory, name='deleteCategory'),
    path('delete/<slug:subCategorySlug>/subcategory/', deleteSubCategory, name='deleteSubCategory'),
    path('delete/<slug:prodSlug>/prod/', deleteProd, name='deleteProd'),
    path('delete/<slug:prodMediaSlug>/prodmedia/', deleteProdMedia, name='deleteProdMedia'),

    path('all/categories/', categories, name="categories"),
    path('error/noPerm/', noPerm, name="noPerm"),
]
