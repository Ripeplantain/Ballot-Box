from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.decorators import allowed_users

from core.models import Profile, Vote
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['agent'])
def dashboard_view(request):
    """
    Dashboard view
    """

    user_groups = request.user.groups.all()
    group_names = [group.name for group in user_groups]
    registered_users = Profile.objects.filter(registered=True).count()
    unregister_users = Profile.objects.filter(registered=False).count()
    users = User.objects.all().count()
    votes = Vote.objects.all().count()
    voted_users = Vote.objects.all().values('voter').distinct().count()

    context = {
                'group_names': group_names,
                'registered_users': registered_users,
                'unregister_users': unregister_users,
                'users': users,
                'votes': votes,
                'voted_users': voted_users,
    }
    return render(request, 'agent/dashboard.html',context)
