from django.contrib.auth.models import User
from django.db import models

"""
Customer Information this will change depending on the complexity of the site
like if we start registering user there will be no need to take their name because it will be already
handle in the user model.
You can also customize the information for users in here or create other relationship relating to user
"""
class Customer(models.Model):
	user 			= models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

	name 			= models.CharField(max_length=100)
	phoneNumber 	= models.IntegerField()	

	def __str__(self):
		return self.name + " - " + str(self.phoneNumber)

"""
Agent model same as customer it is customizable depending on need and complexity of site.
You can also create other relationship associated with agent model
"""

class Agent(models.Model):
	user 		= models.OneToOneField(User, on_delete=models.CASCADE)

	idNumber 	= models.IntegerField()
	phoneNumber = models.IntegerField(blank=True, null=True)
	promoCode 	= models.CharField(max_length=100, unique=True)
	accepted 	= models.BooleanField(default=False)

	def __str__(self):
		return str(self.idNumber) + " - promocode = " + self.promoCode + "- accepted - " + str(self.accepted)