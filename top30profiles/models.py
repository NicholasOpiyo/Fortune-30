from django.db import models

# Model for initial profile information
class InitialInsights(models.Model):
    company = models.CharField(max_length=100)
    revenue = models.IntegerField()
    employees = models.IntegerField()
    industry = models.CharField(max_length=100)
    headquarters = models.CharField(max_length=100)
    fortune_100_rank = models.IntegerField()
    logo = models.CharField(max_length=100)

    def _str_(self):
        return self.company
