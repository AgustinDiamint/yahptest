from django.db import models


class Investment(models.Model):
    investment_type = models.CharField(max_length=255)
    manager = models.CharField(max_length=255)
    investment_desc = models.TextField()

    def __str__(self):
        return self.investment_type


class Workers(models.Model):
    internal_id = models.IntegerField(default=0)
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + self.last_name
