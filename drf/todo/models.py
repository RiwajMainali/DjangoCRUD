from django.db import models

class Todo(models.Model):
    title= models.CharField(verbose_name="hello", max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    isComplete= models.BooleanField(default=False)

