from django.db import models
import uuid
class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
'''
REMINDER: if changed run the following on local repo folder
>python manage.py makemigrations
>python manage.py migrate
'''