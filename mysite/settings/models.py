from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Attack(models.Model):

    # ATTACK_CHOICES = (
    #     ('SYN Flood Attack', 'SYN Flood Attack'),
    #     ('Christmas Tree Attack', 'Christmas Tree Attack'),
    # )

    name = models.CharField(
        verbose_name=_('Attack Name'),
        help_text=_('The name of the attack being detected.'),
        max_length=50,
        primary_key=True,
    )

    # Bool value which represents whether or not the Attack is being detected currently
    detection = models.BooleanField(
        verbose_name=_('Detection'),
        help_text=_('Bool value which represents whether or not this Attack is being detected.'),
        default=True,
    )

    def __str__(self):
        return '{}: {}'.format(self.name, self.detection)
