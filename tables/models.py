from django.db import models


# Create your models here.
class Table(models.Model):
    author_name = models.CharField( max_length=100 )
    patent = models.CharField( max_length=100)
    year = models.CharField( max_length=100)
    title = models.CharField( max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

