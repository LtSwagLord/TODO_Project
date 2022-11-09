from django.db import models

# Create your models here.


class Task(models.Model):
    task_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    creator = models.ForeignKey('auth.user', related_name='tasks', on_delete=models.CASCADE)
    # One is to Many Relation

    def __str__(self):
        return self.task_name
