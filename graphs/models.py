from django.db import models

class Data(models.Model):
    city = models.CharField(max_length=220)
    cases = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.city, self.cases)
