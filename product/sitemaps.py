from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from . models import Prod, SubCategory


class ProductSitemap(Sitemap):

    def items(self):
        return Prod.objects.all().order_by("-pk")

class SubCategorySitemap(Sitemap):

    def items(self):
        return SubCategory.objects.all().order_by("-pk")



class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index']

    def location(self, obj):
        return reverse("product:%s" % obj)