from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required # for profile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST': # come request
        form = UserRegisterForm(request.POST) # to fill the form
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required # for profile https://www.youtube.com/watch?v=FsAPt_9Bf3U
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
            
    else:
        u_form = UserUpdateForm(instance=request.user) # current information about the user instance=request
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error