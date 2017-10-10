from django.db import models

# Create your models here.
class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # Adds the current now of when the model is created_at
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
