from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from orders.filters import OrderFilter, DriverOrderFilter
from .models import Order
from orders.forms import OrderForm, RecipientForm, AddressForm, UpdateAddressForm, StatusOrderForm



def welcome(request):
    return render(request, 'orders/welcome.html')


@login_required
def adminOrders(request):
    orders = Order.objects.all()
    
    new_orders = Order.objects.all().count()
    monday_orders = Order.objects.filter(delivery_day='Monday').count()
    tuesday_orders = Order.objects.filter(delivery_day='Tuesday').count()
    wednesday_orders = Order.objects.filter(delivery_day='Wednesday').count()
    thursday_orders = Order.objects.filter(delivery_day='Thursday').count()
    friday_orders = Order.objects.filter(delivery_day='Friday').count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs.order_by('-date_created')
    #orders = myFilter.qs.order_by('delivery_address__post_code')


    context = {
        'new_orders': new_orders,
        'orders': orders,
        'monday_orders': monday_orders,
        'tuesday_orders': tuesday_orders,
        'wednesday_orders': wednesday_orders,
        'thursday_orders': thursday_orders,
        'friday_orders': friday_orders,
        'myFilter': myFilter,
        'google_map_api_key': settings.GOOGLE_MAP_API_KEY
    }
    return render(request, 'orders/admin_orders.html', context)


@login_required
def driverOrders(request):
    orders = Order.objects.filter(status='Out for delivery')

    DriverFilter = DriverOrderFilter(request.GET, queryset=orders)
    orders = DriverFilter.qs.order_by('delivery_address__post_code')
    
    context = {
        'orders': orders,
        'DriverFilter': DriverFilter
        }
    return render(request, 'orders/driver_orders.html', context)


@login_required
def orderCreate(request):
    ord_form = OrderForm()
    recipient_form = RecipientForm()
    address_form = AddressForm()

    if request.method == 'POST':
        recipient_form = RecipientForm(request.POST)
        address_form = AddressForm(request.POST)
        ord_form = OrderForm(request.POST)

        if recipient_form.is_valid() and address_form.is_valid() and ord_form.is_valid():
            
            obj_recipient = recipient_form.save(commit=False)
            obj_recipient.refereed_by = request.user.referrer
            obj_recipient.save()

            obj_address = address_form.save(commit=False)
            obj_address.recipient = obj_recipient
            obj_address.save()
            
            obj_order = ord_form.save(commit=False)
            obj_order.referrer = request.user.referrer
            obj_order.recipient = obj_recipient
            obj_order.delivery_address = obj_address
            obj_order.save()
            
            return redirect('/referrer/')


    context = {
        'recipient_form': recipient_form,
        'address_form': address_form,
        'ord_form': ord_form,   
    }
    return render(request, 'orders/order_create.html', context)


@login_required
def orderDetails(request, pk):
    order_details = Order.objects.get(id=pk)
    context = {
        'order_details': order_details
    }
    return render(request, 'orders/order_details.html', context)


@login_required
def orderUpdate(request, pk):
    order = Order.objects.get(id=pk)
    ord_form = StatusOrderForm(instance=order)
    recipient_form = RecipientForm(instance=order.recipient)
    address_form = UpdateAddressForm(instance=order.delivery_address)

    if request.method == 'POST':
        #form = OrderForm(request.POST, instance=order)
        ord_form = StatusOrderForm(request.POST, instance=order)
        recipient_form = RecipientForm(request.POST, instance=order.recipient)
        address_form = UpdateAddressForm(request.POST, instance=order.delivery_address)
        
        if recipient_form.is_valid() and address_form.is_valid() and ord_form.is_valid():
            recipient_form.save()
            address_form.save()
            ord_form.save()

            return redirect('admin-orders')

    context = {
        'recipient_form': recipient_form,
        'address_form': address_form,
        'ord_form': ord_form,   
    }
    return render(request, 'orders/order_create.html', context)


@login_required
def orderDelete(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('referrer')
	context = {'item':order}
	return render(request, 'orders/order_delete.html', context)





