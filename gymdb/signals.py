from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Rol

@receiver(post_migrate)
def crear_roles(sender, **kwargs):
    # ensure this runs only for this app's migrations
    if sender.name == "gymdb":
        for nombre in ["admin", "usuario", "coach"]:
            Rol.objects.get_or_create(nombre=nombre)