from django.contrib import admin
from .models import Candidate, Election, Vote, Party

# Register your models here.

admin.site.register(Candidate)
admin.site.register(Election)
admin.site.register(Vote)
admin.site.register(Party)