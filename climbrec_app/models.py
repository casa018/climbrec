from django.db import models
import uuid as uuid_lib
from django.utils.translation import gettext_lazy as _


# Create your models here.

"""
class Calendar_item(models.Model):
    uuid = models.UUIDField(default=uuid_lib.uuid4,
                            primary_key=True, editable=False)
    user_id = #foreign key
    #item_type = 
    start_date = models.DateTimeField(_('start date'), blank=True, null=True)
    end_date = models.DateTimeField(_('end date'), blank=True, null=True)
    location = models.CharField(_('location'), max_length=50, blank=True)
    comment = models.CharField(_('free comment'), max_length=200, blank=True)
    register_date = models.DateTimeField(_('register date'), blank=True, null=True)
    modify_date = models.DateTimeField(_('modify date'), blank=True, null=True)
    delete_flg = models.BooleanField(
        _('delete'),
        default=False,
        help_text=_(
            'Designates whether this item is valid'
        ),
    )
"""
