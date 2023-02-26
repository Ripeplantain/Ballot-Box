from django.shortcuts import render, redirect
from .models import Candidate, Election, Vote
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.decorators import allowed_users

# Create your views here.

@login_required(login_url='login')
def home_view(request):
    """
    Home view
    """

    elections = Election.objects.all()
    user_groups = request.user.groups.all()
    group_names = [group.name for group in user_groups]

    context = {
                'elections': elections,
                'group_names': group_names
            }
    return render(request, 'core/home.html',context)

@login_required(login_url='login')
def election_view(request, id):
    """
    Election view
    """

    candidates = Candidate.objects.filter(election=id)
    user_groups = request.user.groups.all()
    group_names = [group.name for group in user_groups]

    context = {
                'candidates': candidates,
                'group_names': group_names
                }
    return render(request, 'core/candidate.html',context)

@login_required(login_url='login')
def vote_view(request, id):
    """
    Vote view
    """

    candidate = Candidate.objects.get(id=id)
    vote = Vote.objects.create(election=candidate.election, candidate=candidate, voter=request.user)
    vote.save()
    messages.success(request, 'Vote casted successfully')

    return redirect('home')

@login_required(login_url='login')
@allowed_users(allowed_roles=['agent'])
def dashboard_view(request):
    """
    Dashboard view
    """

    user_groups = request.user.groups.all()
    group_names = [group.name for group in user_groups]
    # elections = Election.objects.all()
    context = {
                'group_names': group_names
    }
    return render(request, 'core/dashboard.html',context)