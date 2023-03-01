from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.models import User
from core.models import Profile

import random


def send_otp_via_email(email):
    subject = 'Your account verfication email'
    otp = random.randint(1000,9999)
    message = f"Your otp is {otp}"
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
    user_obj = User.objects.get(email=email)
    profile = Profile.objects.get(user=user_obj)
    profile.otp = otp
    profile.save()
