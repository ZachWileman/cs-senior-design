from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid
# from settings.models import Attack


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

    attack = models.CharField(
        verbose_name=_('Attack'),
        help_text=_('An object that represents the Attack.'),
        max_length=50,
    )

    dest_address = models.GenericIPAddressField(
        verbose_name=_('Destination Address'),
        help_text=_('The Destination Address of the device on the network.'),
    )

    source_address = models.GenericIPAddressField(
        verbose_name=_('Source Address'),
        help_text=_('The specific source address of the attack (if one exists).'),
        null=True,
        blank=True,
    )

    THREAT_LEVELS = (
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('Severe', 'Severe'),
    )

    threat_level = models.CharField(
        verbose_name=_('Threat Level'),
        help_text=_('The Threat Level of the Attack.'),
        max_length=8,
        choices=THREAT_LEVELS,
    )

    def __str__(self):
        return 'MAC: {},  Description: {}'.format(self.mac_address, self.description)
