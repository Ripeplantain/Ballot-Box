from django.shortcuts import render, redirect
from .models import Candidate, Election, Vote
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.decorators import allowed_users
from django.core.cache import cache

# Create your views here.

def landing_page(request):
    """
    Landing page view
    """
    return render(request, 'core/landing.html')

@login_required(login_url='login')
def home_view(request):
    """
    Home view
    """

    if cache.get('elections'):
        elections = cache.get('elections')
    else:
        elections = Election.objects.all()
        cache.set('elections',elections,60)

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

    voted_before = Vote.objects.filter(election=id, voter=request.user).exists()
    if voted_before:
        messages.error(request, 'You have already voted in this election')
        return redirect('home')
    else:
        if cache.get('candidates'):
            candidates = cache.get('candidates')
        else:
            candidates = Candidate.objects.filter(election=id)
            cache.set('candidates',candidates,60)
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
    if request.user.profile.registered == False:
        messages.error(request, 'You must verify your account before you can vote')
        return redirect('profile')
    else:
        candidate = Candidate.objects.get(id=id)
        vote = Vote.objects.create(election=candidate.election, candidate=candidate, voter=request.user)
        vote.save()
        messages.success(request, 'Vote casted successfully')

        return redirect('home')



@login_required(login_url='login')
def results_view(request):
    """
    Display results
    """

    if cache.get('elections'):
        elections = cache.get('elections')
    else:
        elections = Election.objects.all()
        cache.set('elections',elections,60)

    user_groups = request.user.groups.all()
    group_names = [group.name for group in user_groups]

    context = {
                'group_names': group_names,
                'elections': elections,
    }

    return render(request,'core/results.html',context)


@login_required(login_url='login')
def box_view(request,id):
    """
    View election result here
    """

    if cache.get(id):
        candidates = cache.get(id)
    else:
        candidates = Candidate.objects.filter(election=id)
        cache.set(id,candidates,60)

    user_groups = request.user.groups.all()
    group_names = [group.name for group in user_groups]
    votes = Vote.objects.filter(election=id)

    context = {
        'candidates': candidates,
        'group_names': group_names,
        'votes': votes,
    }


    return render(request, 'core/box.html',context)
