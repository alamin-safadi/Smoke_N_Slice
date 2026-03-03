from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from orders.models import Order
from .models import Payment
import stripe
import json

# Stripe configuration
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def process_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, staff=request.user)
    
    if order.status == 'paid':
        messages.warning(request, 'This order has already been paid')
        return redirect('menu:menu')
    
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        
        if not payment_method:
            messages.error(request, 'Please select a payment method')
            return render(request, 'payments/payment.html', {'order': order})
        
        try:
            # Create Stripe Payment Intent
            if payment_method == 'card':
                # For card payments, create Stripe Checkout Session
                checkout_session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=[{
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': f'Order #{order.order_number}',
                                'description': 'Smoke N Slice Order Payment',
                            },
                            'unit_amount': int(order.final_amount * 100),  # Convert to cents
                        },
                        'quantity': 1,
                    }],
                    mode='payment',
                    success_url=request.build_absolute_uri(
                        reverse('payments:payment_success', kwargs={'order_id': order.id})
                    ) + '?session_id={CHECKOUT_SESSION_ID}',
                    cancel_url=request.build_absolute_uri(
                        reverse('payments:payment_cancel', kwargs={'order_id': order.id})
                    ),
                    metadata={
                        'order_id': order.id,
                        'staff_id': request.user.id
                    }
                )
                
                # Create pending payment record
                payment = Payment.objects.create(
                    order=order,
                    payment_method=payment_method,
                    amount=order.final_amount,
                    stripe_payment_intent_id=checkout_session.payment_intent,
                    status='pending'
                )
                
                # Redirect to Stripe Checkout
                return redirect(checkout_session.url)
                
            elif payment_method == 'mobile_banking':
                # For mobile banking - simulate success for demo
                payment = Payment.objects.create(
                    order=order,
                    payment_method=payment_method,
                    amount=order.final_amount,
                    status='completed'
                )
                
                # Update order status
                order.status = 'paid'
                order.save()
                
                messages.success(request, f'Mobile banking payment successful! Order #{order.order_number} is now paid.')
                return redirect('payments:payment_success', order_id=order.id)
                
        except stripe.error.StripeError as e:
            messages.error(request, f'Payment failed: {str(e)}')
            return render(request, 'payments/payment.html', {'order': order})
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return render(request, 'payments/payment.html', {'order': order})
    
    return render(request, 'payments/payment.html', {
        'order': order,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })

@login_required
def payment_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, staff=request.user)
    
    # Get session ID from Stripe callback
    session_id = request.GET.get('session_id')
    
    if session_id:
        try:
            # Retrieve Stripe session
            session = stripe.checkout.Session.retrieve(session_id)
            
            if session.payment_status == 'paid':
                # Update payment status
                payment = Payment.objects.get(
                    stripe_payment_intent_id=session.payment_intent
                )
                payment.status = 'completed'
                payment.save()
                
                # Update order status
                order.status = 'paid'
                order.save()
                
                messages.success(request, 'Card payment completed successfully!')
            else:
                messages.warning(request, 'Payment is still processing...')
                
        except stripe.error.StripeError as e:
            messages.error(request, f'Error verifying payment: {str(e)}')
    
    # Get the latest payment record
    try:
        payment = Payment.objects.filter(order=order).latest('created_at')
    except Payment.DoesNotExist:
        payment = None
    
    return render(request, 'payments/payment_success.html', {
        'order': order,
        'payment': payment
    })

@login_required
def payment_cancel(request, order_id):
    order = get_object_or_404(Order, id=order_id, staff=request.user)
    messages.warning(request, 'Payment was cancelled. You can try again.')
    return redirect('payments:process_payment', order_id=order.id)