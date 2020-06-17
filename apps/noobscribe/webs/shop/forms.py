from django import forms
from django.contrib.auth import get_user_model
from noobscribe.plans.models import Product
from noobscribe.sales.models import SalesOrder, Cart


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('owner', 'product', 'quantity')
    
    owner = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=get_user_model().objects.all()
    )
    product = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=Product.objects.all()
    )
    quantity = forms.ChoiceField(
        widget=forms.Select,
        choices=[(x, x) for x in range(1, 11)],
    )


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = SalesOrder
        fields = ('promo_code', 'note')