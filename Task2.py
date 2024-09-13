# Yes, the Django signals run in the same thread as the caller by default.
# In this code the output will give ID for the threads being run by the signal handler and caller.
# Both the IDs will be same which shows that same thread is being run by signal and caller.

from django.db import models
from django.db.models.signals import post_save
import threading

class SecondModel(models.Model):
    title = models.CharField(max_length=100)

def post_save_handler(sender, instance, **kwargs):
    print(f"ID: {threading.get_ident()}")

post_save.connect(post_save_handler, sender=SecondModel)

def save_second_model():
    print(f"ID: {threading.get_ident()}")
    instance = SecondModel(title="Thread Test")
    instance.save()

