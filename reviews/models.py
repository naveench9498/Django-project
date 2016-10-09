from django.db import models


class Car(models.Model):
    company = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000,null=True)


    def __unicode__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    car = models.ForeignKey(Car)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
