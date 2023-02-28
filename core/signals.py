from .models import Profile, Vote, Candidate
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Vote)
def count_vote(sender, instance, created, **kwargs):
    if created:
        candidate = Candidate.objects.get(id=instance.candidate.id)
        votes = Vote.objects.filter(candidate=instance.candidate.id, election=instance.election.id).count()
        candidate.votes = votes
        candidate.save()