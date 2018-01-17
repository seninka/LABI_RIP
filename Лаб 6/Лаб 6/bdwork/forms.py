from django.forms import ModelForm
from .models import Ser_f_users


class ServesForm(ModelForm):
    class Meta:
        model = Ser_f_users
        fields = ['price','type_of_serves']

