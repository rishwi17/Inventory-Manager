from django.db import models

# Create your models here.

class Item(models.Model):

    type = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Available'),
        ('SOLD', 'Out of Stock'),
        ('RESTOCKING', 'Coming Soon')
    )

    status = models.CharField(max_length=10, choices=choices, default='SOLD')
    issues = models.CharField(max_length=50, default="No Issues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)

class Furniture(Item):
    pass

class Fashion(Item):
    pass

class Gadgets(Item):
    pass
