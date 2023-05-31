from django.db.models.signals import post_save
from .models import Customer
from django.contrib.auth.models import User, Group


def create_customer(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            name=instance.username,
            user=instance
        )
        print('Customer is created and group is linked!')

post_save.connect(create_customer,sender=User)