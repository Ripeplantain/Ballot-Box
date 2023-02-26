from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .decorators import authenticated_user
from django.contrib.auth.models import Group

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