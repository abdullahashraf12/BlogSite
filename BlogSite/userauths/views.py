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
from django.core.exceptions import ObjectDoesNotExist



from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileUpdateForm
from .models import Profile, User

def register_user(request):
    if request.user.is_authenticated:
        return redirect('blogApp:home')  # Redirect to home if user is already logged in
    else:
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            profile_form = ProfileUpdateForm(request.POST, request.FILES)
            
            if user_form.is_valid() and profile_form.is_valid():
                email = user_form.cleaned_data['email']

                # Check if email already exists
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'An account with this email address already exists. Please log in.')
                    return redirect('userauths:login')
                
                # Create new user and profile if email does not exist
                user = user_form.save()
                bio = profile_form.cleaned_data.get('bio', None)
                profile_picture = profile_form.cleaned_data.get('profile_picture', None)
                Profile.objects.create(user=user, bio=bio, profile_picture=profile_picture)
                
                # Log in the user after successful registration
                login(request, user)
                
                # Redirect to home or profile page
                messages.success(request, f'Account created for {user.username}! You are now logged in.')
                return redirect('blogApp:home')
                
            else:
                # Form is not valid, handle the error message
                if User.objects.filter(email=user_form.data['email']).exists():
                    messages.error(request, 'An account with this email address already exists. Please log in.')
                for field, errors in user_form.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
        
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
                password = form.cleaned_data.get('password')

                print("Cleanned Email "+ str(email))

                try:
                    # Attempt to get the user object
                    user = User.objects.get(email=email)
                    
                    # Attempt to authenticate the user
                    user_auth = authenticate(request, username=email, password=password)

                    if user is not None and user_auth is not None and user == user_auth:
                        # User exists and credentials are correct
                        login(request, user)
                        messages.success(request, f'Welcome back, {user.username}!')
                        return redirect('blogApp:home')  # Redirect to home or any other desired URL after successful login
                    else:
                        # Password is incorrect
                        messages.error(request, 'Invalid password. Please try again.')
                        return redirect('userauths:login')  # Redirect back to login page
                except ObjectDoesNotExist:
                    # Handle the case where User object does not exist
                    messages.error(request, 'User does not exist. Please try again.')
                    return redirect('userauths:login')  # Redirect back to login page


            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
                                # messages.error(request, 'Invalid email or password. Please try again.')

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
