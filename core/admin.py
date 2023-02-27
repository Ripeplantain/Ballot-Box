from django.contrib import admin
from .models import Candidate, Election, Vote, Party, Profile

# Register your models here.

admin.site.register(Candidate)
admin.site.register(Election)
admin.site.register(Vote)
admin.site.register(Party)
admin.site.register(Profile)