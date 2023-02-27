from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# This code sets up a signal handler using the @receiver decorator. The signal handler is triggered whenever a User instance is saved (either created or updated), and creates a new Token instance for that user
@receiver(post_save, sender=User, weak=False)

# The 'sender' argument is the model class that sent the signal (in this case, User)
# The 'instance' argument is the instance of the User model that was saved. 
# The 'created' argument is a boolean indicating whether the instance was just created (as opposed to updated). 
# The '**kwargs' argument is used to accept any additional keyword arguments that may be sent with the signal.
def report_uploaded(sender, instance, created, **kwargs):

    # If the User instance was just created (i.e., created is True), the function creates a new Token instance for that user by calling Token.objects.create(user=instance). This creates a new token associated with the given user and saves it to the database. 
    if created:
        Token.objects.create(user=instance)