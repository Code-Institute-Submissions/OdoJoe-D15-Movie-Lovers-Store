from django.db import models


class Subscriber(models.Model):
    """
    Model to record user
    subscriptions to newsletter
    """
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.email
