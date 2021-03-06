from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.conf import settings
from community.models import Community
from django.utils import timezone
from randomslugfield import RandomSlugField

class BadgeClass(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=140)
    # imagefield is why we need PILLOW installed
    image = models.ImageField(
        upload_to='uploads/badges/',
    )
    slug = RandomSlugField(
        length=7,
        unique=True
    )
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='badgeclass_creator',
    )
    created_on = models.DateField(default=datetime.now)
    is_available = models.BooleanField(default=False)
    is_discontinued = models.BooleanField(default=False)

    EARNABLE_BY_CHOICES = (
        ('earner', 'earner'),
        ('moderator', 'moderator'),
    )

    earnable_by = models.CharField(
        max_length=10,
        choices=EARNABLE_BY_CHOICES,
        default='earner',
    )

    instances = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BadgeInstance',
        related_name='badgeclass_instances', through_fields=('badge_class', 'earner'))

    class Meta:
        verbose_name = 'class'
        verbose_name_plural = 'classes'
        db_table = 'badgeclass'

    def __str__(self):
        return self.name

class BadgeInstance(models.Model):
    badge_class = models.ForeignKey(
        BadgeClass,
        on_delete=models.CASCADE,
    )
    earner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='badgeinstance_recipient',
    )
    recieved_on = models.DateField(default=datetime.now)
    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='badgeinstance_assigned_by',
        blank=True,
        null=True,
    )

    visible_in_profile = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'instance'
        verbose_name_plural = 'instances'
        db_table = 'badgeinstance'

    def __str__(self):
        return self.earner.username
