from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from App_Order.models import Order
from App_Payment.forms import BillingForm
from App_Payment.models import BillingAddress

from django.contrib.auth.decorators import login_required


@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    return render(request, 'App_Payment/checkout.html', context={'saved_address': saved_address})
