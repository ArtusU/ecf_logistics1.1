from django.forms import ModelForm
from orders.models import * 


class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = ['full_name', 'email', 'phone']

class AddressForm(ModelForm):
    class Meta:
        model = Delivery_Address
        fields = '__all__'
        exclude = ['recipient']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'comments']


class StatusOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'comments', 'status', 'delivery_day', 'run']