from django.forms import ModelForm
from .models import Confessions

class confession_form(ModelForm):
    class meta:
        model = Confessions
        fields = '__all__'