from django.shortcuts import render, get_object_or_404, redirect
#authentications
from django.contrib.auth.decorators import login_required
# model
from app_order.models import Cart, Order
from app_shop.models import Product
# message
from django.contrib import messages

# Create your views here.

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_items.filter(item=item).exists():
            order_item[0].quantity +=1
            order_item[0].save()
            messages.info(request, "This item quantity was updated")
            return redirect("app_shop:home")
        else:
            order.order_items.add(order_item[0])
            messages.info(request, "This item was added to your cart")
            return redirect("app_shop:home")
    else:
        order = Order(user=request.user)
        order.save()
        order.order_items.add(order_item[0])
        messages.info(request, "This item was added to your cart")
        return redirect("app_shop:home")

# view cart details

@login_required
def cartview(request):
    carts = Cart.objects.filter(user=request.user, purchased = False)
    orders = Order.objects.filter(user=request.user, ordered = False)
    if carts.exists() and orders.exists():
        order = orders[0]
        return render (request, 'app_order/cart.html', context={'carts': carts, 'order':order})
    else:
        messages.warning(request, "Cart empty!")
        return redirect('app_shop: home')

# remove item
@login_required()
def remove_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.order_items.filter(item=item).exists():
            order_item = Cart.objects.filter(
                item=item, user=request.user, purchased=False)[0]
            order.order_items.remove(order_item)
            order_item.delete()
            messages.warning(request, "This item was removed form your cart")
            return redirect("app_order:cart")

        else:
            messages.info(request, "This item was not in your cart")
            return redirect("app_shop:home")
    else:
        messages.info(request, "You don't have an active order!")
        return redirect("app_shop:home")
