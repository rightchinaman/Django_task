# Yes, Django signals run in the same database transaction as the caller.
# In the code below a signal is used to modify an attribute of a model.
# Then it is verified that the change is applied in the same transaction as the save operation.

from django.db import models
from django.db.models.signals import post_save

class App(models.Model):
    function = models.CharField(max_length=100)

def post_save_handler(sender, instance, **kwargs):
    print("Signal handler executed.")
    instance.function = "Modified by signal"
    print(f"function changed to: {instance.function}")

post_save.connect(post_save_handler, sender=App)

def create_app():
    print("Creating App instance")
    app = App(function="Function")
    app.save() 
    print(f"function saved : {app.function}")

if __name__ == "__main__":
    create_app()

    app = App.objects.first()
    print(f"Final function in the database: {app.function}")
