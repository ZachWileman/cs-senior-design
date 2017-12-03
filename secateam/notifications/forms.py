from django.forms import ModelForm
from .models import Notification


class NotificationForm(ModelForm):
    """
    This class is used for creating a form by using the Notification model.
    """

    class Meta:
        exclude = ('id', 'date_created',)
        model = Notification
