from django.db import models

# Create your models here.
class compliments(models.Model):
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.text