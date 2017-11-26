from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid
from settings.models import Attack


#Attack = 'settings.Attack'

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

    attack = models.ForeignKey(
        Attack,
        on_delete=models.CASCADE,
        verbose_name=_('Attack'),
        help_text=_('An object that represents the Attack.'),
        max_length=50,
    )

    mac_address = models.CharField(
        verbose_name=_('MAC Address'),
        help_text=_('The MAC Address of the device on the network.'),
        max_length=17,
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
