# It is by default that Django signals are executed synchronously. 
# In the code below the "Step 1" will will be be printed first. Then, due to pre_save "Step 2" will be printed by the signal handler.
# After this finally "Step 3" will be printed by the caller.

from django.db.models.signals import pre_save
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)

def my_signal_handler(sender, instance, **kwargs):
    print("Step 2")

pre_save.connect(my_signal_handler, sender=MyModel)

def create_instance():
    print("Step 1")
    instance = MyModel(name="Test Instance")
    instance.save()
    print("Step 3")
