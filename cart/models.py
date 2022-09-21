from django.db import models

from accounts.models import Agent, Customer
from product.models import Prod


class AgentEarn(models.Model):
	agent 	= models.ForeignKey(Agent, on_delete=models.CASCADE)
	total 	= models.FloatField(default=0)
	isPaid 	= models.BooleanField(default=False)

	def __str__(self):
		return self.agent.user.username

class Cart(models.Model):
	customer 	= models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)

	#These field can be removed when there is no more agent
	agent 		= models.ForeignKey(AgentEarn, on_delete=models.SET_NULL, blank=True, null=True) #Big BUG, The two models should not interfere with each other
	agentEarn 	= models.FloatField(blank=True, null=True)
	location 	= models.CharField(max_length=100, blank=True, null=True)

	total 		= models.FloatField(default=0)
	isComplete	= models.BooleanField(default=False)
	isOrdered 	= models.BooleanField(default=False)

	timestamp	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "is ordered = " + str(self.isOrdered) + " - is completed = " + str(self.isComplete)


class CartProd(models.Model):
	cart 		= models.ForeignKey(Cart, on_delete=models.CASCADE)
	prod 		= models.ForeignKey(Prod, on_delete=models.CASCADE)

	quantity 	= models.IntegerField(default=1)
	total 		= models.FloatField(default=0)
	def __str__(self):
		return self.cart.__str__() + " - " + self.prod.__str__()

