# yourapp/backends.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Use the custom user model
        UserModel = get_user_model()

        # Assume 'username' is actually the email
        try:
            # Use the email field instead of username for authentication
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None

        # Check if the password is correct
        if user.check_password(password):
            return user
        
        return None