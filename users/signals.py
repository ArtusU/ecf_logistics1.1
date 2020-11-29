from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from orders.models import Referrer


@receiver(post_save, sender=User)
def create_referrer(sender, instance, created, **kwargs):
    if created:
        Referrer.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_referrer(sender, instance, **kwargs):
    instance.referrer.save()