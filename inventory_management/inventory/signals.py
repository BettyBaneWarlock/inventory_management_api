from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Signal receiver to create an authentication token for new users
@receiver(post_save, sender=User)  # Connects this function to the post_save signal for the User model
def create_auth_token(sender, instance=None, created=False, **kwargs):
    # Check if the User instance is newly created
    if created:
        # Generate and assign a new authentication token to the user
        Token.objects.get_or_create(user=instance)
