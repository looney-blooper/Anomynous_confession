from django.forms import ModelForm
from .models import Confessions

class confession_form(ModelForm):
    class Meta:
        model = Confessions
        fields = ['confession']