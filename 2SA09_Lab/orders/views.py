from django.shortcuts import render

from django.db import transaction
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from accounts.decorators import token_required
from accounts.models import Profile
from cart.models import CartItem
from orders.models import Order, OrderItem

@csrf_exempt
@require_http_methods(["POST"])
@token_required
def checkout_view(request):
    items = (
        CartItem.objects
        .filter(user=request.user)
        .select_related("product")
    )

    if not items.exists():
        return JsonResponse({"error": "ตะกร้าว่าง"}, status=400)

    profile, _ = Profile.objects.get_or_create(user=request.user)

    with transaction.atomic():
        total = sum(i.product.price * i.qty for i in items)
        order = Order.objects.create(
            user=request.user,
            address=profile.address,
            total=total
        )

        for i in items:
            OrderItem.objects.create(
                order=order,
                product=i.product,
                price=i.product.price,
                qty=i.qty
            )

        items.delete()

    return JsonResponse({"order_id": order.id}, status=201)

@require_http_methods(["GET"])
@token_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = []
    for it in order.items.select_related("product"):
        order_item = {
            "name": it.product.name,
            "price": str(it.price),
            "qty": it.qty
        }
        order_items.append(order_item)

    return JsonResponse({
        "id": order.id,
        "address": order.address,
        "total": str(order.total),
        "status": order.status,
        "created": order.created.isoformat(),
        "items": order_items
    })

@require_http_methods(["GET"])
@token_required
def order_history(request):
    orders = (
        Order.objects
        .filter(user=request.user)
        .prefetch_related("items__product")
        .order_by("-created")
    )
    orders_list = []
    for o in orders:
        order_dto = {
            "id": o.id,
            "total": str(o.total),
            "status": o.status,
            "created": o.created.isoformat()
        }
        orders_list.append(order_dto)

    return JsonResponse({"orders": orders_list})