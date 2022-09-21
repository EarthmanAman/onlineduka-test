from django.contrib import admin
from django.urls import path

from . views import (
	createAgent,
	confirmAgent,
	deleteAgent,
	agentsList,
	agentDetail,
	agentPay,

	contact,
	login_user,
	logout_user,

	agentInfo,
	agentPaidJobs,
	)

app_name = "accounts"

urlpatterns = [
    path('create/agent/', createAgent, name="createAgent"),
    path('confirm/<int:agentId>//', confirmAgent, name="confirmAgent"),
    path('delete/<int:agentId>/agent/', deleteAgent, name="deleteAgent"),

    path('agent/<int:agentId>/pay/', agentPay, name="agentPay"),

    path('agentlist/', agentsList, name="agentsList"),
    path('agentdetail/<int:agentId>/agent/', agentDetail, name="agentDetail"),
    path('contact/', contact, name="contact"), 
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),

    path('agent-info/', agentInfo, name="agentInfo"), 
    path('agent-paid-jobs/<int:agentId>/', agentPaidJobs, name="agentPaidJobs"), 
]
