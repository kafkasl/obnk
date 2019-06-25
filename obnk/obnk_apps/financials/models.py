# -*- coding: utf-8 -*-

# Django modules
from django.db import models

from obnk_apps.users.models import User


class Transfer(models.Model):
    source_user = models.ForeignKey(User, related_name="outgoing_transfers")
    target_user = models.ForeignKey(User, related_name="incoming_transfers")

    amount = models.FloatField()
    description = models.TextField(blank=True, max_length=20)

    class Meta:
        verbose_name_plural = "Transfers"

    def __unicode__(self):
        return "%s -> %s [%.2f]: %s" % (
        self.source_user.uuid, self.target_user.uuid, self.amount,
        self.description)
