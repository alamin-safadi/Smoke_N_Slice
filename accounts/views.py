from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def staff_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            if user.is_staff:
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Welcome {user.username}!')
                    return redirect('menu:menu')
                else:
                    messages.error(request, 'Invalid password')
            else:
                messages.error(request, 'This account is not staff')
        except User.DoesNotExist:
            messages.error(request, 'No staff account found with this email')
    
    return render(request, 'accounts/login.html')

@login_required
def staff_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('accounts:login')