from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    # This class will show when the rooms and etc are created and updated
    # auto now add =
    created = models.DateTimeField(auto_now_add=True)
    # auto now = Useful for "last-modified"
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
