#A forms.py file is created when something need to be submitted!
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta():
        #password1 and password2 is for verifing the password
        fields = ('username','email','password1','password2')
        model = get_user_model()

        def __init__(self):
            #Reference docs
            super().__init__(self,*args,**kwargs)
            self.fields['username'].label = 'Display Name'
            self.fields['email'].label = 'Email Address'
