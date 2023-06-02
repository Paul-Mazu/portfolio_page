from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=20)
    def __str__(self):
        return f"#{self.name} "