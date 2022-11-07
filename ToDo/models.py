from django.db import models

# Create your models here.


class ToDo(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
