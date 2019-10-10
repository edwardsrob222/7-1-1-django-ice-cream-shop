from django.db import models

# Create your models here.

from django.db import models
import datetime

class IceCream(models.Model):


    DAILY = 'Daily'
    WEEKLY = 'Weekly'
    SEASONAL = 'Seasonal'

    VANILLA = 'Vanilla'
    CHOCOLATE = 'Chocolate'

    BASE_CHOICES = [
        (VANILLA, 'Vanilla'),
        (CHOCOLATE, 'Chocolate'),
    ]

    AVAILABLE_CHOICES = [
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (SEASONAL, 'Seasonal')
    ]

    flavor =  models.CharField(max_length=200)
    base = models.CharField(max_length=200, choices=BASE_CHOICES)
    available = models.CharField(max_length=200, choices=AVAILABLE_CHOICES)
    featured = models.BooleanField(default=False)
    date_churned = models.DateField('Date Churned', default=datetime.date.today)
    likes = models.IntegerField(default=0)

    def __str__(self):
          return self.flavor

    def get_absolute_url(self):
        return reverse('ice_cream:index')
