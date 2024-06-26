from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm
from userauths.models import Profile , User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileUpdateForm
from .models import Profile

def register_user(request):
    if request.user.is_authenticated:
        return redirect('blogApp:home')  # Adjust this to your profile view name or URL
    else:
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            profile_form = ProfileUpdateForm(request.POST, request.FILES)
            if user_form.is_valid() and profile_form.is_valid():
                # Save User object
                user = user_form.save()

                # Extract profile form data
                bio = profile_form.cleaned_data.get('bio', None)
                profile_picture = profile_form.cleaned_data.get('profile_picture', None)

                # Create Profile object linked to the user
                Profile.objects.create(user=user, bio=bio, profile_picture=profile_picture)

                # Log in the user after successful registration
                login(request, user)

                # Redirect to home or profile page
                messages.success(request, f'Account created for {user.username}! You are now logged in.')
                return redirect('blogApp:home')  # Adjust this to your profile view name or URL
            else:
                # Handle form validation errors
                messages.error(request, 'Form validation error. Please check the form fields.')
        else:
            user_form = UserRegistrationForm()
            profile_form = ProfileUpdateForm()

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'register.html', context)



def login_user(request):
    if request.user.is_authenticated:
        return redirect('blogApp:home') 
    else:   
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                my_user = User.objects.get(email=email)
                if my_user is not None:
                    password = form.cleaned_data.get('password')
                    user = authenticate(request, username=email, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, f'Welcome back, {user.username}!')
                        return redirect('blogApp:home')  # Replace 'home' with your desired redirect URL
                    else:
                        messages.error(request, 'Invalid email or password. Please try again.')
                else:
                    messages.error(request, 'User Not Exist. Please try again.')
                    return redirect('blogApp:home')  # Replace 'home' with your desired redirect URL

        else:
            form = UserLoginForm()
        return render(request, 'login.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('userauths:login')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profile.html', context)
