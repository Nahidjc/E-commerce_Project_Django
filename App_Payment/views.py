from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from App_Order.models import Order
from App_Payment.forms import BillingForm
from App_Payment.models import BillingAddress

from django.contrib.auth.decorators import login_required


@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    form = BillingForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.success(request, f"Shipping Address Saved!")
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_total = order_qs[0].get_totals()
    return render(request, 'App_Payment/checkout.html', context={'form': form, 'order_qs': order_qs, 'order_total': order_total})
