from django.db import transaction, models
from django.views.generic import ListView, FormView
from django.shortcuts import get_object_or_404, HttpResponseRedirect, HttpResponse, reverse
from noobscribe.plans.models import Quota, Product
from noobscribe.sales.models import Cart, SalesOrder, OrderItem

from .forms import CheckoutForm, CartForm


class ProductIndexView(ListView):
    """ Quota Index View """
    model = Quota
    template_name = 'shop/product_list.html'


class CartView(ListView):
    model = Cart
    template_name = 'shop/cart_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


def cart_add_product(request):
    if request.method != 'POST':
        return Http404
    product_id=request.POST.get('product')
    product = get_object_or_404(Product, pk=product_id)
    item = Cart.objects.add_product(request, product)
    return HttpResponseRedirect(reverse('cart_index'))
    

def cart_remove_product(request):
    if request.method != 'POST':
        return Http404
    item_id=request.POST.get('item')
    item = get_object_or_404(Cart, pk=item_id)
    item.delete()
    return HttpResponseRedirect(reverse('cart_index'))


class CheckoutView(FormView):
    form_class = CheckoutForm
    template_name = 'shop/checkout_view.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = Cart.objects.user_cart(self.request)
        total = items.aggregate(price=models.Sum('product__price'))
        context.update({
            'object_list': items,
            'total': total['price']
        })
        return context

    def get_success_url(self):
        return reverse('shop_index')

    def form_valid(self, form):
        with transaction.atomic():
            items = Cart.objects.user_cart(self.request)
            order = SalesOrder(owner=self.request.user)
            order.save()
            for item in items:
                order_item = OrderItem(order=order, product=item.product)
                order_item.save()
            items.delete()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))