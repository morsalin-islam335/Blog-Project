from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class UpdateProfile(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        