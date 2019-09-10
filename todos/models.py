from django.db import models

# Create your models here.


class Todo(models.Model):
    title=models.CharField(max_length=200)
    due_date=models.DateField()


    def __str__(self):
        return self.title
