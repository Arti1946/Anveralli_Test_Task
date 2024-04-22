from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import OrderForm
from .models import Order


def orders_list(request):
    orders = Order.objects.select_related("executor", "customer")
    return render(
        request, "orders/orders_list.html", {"orders": orders, "lk": False}
    )


def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, "orders/order_detail.html", {"order": order})


@login_required
def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST or None)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect("orders:order_detail", order_id=order.id)
        return render(request, "orders/order_create.html", {"form": form})
    form = OrderForm(request.POST or None)
    return render(request, "orders/order_create.html", {"form": form})


@login_required
def lk_orders_list(request):
    lk = True
    if request.user.role == settings.ROLES["Customer"]:
        orders = Order.objects.filter(customer=request.user).select_related(
            "executor", "customer"
        )
    else:
        orders = Order.objects.filter(executor=request.user).select_related("executor", "customer")
    context = {"orders": orders, "lk": lk}
    return render(request, "orders/orders_list.html", context)
