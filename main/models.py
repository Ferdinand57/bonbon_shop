from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2) # for price that involve fractions
    description = models.TextField()

    def __str__(self):
        return self.name
    
'''
REMINDER: if changed run the following on local repo folder
>python manage.py makemigrations
>python manage.py migrate
'''