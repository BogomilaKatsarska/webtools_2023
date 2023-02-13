from django.db import models


class Employee(models.Model):
    first_name = models.CharField(
        max_length=15,
    )
    last_name = models.CharField(
        max_length=15,
    )
    age = models.PositiveIntegerField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
