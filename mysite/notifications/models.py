from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid


class Notification(models.Model):
    """
    Model which represents a Notification.
    """

    id = models.UUIDField(
        verbose_name=_('Notification ID'),
        primary_key=True,
        default=uuid.uuid1,
        help_text=_('An ID which represents a specific Notification.'),
        editable=False,
    )

    date_created = models.DateTimeField(
        verbose_name=_('Date Created'),
        help_text=_('When the notification was created.'),
        auto_now_add=True,
        editable=False,
    )

    description = models.CharField(
        verbose_name=_('Description'),
        help_text=_('The description of the notification.'),
        max_length=1000,
    )

    mac_address = models.CharField(
        verbose_name=_('MAC Address'),
        help_text=_('The MAC Address of the device on the network.'),
        max_length=17,
    )

    def __str__(self):
        return 'MAC: {},  Description: {}'.format(self.mac_address, self.description)
