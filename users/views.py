from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserUpdateForm, ReferrerForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please login.')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def referrer(request):
    orders = request.user.referrer.order_set.all().order_by('-date_created')
    context = {
        'orders': orders
    }
    
    return render(request, 'users/referrer.html', context)

@login_required
def referrerSettings(request):
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        referrer_form = ReferrerForm(request.POST, instance=request.user.referrer)
        if user_form.is_valid() and referrer_form.is_valid():
            user_form.save()
            referrer_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('referrer')

    else:
        user_form = UserUpdateForm(instance=request.user)
        referrer_form = ReferrerForm(instance=request.user.referrer)
    
    context = {
        'user_form': user_form,
        'referrer_form': referrer_form
    }
    
    return render(request, 'users/referrer_settings.html', context)





