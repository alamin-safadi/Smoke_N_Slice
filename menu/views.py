from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Category

@login_required
def menu(request):
    categories = Category.objects.all()
    items = Item.objects.filter(is_available=True)
    
    if request.method == 'POST':
        selected_items = []
        for key, value in request.POST.items():
            if key.startswith('item_') and value != '0':
                item_id = key.replace('item_', '')
                quantity = int(value)
                if quantity > 0:
                    selected_items.append({
                        'item_id': item_id,
                        'quantity': quantity
                    })
        
        if selected_items:
            request.session['selected_items'] = selected_items
            return redirect('orders:create_order')
        else:
            from django.contrib import messages
            messages.error(request, 'Please select at least one item')
    
    return render(request, 'menu/menu.html', {
        'categories': categories,
        'items': items
    })