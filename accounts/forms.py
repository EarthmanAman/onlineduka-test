from django import forms
from . models import Agent, Customer

class CreateAgentForm(forms.ModelForm):

	class Meta:
		model = Agent
		fields = [
			'idNumber',
			'phoneNumber',
		]

class CreateCustomerForm(forms.ModelForm):

	class Meta:
		model = Customer
		fields = [
			'name',
			'phoneNumber',
		]