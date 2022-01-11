from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process_checkout(request):
    product= Product.objects.get(id=request.POST['id'])
    new_order = Order.objects.create(
        quantity_ordered=request.POST["quantity"], 
        total_price= product.price
    )
    return redirect(f'/checkout/{new_order.id}')

def display_checkout(request, order_id):
    order = Order.objects.get(id=order_id)
    total_charge = order.quantity_ordered * order.total_price
    history_order_total = Order.objects.aggregate(Sum('total_price'))['total_price__sum']
    history_order_items = Order.objects.aggregate(Sum('quantity_ordered'))['quantity_ordered__sum']
    context = {
        'total_charge' : total_charge,
        'total_quanity' : order.quantity_ordered,
        'history_order_total': history_order_total,
        'history_order_items' : history_order_items,
    }
    return render(request, "store/checkout.html", context)
