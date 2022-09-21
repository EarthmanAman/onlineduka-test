from django.contrib import admin

from . models import (
	Agent,
	Customer,
	)

admin.site.register(Agent)
# admin.site.register(Customer)