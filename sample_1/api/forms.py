from django.forms import ModelForm
from .models import Comments

class confession_form(ModelForm):
    class meta:
        model = Comments
        fields = '__all__'