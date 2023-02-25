from django.shortcuts import render
from .models import Election

# Create your views here.

def home_view(request):
    """
    Home view
    """

    elections = Election.objects.all()

    context = {'elections': elections}
    return render(request, 'core/home.html',context)


def election_view(request, id):
    """
    Election view
    """

    election = Election.objects.get(id=id)

    context = {'election': election}
    return render(request, 'core/election.html',context)