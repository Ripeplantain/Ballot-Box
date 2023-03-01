from django.shortcuts import render,redirect
from .forms import CreateUserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import authenticated_user
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse, HttpResponse

from core.models import Profile
from .email import send_otp_via_email


# Create your views here.

def register_view(request):
    """
    This view will handle the registration of a new user
    """

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='voter')
            user.groups.add(group)
            
            messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html',context)


@authenticated_user
def login_view(request):
    """
    This view will handle the login of a user
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # return JsonResponse({'username': username, 'password': password})
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Username or password is incorrect')

    return render(request, 'account/login.html')


def logout_view(request):
    """
    This view will handle the logout of a user
    """
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile_view(request):
    """
    This view will handle the profile of a user
    """

    user_groups = request.user.groups.all()
    group_names = [group.name for group in user_groups]

    profile = Profile.objects.get(user=request.user.id)
    context = {
                'profile': profile,
                'group_names': group_names
            }
    return render(request, 'account/profile.html',context)


@login_required(login_url='login')
def verify_view(request):
    """
    This view will handle the verification of a user
    """

    if request.user.profile.registered:
        messages.error(request, 'You are already verified')
        return redirect('home')
    else:
        form = ProfileForm()
        send_otp_via_email(request.user.email)
        messages.success(request, 'OTP has been sent to your email')

        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():
                if form.cleaned_data.get('otp') == request.user.profile.otp:
                    data = form.save(commit=False)
                    data.registered = True
                    data.save()
                    return redirect('home')

        context = {
            'form': form
        }
        return render(request, 'account/verify.html',context)