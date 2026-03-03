from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from menu.models import Item
from decimal import Decimal  

@login_required
def create_order(request):
    selected_items = request.session.get('selected_items', [])
    
    if not selected_items:
        messages.error(request, 'No items selected. Please go back to menu and select items.')
        return redirect('menu:menu')
    
    items_with_details = []
    total_amount = 0
    
    for selected_item in selected_items:
        try:
            item = Item.objects.get(id=selected_item['item_id'], is_available=True)
            quantity = selected_item['quantity']
            subtotal = item.price * quantity
            total_amount += subtotal
            
            items_with_details.append({
                'item': item,
                'quantity': quantity,
                'subtotal': subtotal
            })
        except Item.DoesNotExist:
            continue
    
    if request.method == 'POST':
        
        discount_input = request.POST.get('discount_percent', '0')
        discount_percent = Decimal(discount_input)
        
        if discount_percent < 0 or discount_percent > 100:
            messages.error(request, 'Discount percentage must be between 0 and 100')
            return render(request, 'orders/create_order.html', {
                'items': items_with_details,
                'total_amount': total_amount
            })
        
        # Create order
        order = Order(
            staff=request.user,
            total_amount=total_amount,
            discount_percent=discount_percent
        )
        order.save()
        
        # Create order items
        for item_detail in items_with_details:
            OrderItem.objects.create(
                order=order,
                item=item_detail['item'],
                quantity=item_detail['quantity'],
                price=item_detail['item'].price
            )
        
        # Clear session
        request.session['selected_items'] = []
        
        # Redirect to payment
        return redirect('payments:process_payment', order_id=order.id)
    
    return render(request, 'orders/create_order.html', {
        'items': items_with_details,
        'total_amount': total_amount
    })