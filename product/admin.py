from django.contrib import admin

from . models import (
	Category,
	Prod,
	ProdMedia,
	SubCategory,
#	RequestedProd,
	)

admin.site.register(Category)
admin.site.register(Prod)
admin.site.register(ProdMedia)
admin.site.register(SubCategory)
#admin.site.register(RequestedProd)
