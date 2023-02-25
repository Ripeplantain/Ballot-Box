from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

# Create your views here.

def register_view(request):
    """
    This view will handle the registration of a new user
    """

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html',context)

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

    return render(request, 'account/login.html')