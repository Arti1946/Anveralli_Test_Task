from core.roles import Role
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import OrderForm
from .models import Order, OrdersResponses
from users.models import CustomUser


def orders_list(request):
    orders = Order.objects.select_related("customer").filter(executor=None)
    return render(
        request, "orders/orders_list.html", {"orders": orders, "lk": False}
    )


def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    reply = None
    if request.user.role == Role.EXECUTOR and request.user.is_authenticated:
        reply = OrdersResponses.objects.filter(
            orders=order, responses=request.user
        ).exists()
    return render(
        request, "orders/order_detail.html", {"order": order, "reply": reply}
    )


@login_required
def order_create(request):
    if request.user.is_authenticated and request.user.role == Role.CUSTOMER:
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
    raise PermissionError("Только заказчик может создавать заказы")


@login_required
def lk_orders_list(request):
    lk = True
    if request.user.role == Role.CUSTOMER:
        orders = Order.objects.filter(customer=request.user).select_related(
            "customer", "executor"
        )
    else:
        orders = Order.objects.filter(executor=request.user).select_related(
            "customer", "executor"
        )
    context = {"orders": orders, "lk": lk}
    return render(request, "orders/orders_list.html", context)


@login_required
def choose_executor(request, order_id, responser_id):
    order = get_object_or_404(Order, id=order_id)
    responser = get_object_or_404(CustomUser, id=responser_id)
    order.executor = responser
    order.save()
    return redirect("orders:order_detail", order_id=order_id)


@login_required
def reply_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.user.is_authenticated and request.user != order.customer:
        OrdersResponses.objects.get_or_create(
            orders=order, responses=request.user
        )
    return redirect("orders:responses")


@login_required
def responses(request):
    resp = OrdersResponses.objects.filter(responses=request.user)
    return render(request, "orders/responses.html", {"resp": resp})
