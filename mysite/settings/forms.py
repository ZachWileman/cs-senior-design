from django.forms import ModelForm
from .models import Attack
from django.forms.widgets import TextInput


class AttackForm(ModelForm):
    """
    This class is used for creating a form by using the Attack model.
    """

    class Meta:
        model = Attack
        fields = '__all__'
