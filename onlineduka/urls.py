"""onlineduka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.sitemaps.views import sitemap

from product.sitemaps import ProductSitemap, StaticViewSitemap, SubCategorySitemap

sitemaps = {
    'product': ProductSitemap,
    'subcategory':SubCategorySitemap,
    'static': StaticViewSitemap
}


urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('cart/', include('cart.urls', namespace="cart")),
    path('', include('product.urls', namespace="product")),


    path('pass/password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name="password_reset"),
    path('pass/password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('pass/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),  name='password_reset_confirm'),
    path('pass/password_reset_complete/', auth_views. PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
