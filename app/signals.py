from django.db.models.signals import pre_save, post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(instance, **kwargs):
    if kwargs.get('created'):
        print("token created for user")
        Token.objects.create(user=instance)