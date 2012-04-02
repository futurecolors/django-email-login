from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailBackend(ModelBackend):
    
    def authenticate(self, email=None, password=None):
        try:
            user = User.objects.get(email__iexact=email.lower())
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None