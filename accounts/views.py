from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from .forms import (
    CreateAgentForm,
    CreateCustomerForm,
)

from cart.models import AgentEarn, Cart

from .models import (
    Agent,
    Customer,
)


def login_user(request):
    template_name = "./form/login.html"
    if request.method == "POST":
        try:
            username = int(request.POST.get("username"))
        except:
            username = request.POST.get("username")
        password = request.POST.get("password")

        userIn = authenticate(username=username, password=password)
        if userIn:
            login(request, userIn)
            next_endpoint = request.GET.get("next", "")
            return redirect("/")
    return render(request, template_name)


def logout_user(request):
    logout(request)
    return redirect("/")


"""
Agent section
"""


def createAgent(request):
    template_name = "./form/createAgent.html"
    userAval = False
    if request.method == "POST":
        idNumber = int(request.POST.get("idNumber"))
        phoneNumber = int(request.POST.get("phoneNumber"))
        email = request.POST.get("email")
        password = request.POST.get("password")
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        userIn = User.objects.filter(username=phoneNumber)

        if userIn.exists():
            userAval = True
        else:
            user = User(
                username=phoneNumber,
                email=email,
                first_name=firstName,
                last_name=lastName,
            )
            user.set_password(password)
            user.save()
            checkAgent = Agent.objects.filter(idNumber=idNumber)
            if checkAgent.exists():
                userAval = True
            else:
                agent = Agent(
                    user=user,
                    idNumber=idNumber,
                    promoCode=str(phoneNumber),
                    phoneNumber=phoneNumber,
                )
                agent.save()
                login(request, user)
                return redirect(
                    "accounts:agentInfo"
                )  # After registering go back to index page

    context = {"userAval": userAval}
    return render(request, template_name, context)


@login_required
def confirmAgent(request, agentId):
    if request.user.is_superuser:
        agent = get_object_or_404(Agent, pk=agentId)
        agent.accepted = not agent.accepted
        agent.save()
    return redirect("accounts:agentsList")


@login_required
def deleteAgent(request):
    if request.method == "POST" and request.user.is_superuser:
        agentId = int(request.POST.get("agentId"))
        agent = get_object_or_404(Agent, pk=agentId)
        agent.delete()
    return redirect("accounts:agents")


@login_required
def agentsList(request):
    if request.user.is_superuser:
        template_name = "./agentsList.html"
        agents = Agent.objects.all()
        context = {"agents": agents}
        return render(request, template_name, context)
    else:
        return redirect("product:noPerm")


@login_required
def agentDetail(request, agentId):
    if request.user.agent or request.user.is_superuser:
        added = False
        template_name = "./agentDetail.html"
        agent = get_object_or_404(Agent, idNumber=agentId)
        agentEarns = agent.agentearn_set.filter(isPaid=False).order_by("-pk")
        if request.method == "POST":
            earn = int(request.POST.get("earn"))
            cartId = int(request.POST.get("cartId"))
            cart = get_object_or_404(Cart, pk=cartId)
            cart.agentEarn = earn
            agentEarn = cart.agent
            agentEarn.total += earn
            agentEarn.save()
            cart.save()
            added = True
        context = {"agentEarns": agentEarns, "agent": agent, "added": added}
        return render(request, template_name, context)
    else:
        return redirect("product:noPerm")


@login_required
def agentPaidJobs(request, agentId):
    template_name = "./agentPaidJobs.html"
    agent = get_object_or_404(Agent, idNumber=agentId)
    paidJobs = agent.agentearn_set.filter(isPaid=True)
    context = {"paidJobs": paidJobs}
    return render(request, template_name, context)


@login_required
def agentPay(request, agentId):
    agent = get_object_or_404(AgentEarn, pk=agentId)
    agent.isPaid = True
    agent.save()
    newAgentEarn = AgentEarn(agent=agent.agent)
    newAgentEarn.save()
    return redirect("accounts:agentsList")


def contact(request):
    template_name = "./contact.html"
    send = False
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phoneNumber = request.POST.get("phoneNumber")
        message = request.POST.get("message")
        message = "Customer Name : {}\n Phone number : {}\nCustomer Email : {} \n Message :\n {}".format(
            name, phoneNumber, email, message
        )
        to_email = email
        email = EmailMessage("CONTACT", message, to=["contact@hashimathman.com"])
        email.send()
        send = True
    context = {"send": send}

    return render(request, template_name, context)


@login_required
def agentInfo(request):
    template_name = "./agentInfo.html"
    return render(request, template_name)
